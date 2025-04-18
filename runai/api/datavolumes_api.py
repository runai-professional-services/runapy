from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class DatavolumesApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def count_datavolumes(
        self,
        request_type: models.DatavolumeRequestType,
        usable_in_project_id: Optional[str] = None,
        filter_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        Count data volumes.

        ### Parameters:
        ```python
        request_type: Optional[models.DatavolumeRequestType]
        usable_in_project_id: Optional[str]
        filter_by: Optional[List[str]]
        ```
        request_type: Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \&quot;usableInProjectId\&quot; query param.
        usable_in_project_id: Only when using \&quot;UsableInProject\&quot; requestType; Filter results for only datavolumes that are shared with - or originated in - the project.
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.

        ### Example:
        ```python
        DatavolumesApi(
            request_type=runai.DatavolumeRequestType(),
                        usable_in_project_id='5',
                        filter_by=['[\"name!=some-datavolume-name\"]']
        )
        ```
        """

        # Query params:
        query_params = [
            ("requestType", request_type),
            ("usableInProjectId", usable_in_project_id),
            ("filterBy", filter_by),
        ]
        resource_path = f"/api/v1/datavolumes/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def create_datavolume(
        self,
        datavolume_creation_fields: models.DatavolumeCreationFields,
    ):
        r"""


        ### Description
        Create a datavolume

        ### Parameters:
        ```python
        datavolume_creation_fields: DatavolumeCreationFields
        ```
        datavolume_creation_fields: The datavolume to create.

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_creation_fields=runai.DatavolumeCreationFields()
        )
        ```
        """

        # Body params:
        body_params = datavolume_creation_fields

        resource_path = f"/api/v1/datavolumes".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_datavolume(
        self,
        datavolume_id: str,
    ):
        r"""


        ### Description
        Delete datavolume

        ### Parameters:
        ```python
        datavolume_id: str
        ```
        datavolume_id: The id of the datavolume to retrieve

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_id='71f69d83-ba66-4822-adf5-55ce55efd210'
        )
        ```
        """

        resource_path = f"/api/v1/datavolumes/{datavolume_id}".replace("_", "-")
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_datavolume(
        self,
        datavolume_id: str,
    ):
        r"""


        ### Description
        Get datavolume

        ### Parameters:
        ```python
        datavolume_id: str
        ```
        datavolume_id: The id of the datavolume to retrieve

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_id='71f69d83-ba66-4822-adf5-55ce55efd210'
        )
        ```
        """

        resource_path = f"/api/v1/datavolumes/{datavolume_id}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_datavolume_shared_scopes(
        self,
        datavolume_id: str,
    ):
        r"""


        ### Description
        Get the datavolume&#39;s shared scopes

        ### Parameters:
        ```python
        datavolume_id: str
        ```
        datavolume_id: The id of the datavolume to retrieve

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_id='71f69d83-ba66-4822-adf5-55ce55efd210'
        )
        ```
        """

        resource_path = f"/api/v1/datavolumes/{datavolume_id}/shared_scopes".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_datavolumes(
        self,
        request_type: models.DatavolumeRequestType,
        usable_in_project_id: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        filter_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        List datavolumes in permitted scopes

        ### Parameters:
        ```python
        request_type: Optional[models.DatavolumeRequestType]
        usable_in_project_id: Optional[str]
        offset: Optional[int]
        limit: Optional[int]
        sort_by: Optional[str]
        sort_order: Optional[str]
        filter_by: Optional[List[str]]
        ```
        request_type: Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \&quot;usableInProjectId\&quot; query param.
        usable_in_project_id: Only when using \&quot;UsableInProject\&quot; requestType; Filter results for only datavolumes that are shared with - or originated in - the project.
        offset: The offset of the first item returned in the collection.
        limit: The maximum number of entries to return. - Default: 50
        sort_by: Sort results by a parameters.
        sort_order: Sort results in descending or ascending order. - Default: asc
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.

        ### Example:
        ```python
        DatavolumesApi(
            request_type=runai.DatavolumeRequestType(),
                        usable_in_project_id='5',
                        offset=100,
                        limit=50,
                        sort_by='sort_by_example',
                        sort_order=asc,
                        filter_by=['[\"name!=some-datavolume-name\"]']
        )
        ```
        """

        # Query params:
        query_params = [
            ("requestType", request_type),
            ("usableInProjectId", usable_in_project_id),
            ("offset", offset),
            ("limit", limit),
            ("sortBy", sort_by),
            ("sortOrder", sort_order),
            ("filterBy", filter_by),
        ]
        resource_path = f"/api/v1/datavolumes".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def patch_datavolume(
        self,
        datavolume_id: str,
        datavolume_patch_fields: models.DatavolumePatchFields,
    ):
        r"""


        ### Description
        Patch datavolume

        ### Parameters:
        ```python
        datavolume_id: str
        datavolume_patch_fields: DatavolumePatchFields
        ```
        datavolume_id: The id of the datavolume to retrieve
        datavolume_patch_fields: Datavolume to update.

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        datavolume_patch_fields=runai.DatavolumePatchFields()
        )
        ```
        """

        # Body params:
        body_params = datavolume_patch_fields

        resource_path = f"/api/v1/datavolumes/{datavolume_id}".replace("_", "-")
        method = "PATCH"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def patch_datavolume_shared_scopes(
        self,
        datavolume_id: str,
        shared_scopes_patch_request: models.SharedScopesPatchRequest,
    ):
        r"""


        ### Description
        Patch the datavolume&#39;s shared scopes

        ### Parameters:
        ```python
        datavolume_id: str
        shared_scopes_patch_request: SharedScopesPatchRequest
        ```
        datavolume_id: The id of the datavolume to retrieve
        shared_scopes_patch_request: Requested SharedScopes of the datavolume to patch.

        ### Example:
        ```python
        DatavolumesApi(
            datavolume_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        shared_scopes_patch_request=runai.SharedScopesPatchRequest()
        )
        ```
        """

        # Body params:
        body_params = shared_scopes_patch_request

        resource_path = f"/api/v1/datavolumes/{datavolume_id}/shared_scopes".replace(
            "_", "-"
        )
        method = "PATCH"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
