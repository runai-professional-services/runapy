from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class EnvironmentApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def create_environment_asset(
        self,
        environment_creation_request: Optional[
            models.EnvironmentCreationRequest
        ] = None,
    ):
        r"""


        ### Description
        Create an environment asset.

        ### Parameters:
        ```python
        environment_creation_request: EnvironmentCreationRequest
        ```
        environment_creation_request: See model EnvironmentCreationRequest for more information.

        ### Example:
        ```python
        EnvironmentApi(
            environment_creation_request=runai.EnvironmentCreationRequest()
        )
        ```
        """

        # Body params:
        body_params = environment_creation_request

        resource_path = f"/api/v1/asset/environment".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_environment_asset_by_id(
        self,
        asset_id: str,
    ):
        r"""


        ### Description
        Delete an environment asset.

        ### Parameters:
        ```python
        asset_id: str
        ```
        asset_id: Unique identifier of the asset.

        ### Example:
        ```python
        EnvironmentApi(
            asset_id='asset_id_example'
        )
        ```
        """

        resource_path = f"/api/v1/asset/environment/{asset_id}".replace("_", "-")
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_environment_asset_by_id(
        self,
        asset_id: str,
        usage_info: Optional[bool] = None,
        comply_to_project: Optional[int] = None,
        comply_to_workload_type: Optional[str] = None,
        comply_to_replica_type: Optional[str] = None,
    ):
        r"""


        ### Description
        Get an environment asset.

        ### Parameters:
        ```python
        asset_id: str
        usage_info: Optional[bool]
        comply_to_project: Optional[int]
        comply_to_workload_type: Optional[str]
        comply_to_replica_type: Optional[str]
        ```
        asset_id: Unique identifier of the asset.
        usage_info: Whether the query should include asset usage information as part of the response.
        comply_to_project: Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_workload_type: Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        ### Example:
        ```python
        EnvironmentApi(
            asset_id='asset_id_example',
                        usage_info=True,
                        comply_to_project=56,
                        comply_to_workload_type='comply_to_workload_type_example',
                        comply_to_replica_type='comply_to_replica_type_example'
        )
        ```
        """

        # Query params:
        query_params = [
            ("usageInfo", usage_info),
            ("complyToProject", comply_to_project),
            ("complyToWorkloadType", comply_to_workload_type),
            ("complyToReplicaType", comply_to_replica_type),
        ]
        resource_path = f"/api/v1/asset/environment/{asset_id}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def list_environment_assets(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        project_id: Optional[int] = None,
        department_id: Optional[str] = None,
        cluster_id: Optional[str] = None,
        usage_info: Optional[bool] = None,
        comply_to_project: Optional[int] = None,
        comply_to_workload_type: Optional[str] = None,
        distributed_framework: Optional[str] = None,
        is_distributed: Optional[bool] = None,
        is_training: Optional[bool] = None,
        is_workspace: Optional[bool] = None,
        is_inference: Optional[bool] = None,
        comply_to_replica_type: Optional[str] = None,
    ):
        r"""


        ### Description
        List environment assets.

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
        distributed_framework: Optional[str]
        is_distributed: Optional[bool]
        is_training: Optional[bool]
        is_workspace: Optional[bool]
        is_inference: Optional[bool]
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
        distributed_framework: Filter results to workload of type distributed and distributedFramework.
        is_distributed: Filter results to workload of type distributed.
        is_training: Filter results to workload of type training.
        is_workspace: Filter results to workload of type workspace.
        is_inference: Filter results to workload of type inference.
        comply_to_replica_type: Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        ### Example:
        ```python
        EnvironmentApi(
            name='name_example',
                        scope='scope_example',
                        project_id=56,
                        department_id='1',
                        cluster_id='d73a738f-fab3-430a-8fa3-5241493d7128',
                        usage_info=True,
                        comply_to_project=56,
                        comply_to_workload_type='comply_to_workload_type_example',
                        distributed_framework='distributed_framework_example',
                        is_distributed=True,
                        is_training=True,
                        is_workspace=True,
                        is_inference=True,
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
            ("distributedFramework", distributed_framework),
            ("isDistributed", is_distributed),
            ("isTraining", is_training),
            ("isWorkspace", is_workspace),
            ("isInference", is_inference),
            ("complyToReplicaType", comply_to_replica_type),
        ]
        resource_path = f"/api/v1/asset/environment".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def update_environment_asset_by_id(
        self,
        asset_id: str,
        environment_update_request: Optional[models.EnvironmentUpdateRequest] = None,
    ):
        r"""


        ### Description
        Update an environment asset.

        ### Parameters:
        ```python
        asset_id: str
        environment_update_request: EnvironmentUpdateRequest
        ```
        asset_id: Unique identifier of the asset.
        environment_update_request: See model EnvironmentUpdateRequest for more information.

        ### Example:
        ```python
        EnvironmentApi(
            asset_id='asset_id_example',
                        environment_update_request=runai.EnvironmentUpdateRequest()
        )
        ```
        """

        # Body params:
        body_params = environment_update_request

        resource_path = f"/api/v1/asset/environment/{asset_id}".replace("_", "-")
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
