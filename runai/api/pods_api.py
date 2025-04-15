from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class PodsApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def count_pods(
        self,
        deleted: Optional[bool] = None,
        filter_by: Optional[List[str]] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        Get pods count.

        ### Parameters:
        ```python
        deleted: Optional[bool]
        filter_by: Optional[List[str]]
        search: Optional[str]
        ```
        deleted: Return only deleted resources when &#x60;true&#x60;.
        filter_by: Filter results using a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contains, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;.
        search: Filter results by a free text search.

        ### Example:
        ```python
        PodsApi(
            deleted=True,
                        filter_by=['[\"nodeName!=some-node-name\"]'],
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("deleted", deleted),
            ("filterBy", filter_by),
            ("search", search),
        ]
        resource_path = f"/api/v1/workloads/pods/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    @deprecated_message()
    def get_pods(
        self,
        uuid: str,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        get all pods from a specific cluster. Deprecated - please use api/v1/workloads/pods instead

        ### Parameters:
        ```python
        uuid: str
        ```
        uuid: Unique identifier of the cluster

        ### Example:
        ```python
        PodsApi(
            uuid='uuid_example'
        )
        ```
        """

        resource_path = f"/v1/k8s/clusters/{uuid}/pods".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_workload_pod_metrics(
        self,
        workload_id: str,
        pod_id: str,
        metric_type: List[models.PodMetricType],
        start: datetime,
        end: datetime,
        number_of_samples: Optional[int] = None,
    ):
        r"""


        ### Description
        Get pod metrics data.

        ### Parameters:
        ```python
        workload_id: str
        pod_id: str
        metric_type: Optional[models.List[PodMetricType]]
        start: Optional[datetime]
        end: Optional[datetime]
        number_of_samples: Optional[int]
        ```
        workload_id: The  Universally Unique Identifier (UUID) of the workload.
        pod_id: The requested pod id.
        metric_type: Specify which metric data to request. Advanced GPU metrics are only supported if the &#39;Advanced GPU Metrics&#39; feature flag in the settings is enabled.
        start: Start date of time range to fetch data in ISO 8601 timestamp format.
        end: End date of time range to fetch data in ISO 8601 timestamp format.
        number_of_samples: The number of samples to take in the specified time range. - Default: 20

        ### Example:
        ```python
        PodsApi(
            workload_id='workload_id_example',
                        pod_id='pod_id_example',
                        metric_type=[runai.PodMetricType()],
                        start='2023-06-06T12:09:18.211Z',
                        end='2023-06-07T12:09:18.211Z',
                        number_of_samples=20
        )
        ```
        """

        # Query params:
        query_params = [
            ("metricType", metric_type),
            ("start", start),
            ("end", end),
            ("numberOfSamples", number_of_samples),
        ]
        resource_path = (
            f"/api/v1/workloads/{workload_id}/pods/{pod_id}/metrics".replace("_", "-")
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_workload_pods(
        self,
        workload_id: str,
        deleted: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        Get workload pods by id.

        ### Parameters:
        ```python
        workload_id: str
        deleted: Optional[bool]
        offset: Optional[int]
        limit: Optional[int]
        search: Optional[str]
        ```
        workload_id: The  Universally Unique Identifier (UUID) of the workload.
        deleted: Return only deleted resources when &#x60;true&#x60;.
        offset: The offset of the first item returned in the collection.
        limit: The maximum number of entries to return. - Default: 50
        search: Filter results by a free text search.

        ### Example:
        ```python
        PodsApi(
            workload_id='workload_id_example',
                        deleted=True,
                        offset=100,
                        limit=50,
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("deleted", deleted),
            ("offset", offset),
            ("limit", limit),
            ("search", search),
        ]
        resource_path = f"/api/v1/workloads/{workload_id}/pods".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def list_pods(
        self,
        deleted: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_order: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_by: Optional[List[str]] = None,
        verbosity: Optional[models.PodVerbosity] = None,
        completed: Optional[str] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        List pods.

        ### Parameters:
        ```python
        deleted: Optional[bool]
        offset: Optional[int]
        limit: Optional[int]
        sort_order: Optional[str]
        sort_by: Optional[str]
        filter_by: Optional[List[str]]
        verbosity: Optional[models.PodVerbosity]
        completed: Optional[str]
        search: Optional[str]
        ```
        deleted: Return only deleted resources when &#x60;true&#x60;.
        offset: The offset of the first item returned in the collection.
        limit: The maximum number of entries to return. - Default: 50
        sort_order: Sort results in descending or ascending order. - Default: asc
        sort_by: Sort results using a parameter.
        filter_by: Filter results using a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contains, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;.
        verbosity: response verbosity level. if full, the response includes workloadName and projectName fields.  - Default: brief
        completed: Return only completed resources when &#39;true&#39;, return only non-completed resources when &#39;false&#39;. By default, or when empty, returns all resources. - Default: &#39;all&#39;
        search: Filter results by a free text search.

        ### Example:
        ```python
        PodsApi(
            deleted=True,
                        offset=100,
                        limit=50,
                        sort_order=asc,
                        sort_by='sort_by_example',
                        filter_by=['[\"nodeName!=some-node-name\"]'],
                        verbosity=brief,
                        completed='all',
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("deleted", deleted),
            ("offset", offset),
            ("limit", limit),
            ("sortOrder", sort_order),
            ("sortBy", sort_by),
            ("filterBy", filter_by),
            ("verbosity", verbosity),
            ("completed", completed),
            ("search", search),
        ]
        resource_path = f"/api/v1/workloads/pods".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )
