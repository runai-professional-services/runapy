import logging
from typing import Optional, Any, Dict, Callable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from pydantic import BaseModel, HttpUrl

from runai import assets
from . import errors
from . import controllers
from . import models

logger = logging.getLogger(__name__)


class RunaiClientConfig(BaseModel):
    realm: str
    client_id: str
    client_secret: str
    runai_base_url: HttpUrl
    cluster_id: Optional[str] = None
    retries: Optional[int] = None
    debug: Optional[bool] = False


class RunaiClient:
    """
    RunaiClient class include all the modules to interact with the Run:ai REST API https://app.run.ai/api/docs
    """

    def __init__(
        self,
        realm: str,
        client_id: str,
        client_secret: str,
        runai_base_url: str,
        cluster_id: Optional[str] = None,
        retries: Optional[int] = None,
        debug: Optional[bool] = False,
    ):
        config = {
            "realm": realm,
            "client_id": client_id,
            "client_secret": client_secret,
            "runai_base_url": runai_base_url,
            "cluster_id": cluster_id,
            "retries": retries,
            "debug": debug,
        }
        models.build_model(model=RunaiClientConfig, data=config)

        self.cluster_id = cluster_id
        self._base_url = f"{runai_base_url}"
        self._api_token = self._generate_api_token(
            runai_base_url=runai_base_url,
            realm=realm,
            client_id=client_id,
            client_secret=client_secret,
        )
        self._session = self._create_session(self._api_token, retries)
        if debug:
            logging.basicConfig(level=logging.DEBUG)

    def _create_session(
        self,
        api_token: str,
        retries: int,
    ) -> requests.Session:

        session = requests.Session()
        session.headers.update(
            {"authorization": f"Bearer {api_token}", "content-type": "application/json"}
        )

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

    def _generate_api_token(
        self, runai_base_url: str, realm: str, client_id: str, client_secret: str
    ) -> str:
        data = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
        headers = {"content-type": "application/x-www-form-urlencoded"}
        url = f"{runai_base_url}/auth/realms/{realm}/protocol/openid-connect/token"
        try:
            resp = requests.post(url, data=data, headers=headers)
            if not resp.ok:
                raise errors.RunaiHTTPError(resp)
            resp_json = resp.json()
            if "access_token" not in resp_json:
                raise errors.RunaiClientError(
                    message=f"Failed to get access token from response. Body={resp_json}",
                    err=None,
                )
            return resp_json["access_token"]

        except requests.exceptions.JSONDecodeError as err:
            raise errors.RunaiClientError(
                message=f"Failed to decode response to json, response: {resp.text}",
                err=err,
            )

    def config_cluster_id(self, cluster_id: str):
        # Validate cluster_id has UUID4 format
        _ = models.build_model(model=models.UUID4Model, data={"field": cluster_id})

        if cluster_id == self.cluster_id:
            logger.debug(f"cluster_id already configured to {cluster_id}, skipping...")
            return
        if cluster_id is not None:
            logger.debug(f"overriding cluster_id {self.cluster_id} with {cluster_id}")

        self.cluster_id = cluster_id

    def request(
        self, http_method: Callable, url: str, **kwargs: Any
    ) -> requests.Response:

        full_url = f"{self._base_url}{url}"
        logger.debug(f"Making {http_method.__name__.upper()} call to: {full_url}")

        try:
            resp = http_method(url=full_url, **kwargs)
            if not resp.ok:
                raise errors.RunaiHTTPError(resp)
            logger.debug(
                f"Request to {full_url} succeeded with status code: {resp.status_code}"
            )
            return resp
        except requests.exceptions.RequestException as e:
            raise errors.RunaiClientError(
                message=f"Request failed for URL {full_url}", err=e
            )

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
