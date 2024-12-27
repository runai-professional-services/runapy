import datetime
import logging
import json
import base64
import threading
from typing import Optional, Any, Dict, Callable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from pydantic import BaseModel, HttpUrl, model_validator

from runai import assets
from . import errors
from . import controllers
from . import models

logger = logging.getLogger(__name__)


class RunaiClientConfig(BaseModel):
    runai_base_url: HttpUrl
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    cluster_id: Optional[str] = None
    retries: Optional[int] = None
    debug: Optional[bool] = False
    bearer_token: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def bearer_or_credentials(cls, values):
        client_id = values.get('client_id')
        client_secret = values.get('client_secret')
        bearer_token = values.get('bearer_token')

        if bearer_token is not None and (client_id is not None or client_secret is not None):
            raise errors.RunaiClientError('The parameter "bearer_token" cannot be set together with "client_id" and "client_secret"', None)

        if bearer_token is None and (client_id is None or client_secret is None):
            raise errors.RunaiClientError('The parameters "client_id" and "client_secret" must be set if "bearer_token" is not configured', None)

        return values


class RunaiClient:
    """
    RunaiClient class include all the modules to interact with the Run:ai REST API https://app.run.ai/api/docs
    """

    def __init__(
        self,
        runai_base_url: str,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        cluster_id: Optional[str] = None,
        retries: Optional[int] = None,
        debug: Optional[bool] = False,
        bearer_token: Optional[str] = None
    ):
        self.config = {
            "client_id": client_id,
            "client_secret": client_secret,
            "runai_base_url": runai_base_url,
            "cluster_id": cluster_id,
            "retries": retries,
            "debug": debug,
            "bearer_token": bearer_token,
        }
        models.build_model(model=RunaiClientConfig, data=self.config)

        self.cluster_id = cluster_id
        self.client_id = client_id
        self.client_secret = client_secret
        self._base_url = f"{runai_base_url}"
        self.bearer_token = bearer_token

        self._session = self._create_session(retries)

        self._token_refresh_thread_lock = threading.Lock()
        self._token_refresh_thread_is_locked = False

        self._api_token = None

        if bearer_token is None:  # Default to application token if CLIv2 token not provided
            self._api_token_expiary = None
            self._refresh_token()
        else:
            self._api_token = self.bearer_token
            self._session.headers.update({"Authorization": f"Bearer {self._api_token}"})

        if debug:
            logging.basicConfig(level=logging.DEBUG)

    def _create_session(self, retries: int) -> requests.Session:
        session = requests.Session()

        retries = Retry(
            total=retries if retries else 1,
            backoff_factor=2,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("https://", adapter)

        return session

    def _generate_api_token(self) -> str:
        headers = {"Accept": "*/*", "Content-type": "application/json"}
        data = json.dumps({"grantType": "app_token", "AppId": self.client_id, "AppSecret": self.client_secret})
        url = f"{self._base_url}/api/v1/token"
        try:
            logger.debug(f"Generating API token for client_id: {self.client_id} and cluster_id: {self.cluster_id}")
            resp = requests.post(url=url, data=data, headers=headers)
            if not resp.ok:
                raise errors.RunaiHTTPError(resp)
            resp_json = resp.json()
            if "accessToken" not in resp_json:
                raise errors.RunaiClientError(
                    message=f"Failed to get access token from response. Body={resp_json}", err=None)
            return resp_json["accessToken"]

        except requests.exceptions.JSONDecodeError as err:
            raise errors.RunaiClientError(
                message=f"Failed to decode response to json, response: {resp.text}", err=err)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as err:
            raise errors.RunaiClientError(
                message="Connection error occurred while generating API token.", err=err
            )

    def _set_token_expiary(self) -> None:
        token_payload = self._api_token.split(".")[1]
        token_payload_decoded = json.loads(base64.b64decode(token_payload + "=="))
        self._api_token_expiary = token_payload_decoded.get("exp", 0)

    def _is_token_about_to_expire(self) -> bool:
        if not self._api_token:
            return True  # If no token is set, treat it as expired
        current_time = datetime.datetime.now(datetime.timezone.utc)
        current_time_timestamp = current_time.timestamp()
        logger.debug(f"Token expires at: {datetime.datetime.fromtimestamp(self._api_token_expiary)} and current time is: {current_time}")
        # Check if the token will expire in the next 60 seconds
        return self._api_token_expiary - current_time_timestamp <= 60

    def _refresh_token(self):
        with self._token_refresh_thread_lock:
            self._token_refresh_thread_is_locked = True
            token = self._generate_api_token()
            logger.debug("API token refreshed successfully.")
            self._api_token = token
            self._set_token_expiary()
            self._session.headers.update({"Authorization": f"Bearer {token}"})
            logger.debug("Updated session headers with the new token.")
            self._token_refresh_thread_is_locked = False

    def _check_token_expired(self):
        if self.bearer_token is not None:  # Skip token refresh for CLIv2 token
            return

        if self._is_token_about_to_expire():
            logger.debug("Need to refresh token")
            if self._token_refresh_thread_is_locked is not True:
                self._refresh_token()
            else:
                logger.debug("Another thread is already refreshing the token. Skipping refresh")

    def config_cluster_id(self, cluster_id: str):
        # Validate cluster_id has UUID4 format
        _ = models.build_model(model=models.UUID4Model, data={"field": cluster_id})

        if cluster_id == self.cluster_id:
            logger.debug(f"cluster_id already configured to {cluster_id}, skipping...")
            return
        if cluster_id is not None:
            logger.debug(f"overriding cluster_id {self.cluster_id} with {cluster_id}")

        self.cluster_id = cluster_id

    def request(self, http_method: Callable, url: str, **kwargs: Any) -> requests.Response:
        self._check_token_expired()  # Refresh token if about to expire

        full_url = f"{self._base_url}{url}"
        logger.debug(f"Making {http_method.__name__.upper()} call to: {full_url}")

        try:
            resp = http_method(url=full_url, **kwargs)
            if not resp.ok:
                raise errors.RunaiHTTPError(resp)
            logger.debug(f"Request to {full_url} succeeded with status code: {resp.status_code}")
            return resp
        except requests.exceptions.RequestException as e:
            raise errors.RunaiClientError(message=f"Request failed for URL {full_url}", err=e)

    def get(self, url: str, params: Optional[Any] = None) -> Dict:
        logger.debug(f"Params: {params}")
        resp = self.request(self._session.get, url, params=params)
        return resp.json()

    def post(self, url: str, data: dict) -> Dict:
        logger.debug(f"Data: {data}")
        resp = self.request(self._session.post, url, data=data)
        return resp.json()

    def put(self, url: str, data: dict) -> Dict:
        logger.debug(f"Data: {data}")
        resp = self.request(self._session.put, url, data=data)
        if resp.headers["Content-Type"].__contains__("text/plain"):
            return resp.text
        return resp.json()

    def patch(self, url: str, data: dict) -> Dict:
        logger.debug(f"Data: {data}")
        resp = self.request(self._session.patch, url, data=data)
        if resp.headers["Content-Type"].__contains__("text/plain"):
            return resp.text
        return resp.json()

    def delete(self, url: str) -> Dict:
        resp = self.request(self._session.delete, url)
        if not resp.content:
            return {}
        if resp.headers["Content-Type"].__contains__("text/plain"):
            return resp.text
        return resp.json()

    @property
    def clusters(self) -> controllers.ClusterController:
        return controllers.ClusterController(self)

    @property
    def access_rules(self) -> controllers.AccessRulesController:
        return controllers.AccessRulesController(self)

    @property
    def roles(self) -> controllers.RolesController:
        return controllers.RolesController(self)

    @property
    def departments(self) -> controllers.DepartmentController:
        return controllers.DepartmentController(self)

    @property
    def projects(self) -> controllers.ProjectController:
        return controllers.ProjectController(self)
    
    @property
    def templates(self) -> controllers.TemplateController:
        return controllers.TemplateController(self)
    
    @property
    def compute(self) -> controllers.ComputeController:
        return controllers.ComputeController(self)

    @property
    def environments(self) -> controllers.EnvironmentController:
        return controllers.EnvironmentController(self)

    @property
    def node_pools(self) -> controllers.NodePoolController:
        return controllers.NodePoolController(self)

    @property
    def users(self) -> controllers.UsersController:
        return controllers.UsersController(self)

    @property
    def workloads(self) -> controllers.WorkloadsController:
        return controllers.WorkloadsController(self)

    @property
    def workspace(self) -> controllers.WorkspaceController:
        return controllers.WorkspaceController(self)

    @property
    def training(self) -> controllers.TrainingController:
        return controllers.TrainingController(self)

    @property
    def inference(self) -> controllers.InferenceController:
        return controllers.InferenceController(self)

    @property
    def distributed(self) -> controllers.DistributedController:
        return controllers.DistributedController(self)

    @property
    def assets(self) -> assets.AssetsFactory:
        return assets.AssetsFactory(self)
