from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class PVCApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def create_pvc_asset(
        self,
        pvc_creation_request: Optional[models.PVCCreationRequest] = None,
    ):
        r"""


        ### Description
        Create a PVC asset.

        ### Parameters:
        ```python
        pvc_creation_request: PVCCreationRequest
        ```
        pvc_creation_request: See model PVCCreationRequest for more information.

        ### Example:
        ```python
        PVCApi(
            pvc_creation_request=runai.PVCCreationRequest()
        )
        ```
        """

        # Body params:
        body_params = pvc_creation_request

        resource_path = f"/api/v1/asset/datasource/pvc".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_pvc_asset_by_id(
        self,
        asset_id: str,
    ):
        r"""


        ### Description
        Delete a PVC asset.

        ### Parameters:
        ```python
        asset_id: str
        ```
        asset_id: Unique identifier of the asset.

        ### Example:
        ```python
        PVCApi(
            asset_id='asset_id_example'
        )
        ```
        """

        resource_path = f"/api/v1/asset/datasource/pvc/{asset_id}".replace("_", "-")
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_pvc_asset_by_id(
        self,
        asset_id: str,
        usage_info: Optional[bool] = None,
        comply_to_project: Optional[int] = None,
        comply_to_workload_type: Optional[str] = None,
        status_info: Optional[bool] = None,
        comply_to_replica_type: Optional[str] = None,
    ):
        r"""


        ### Description
        Get a PVC asset.

        ### Parameters:
        ```python
        asset_id: str
        usage_info: Optional[bool]
        comply_to_project: Optional[int]
        comply_to_workload_type: Optional[str]
        status_info: Optional[bool]
        comply_to_replica_type: Optional[str]
        ```
        asset_id: Unique identifier of the asset.
        usage_info: Whether the query should include asset usage information as part of the response.
        comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        status_info: Whether the query should include asset status information as part of the response.
        comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        ### Example:
        ```python
        PVCApi(
            asset_id='asset_id_example',
                        usage_info=True,
                        comply_to_project=56,
                        comply_to_workload_type='comply_to_workload_type_example',
                        status_info=True,
                        comply_to_replica_type='comply_to_replica_type_example'
        )
        ```
        """

        # Query params:
        query_params = [
            ("usageInfo", usage_info),
            ("complyToProject", comply_to_project),
            ("complyToWorkloadType", comply_to_workload_type),
            ("statusInfo", status_info),
            ("complyToReplicaType", comply_to_replica_type),
        ]
        resource_path = f"/api/v1/asset/datasource/pvc/{asset_id}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def list_pvc_assets(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        project_id: Optional[int] = None,
        department_id: Optional[str] = None,
        cluster_id: Optional[str] = None,
        usage_info: Optional[bool] = None,
        comply_to_project: Optional[int] = None,
        comply_to_workload_type: Optional[str] = None,
        status_info: Optional[bool] = None,
        asset_ids: Optional[str] = None,
        comply_to_replica_type: Optional[str] = None,
    ):
        r"""


        ### Description
        List PVC assets.

        ### Parameters:
        ```python
        name: Optional[str]
        scope: Optional[str]
        project_id: Optional[int]
        department_id: Optional[str]
        cluster_id: Optional[str]
        usage_info: Optional[bool]
        comply_to_project: Optional[int]
        comply_to_workload_type: Optional[str]
        status_info: Optional[bool]
        asset_ids: Optional[str]
        comply_to_replica_type: Optional[str]
        ```
        name: Filter results by name.
        scope: Filter results by scope.
        project_id: Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets.
        department_id: Filter using the department id.
        cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        usage_info: Whether the query should include asset usage information as part of the response.
        comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        status_info: Whether the query should include asset status information as part of the response.
        asset_ids: Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs.
        comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        ### Example:
        ```python
        PVCApi(
            name='name_example',
                        scope='scope_example',
                        project_id=56,
                        department_id='1',
                        cluster_id='d73a738f-fab3-430a-8fa3-5241493d7128',
                        usage_info=True,
                        comply_to_project=56,
                        comply_to_workload_type='comply_to_workload_type_example',
                        status_info=True,
                        asset_ids='dbf4767e-2fa1-43b0-97a2-7c0cecda180b,550e8400-e29b-41d4-a716-44665544000a',
                        comply_to_replica_type='comply_to_replica_type_example'
        )
        ```
        """

        # Query params:
        query_params = [
            ("name", name),
            ("scope", scope),
            ("projectId", project_id),
            ("departmentId", department_id),
            ("clusterId", cluster_id),
            ("usageInfo", usage_info),
            ("complyToProject", comply_to_project),
            ("complyToWorkloadType", comply_to_workload_type),
            ("statusInfo", status_info),
            ("assetIds", asset_ids),
            ("complyToReplicaType", comply_to_replica_type),
        ]
        resource_path = f"/api/v1/asset/datasource/pvc".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def update_pvc_asset_by_id(
        self,
        asset_id: str,
        pvc_update_request: Optional[models.PVCUpdateRequest] = None,
    ):
        r"""


        ### Description
        Update a PVC asset.

        ### Parameters:
        ```python
        asset_id: str
        pvc_update_request: PVCUpdateRequest
        ```
        asset_id: Unique identifier of the asset.
        pvc_update_request: See model PVCUpdateRequest for more information.

        ### Example:
        ```python
        PVCApi(
            asset_id='asset_id_example',
                        pvc_update_request=runai.PVCUpdateRequest()
        )
        ```
        """

        # Body params:
        body_params = pvc_update_request

        resource_path = f"/api/v1/asset/datasource/pvc/{asset_id}".replace("_", "-")
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
