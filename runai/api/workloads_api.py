from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class WorkloadsApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def count_workloads(
        self,
        deleted: Optional[bool] = None,
        filter_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        Count workloads.

        ### Parameters:
        ```python
        deleted: Optional[bool]
        filter_by: Optional[List[str]]
        ```
        deleted: Return only deleted resources when &#x60;true&#x60;.
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contain, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;.

        ### Example:
        ```python
        WorkloadsApi(
            deleted=True,
                        filter_by=['[\"name!=some-workload-name\",\"allocatedGPU>=2\",\"createdAt>=2021-01-01T00:00:00Z\"]']
        )
        ```
        """

        # Query params:
        query_params = [
            ("deleted", deleted),
            ("filterBy", filter_by),
        ]
        resource_path = f"/api/v1/workloads/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_workload(
        self,
        workload_id: str,
    ):
        r"""


        ### Description
        Get a workload.

        ### Parameters:
        ```python
        workload_id: str
        ```
        workload_id: The  Universally Unique Identifier (UUID) of the workload.

        ### Example:
        ```python
        WorkloadsApi(
            workload_id='workload_id_example'
        )
        ```
        """

        resource_path = f"/api/v1/workloads/{workload_id}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_workload_metrics(
        self,
        workload_id: str,
        metric_type: List[models.WorkloadMetricType],
        start: datetime,
        end: datetime,
        number_of_samples: Optional[int] = None,
    ):
        r"""


        ### Description
        Get workload metrics data. [Experimental]

        ### Parameters:
        ```python
        workload_id: str
        metric_type: Optional[models.List[WorkloadMetricType]]
        start: Optional[datetime]
        end: Optional[datetime]
        number_of_samples: Optional[int]
        ```
        workload_id: The  Universally Unique Identifier (UUID) of the workload.
        metric_type: Specify which data to request.
        start: Start date of time range to fetch data in ISO 8601 timestamp format.
        end: End date of time range to fetch data in ISO 8601 timestamp format.
        number_of_samples: The number of samples to take in the specified time range. - Default: 20

        ### Example:
        ```python
        WorkloadsApi(
            workload_id='workload_id_example',
                        metric_type=[runai.WorkloadMetricType()],
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
        resource_path = f"/api/v1/workloads/{workload_id}/metrics".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_workloads(
        self,
        deleted: Optional[bool] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_order: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        List workloads.

        ### Parameters:
        ```python
        deleted: Optional[bool]
        offset: Optional[int]
        limit: Optional[int]
        sort_order: Optional[str]
        sort_by: Optional[str]
        filter_by: Optional[List[str]]
        ```
        deleted: Return only deleted resources when &#x60;true&#x60;.
        offset: The offset of the first item returned in the collection.
        limit: The maximum number of entries to return. - Default: 50
        sort_order: Sort results in descending or ascending order. - Default: asc
        sort_by: Sort results by a parameter.
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x60;&#x3D;&#x3D;&#x60; Equals, &#x60;!&#x3D;&#x60; Not equals, &#x60;&lt;&#x3D;&#x60; Less than or equal, &#x60;&gt;&#x3D;&#x60; Greater than or equal, &#x60;&#x3D;@&#x60; contains, &#x60;!@&#x60; Does not contain, &#x60;&#x3D;^&#x60; Starts with and &#x60;&#x3D;$&#x60; Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x60;&#x3D;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x3D;&#x60; and &#x60;&gt;&#x3D;&#x60;.

        ### Example:
        ```python
        WorkloadsApi(
            deleted=True,
                        offset=100,
                        limit=50,
                        sort_order=asc,
                        sort_by='sort_by_example',
                        filter_by=['[\"name!=some-workload-name\",\"allocatedGPU>=2\",\"createdAt>=2021-01-01T00:00:00Z\"]']
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
        ]
        resource_path = f"/api/v1/workloads".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_workloads_telemetry(
        self,
        telemetry_type: models.WorkloadTelemetryType,
        cluster_id: Optional[str] = None,
        nodepool_name: Optional[str] = None,
        department_id: Optional[str] = None,
        group_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        Get the workloads telemetry. [Experimental]

        ### Parameters:
        ```python
        telemetry_type: Optional[models.WorkloadTelemetryType]
        cluster_id: Optional[str]
        nodepool_name: Optional[str]
        department_id: Optional[str]
        group_by: Optional[List[str]]
        ```
        telemetry_type: Specifies the telemetry type.
        cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        nodepool_name: Filter using the nodepool.
        department_id: Filter using the department id.
        group_by: Group workloads by field.

        ### Example:
        ```python
        WorkloadsApi(
            telemetry_type=runai.WorkloadTelemetryType(),
                        cluster_id='d73a738f-fab3-430a-8fa3-5241493d7128',
                        nodepool_name='default',
                        department_id='1',
                        group_by=['group_by_example']
        )
        ```
        """

        # Query params:
        query_params = [
            ("clusterId", cluster_id),
            ("nodepoolName", nodepool_name),
            ("departmentId", department_id),
            ("groupBy", group_by),
            ("telemetryType", telemetry_type),
        ]
        resource_path = f"/api/v1/workloads/telemetry".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )
