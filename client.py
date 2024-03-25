import logging
import json
import requests
from typing import Optional, Any
from models import Cluster, Department, Project, NodePool
from controller import Controller, ClusterController, DepartmentController, ProjectController, NodePoolController

logger = logging.getLogger(__name__)

class RunaiClient:
    """
    RunaiClient is a python module that levarages Run:ai REST API https://app.run.ai/api/docs

    realm: The company's realm name, can be obtained from the UI login screen at app.run.ai -> app.run.ai/auth/realms/<realm>
    client_id: The application token name generated at the UI -> Applications
    client_secret: The application secret
    runai_base_url: The Run:ai company's domain name, for example: https://mycompany.run.ai
    """
    def __init__(
            self,
            realm: str,
            client_id: str,
            client_secret: str,
            runai_base_url: str):
        self._base_url = f"{runai_base_url}"
        self._api_token = self._generate_api_token(runai_base_url, realm, client_id, client_secret)
        self._headers = {"authorization": f"Bearer {self._api_token}", 'content-type': "application/json"}

    def _generate_api_token(self, runai_base_url: str, realm: str, client_id: str, client_secret: str):
        payload = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
        headers = {'content-type': "application/x-www-form-urlencoded"}
        url = f"{runai_base_url}/auth/realms/{realm}/protocol/openid-connect/token"
        try:
            response = requests.post(url, payload, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            if "access_token" not in response_json:
                raise SystemExit(f"failed to get access token from response. response body={response_json}")

            return response_json["access_token"]

        except requests.exceptions.HTTPError as err:
            print(f"failed to get api token. err={err}")
            raise SystemExit(err)
        except requests.exceptions.JSONDecodeError as err:
            print(f"failed to decode json response. err={err}")
            raise SystemExit(err)
    
    def request(self,
                 method,
                 url: str,
                 headers: object,
                 data: object = None) -> requests.Response:
        if data:
            logging.warning(f"Making call to: {url}...")
            resp = method(url=url, data=data, headers=headers)
        else:
            logging.warning(f"Making call to: {url}...")
            resp = method(url=url, headers=headers)
        if not resp or resp.status_code >= requests.codes.server_error:
            logger.warning(f"Failed to make call: {resp.text}")
            SystemExit("Failed to make HTTP call, exiting...")

        return resp

    def _get(self, url: str, data: Optional[Any]=None):
        logger.debug(f"GET: {url}")
        
        resp = self.request(requests.get,url=f"{self._base_url}{url}",headers=self._headers, data=data)
        
        if not resp.ok:
            logger.error(resp.text)
            SystemExit("Failed to make HTTP call, exiting...")

        logging.warning(f"resp: {resp.text}")
        return resp.json()

    def _post(self, url: str, data: dict):
        try:
            print(f"\n\nDATA: {data}\n\n")
            response = requests.post(f"{self._base_url}/{url}",
                                     data=data,
                                     headers=self._headers)
            print(f"\nRES: {response.json()}\n\n")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"error when trying to _post to url {url}, with data={data}. err={err}")
            raise SystemExit(err)

    def _put(self, url: str, data: dict):
        try:
            response = requests.put(f"{self._base_url}/{url}",
                                    data=data,
                                    headers=self._headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"error when trying to _put to url {url}, with data={data}. err={err}")
            raise SystemExit(err)

    def _delete(self, url: str):
        try:
            response = requests.delete(f"{self._base_url}/{url}",
                                       headers=self._headers)
            response.raise_for_status()
            if response.status_code == 202:
                # Skip response.json() for content that do not exist TODO: refactor this to no need if conditional statment
                return response.status_code
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"error when trying to _delete to url {url}, with err={err}")
            raise SystemExit(err)
    

    @property
    def clusters(self) -> Controller:
        return Controller.factory(Cluster, self)
    
    # TODO: If the object is called directly with RunaiClient.<object> need to include cluster_id, as it will not be included in the final state of the object
    @property
    def departments(self) -> Controller:
        return Controller.factory(Department, self)
    
    # TODO: If the object is called directly with RunaiClient.<object> need to include cluster_id, as it will not be included in the final state of the object
    @property
    def projects(self) -> Controller:
        return Controller.factory(Project, self)
    
    # TODO: If the object is called directly with RunaiClient.<object> need to include cluster_id, as it will not be included in the final state of the object
    @property
    def node_pools(self) -> Controller:
        return Controller.factory(NodePool, self)