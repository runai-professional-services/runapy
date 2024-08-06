import logging
from typing import Optional, Any, Dict, Callable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from . import errors
from . import controllers

logger = logging.getLogger(__name__)


class RunaiClient:
    """
    RunaiClient is a python pacakge that to interact with the Run:ai REST API https://app.run.ai/api/docs

    Parameters:

    - realm: The company's realm name, can be obtained from the UI login screen at app.run.ai -> app.run.ai/auth/realms/<realm>

    - client_id: The application token name generated at the UI -> Applications

    - client_secret: The application secret

    - runai_base_url: The Run:ai company's domain name, for example: https://mycompany.run.ai

    - cluster_id: The cluster ID

    - retries: Number of retries to perform on failed API calls due to intermittend network errors
    """

    def __init__(
        self,
        realm: str,
        client_id: str,
        client_secret: str,
        runai_base_url: str,
        cluster_id: str,
        retries: Optional[int] = None,
        debug: bool = False,
    ):
        self.cluster_id = cluster_id
        self._base_url = f"{runai_base_url}"
        self._session = self._create_session(
            runai_base_url, realm, client_id, client_secret, retries
        )
        if debug:
            logging.basicConfig(level=logging.DEBUG)

    def _create_session(
        self,
        runai_base_url: str,
        realm: str,
        client_id: str,
        client_secret: str,
        retries: int,
    ) -> requests.Session:

        session = requests.Session()
        api_token = self._generate_api_token(
            runai_base_url=runai_base_url,
            realm=realm,
            client_id=client_id,
            client_secret=client_secret,
        )
        session.headers.update(
            {"authorization": f"Bearer {api_token}",
             "content-type": "application/json"}
        )

        retries = Retry(
            total=retries if retries else 1,
            backoff_factor=2,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
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
                logger.error(f"Request failed: {resp}")
                raise errors.RunaiHTTPError(resp)
            resp_json = resp.json()
            if "access_token" not in resp_json:
                raise errors.RunaiClientError(
                    f"Failed to get access token from response. response body={resp_json}"
                )

            return resp_json["access_token"]

        except requests.exceptions.JSONDecodeError as err:
            logger.error(f"Failed to decode json response. err={err}")
            raise errors.RunaiClientError(err)

    def request(
        self, http_method: Callable, url: str, **kwargs: Any
    ) -> requests.Response:

        full_url = f"{self._base_url}{url}"
        logger.debug(f"Making {http_method.__name__.upper()} call to: {full_url}...")

        try:
            resp = http_method(url=full_url, **kwargs)
            if not resp.ok:
                logger.error(f"Request failed: [{resp.status_code}] - {resp.text}")
                raise errors.RunaiHTTPError(resp)
            logger.debug(f"Request to {full_url} succeeded with status code: {resp.status_code}")
            return resp
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for URL {url}: {e}")
            raise errors.RunaiError(f"Request failed for URL {url}: {e}")

    def get(self, url: str, params: Optional[Any] = None) -> Dict:
        resp = self.request(self._session.get, url, params=params)
        return resp.json()

    def post(self, url: str, data: dict) -> Dict:
        resp = self.request(self._session.post, url, data=data)
        return resp.json()

    def put(self, url: str, data: dict) -> Dict:
        resp = self.request(self._session.put, url, data=data)
        return resp.json()

    def delete(self, url: str) -> Dict:
        resp = self.request(self._session.delete, url)
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
