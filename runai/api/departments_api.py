from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class DepartmentsApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def count_departments(
        self,
        filter_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        Count departments

        ### Parameters:
        ```python
        filter_by: Optional[List[str]]
        ```
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.

        ### Example:
        ```python
        DepartmentsApi(
            filter_by=['[\"name!=some-name\"]']
        )
        ```
        """

        # Query params:
        query_params = [
            ("filterBy", filter_by),
        ]
        resource_path = f"/api/v1/org_unit/departments/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def create_department(
        self,
        department_creation_request: models.DepartmentCreationRequest,
    ):
        r"""


        ### Description
        Create department

        ### Parameters:
        ```python
        department_creation_request: DepartmentCreationRequest
        ```
        department_creation_request: Department to create.

        ### Example:
        ```python
        DepartmentsApi(
            department_creation_request=runai.DepartmentCreationRequest()
        )
        ```
        """

        # Body params:
        body_params = department_creation_request

        resource_path = f"/api/v1/org_unit/departments".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    @deprecated_message()
    def create_department_0(
        self,
        cluster_id: str,
        department_create_request: models.DepartmentCreateRequest,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Create a new department.

        ### Parameters:
        ```python
        cluster_id: str
        department_create_request: DepartmentCreateRequest
        ```
        cluster_id: The unique uuid identifying the cluster.
        department_create_request: See model DepartmentCreateRequest for more information.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_create_request=runai.DepartmentCreateRequest()
        )
        ```
        """

        # Body params:
        body_params = department_create_request

        resource_path = f"/v1/k8s/clusters/{cluster_id}/departments".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_department(
        self,
        department_id: str,
    ):
        r"""


        ### Description
        Delete department

        ### Parameters:
        ```python
        department_id: str
        ```
        department_id: The id of the department.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1'
        )
        ```
        """

        resource_path = f"/api/v1/org_unit/departments/{department_id}".replace(
            "_", "-"
        )
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    @deprecated_message()
    def delete_department_0(
        self,
        cluster_id: str,
        department_id: int,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Delete a department.

        ### Parameters:
        ```python
        cluster_id: str
        department_id: int
        ```
        cluster_id: The unique uuid identifying the cluster.
        department_id: The unique id identifying the department.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_id=2
        )
        ```
        """

        resource_path = (
            f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}".replace(
                "_", "-"
            )
        )
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_department(
        self,
        department_id: str,
    ):
        r"""


        ### Description
        Get department

        ### Parameters:
        ```python
        department_id: str
        ```
        department_id: The id of the department.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1'
        )
        ```
        """

        resource_path = f"/api/v1/org_unit/departments/{department_id}".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    @deprecated_message()
    def get_department_0(
        self,
        cluster_id: str,
        department_id: int,
        exclude_permissions: Optional[bool] = None,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Get a specific department.

        ### Parameters:
        ```python
        cluster_id: str
        department_id: int
        exclude_permissions: Optional[bool]
        ```
        cluster_id: The Universally Unique Identifier (UUID) of the cluster.
        department_id: The unique id of the department.
        exclude_permissions: backwards compatibility of the &#39;departmentAdmins&#39; field. if &#39;true&#39;, will not set the &#39;departmentAdmins&#39; field in the returned department. if &#39;false&#39;, will set the &#39;departmentAdmins&#39; field in the returned department.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_id=2,
                        exclude_permissions=true
        )
        ```
        """

        # Query params:
        query_params = [
            ("excludePermissions", exclude_permissions),
        ]
        resource_path = (
            f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}".replace(
                "_", "-"
            )
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_department_metrics(
        self,
        department_id: str,
        metric_type: List[models.OrgUnitMetricType],
        start: datetime,
        end: datetime,
        number_of_samples: Optional[int] = None,
        nodepool_name: Optional[str] = None,
    ):
        r"""


        ### Description
        Get department metrics data.

        ### Parameters:
        ```python
        department_id: str
        metric_type: Optional[models.List[OrgUnitMetricType]]
        start: Optional[datetime]
        end: Optional[datetime]
        number_of_samples: Optional[int]
        nodepool_name: Optional[str]
        ```
        department_id: The id of the department.
        metric_type: Specify which data to request.
        start: Start date of time range to fetch data in ISO 8601 timestamp format.
        end: End date of time range to fetch data in ISO 8601 timestamp format.
        number_of_samples: The number of samples to take in the specified time range. - Default: 20
        nodepool_name: Filter using the nodepool.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1',
                        metric_type=[runai.OrgUnitMetricType()],
                        start='2023-06-06T12:09:18.211Z',
                        end='2023-06-07T12:09:18.211Z',
                        number_of_samples=20,
                        nodepool_name='default'
        )
        ```
        """

        # Query params:
        query_params = [
            ("metricType", metric_type),
            ("start", start),
            ("end", end),
            ("numberOfSamples", number_of_samples),
            ("nodepoolName", nodepool_name),
        ]
        resource_path = f"/api/v1/org_unit/departments/{department_id}/metrics".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    @deprecated_message()
    def get_department_metrics_0(
        self,
        cluster_uuid: str,
        department_id: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        number_of_samples: Optional[int] = None,
        nodepool_name: Optional[str] = None,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Get metrics for a specific department.

        ### Parameters:
        ```python
        cluster_uuid: str
        department_id: str
        start: Optional[datetime]
        end: Optional[datetime]
        number_of_samples: Optional[int]
        nodepool_name: Optional[str]
        ```
        cluster_uuid: The Universally Unique Identifier (UUID) of the cluster.
        department_id: The id of the department.
        start: Start of time range to fetch data from in UTC format.
        end: End of time range to fetch data from in UTC format.
        number_of_samples: The number of samples to take in the specified time range. - Default: 20
        nodepool_name: Filter by unique nodepool name.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_uuid='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_id='1',
                        start='2013-10-20T19:20:30+01:00',
                        end='2013-10-20T19:20:30+01:00',
                        number_of_samples=20,
                        nodepool_name='default'
        )
        ```
        """

        # Query params:
        query_params = [
            ("start", start),
            ("end", end),
            ("numberOfSamples", number_of_samples),
            ("nodepoolName", nodepool_name),
        ]
        resource_path = f"/v1/k8s/clusters/{cluster_uuid}/departments/{department_id}/metrics".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_departments(
        self,
        filter_by: Optional[List[str]] = None,
        sort_by: Optional[models.DepartmentFilterSortFields] = None,
        verbosity: Optional[models.Verbosity] = None,
        sort_order: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        r"""


        ### Description
        Get departments

        ### Parameters:
        ```python
        filter_by: Optional[List[str]]
        sort_by: Optional[models.DepartmentFilterSortFields]
        verbosity: Optional[models.Verbosity]
        sort_order: Optional[str]
        offset: Optional[int]
        limit: Optional[int]
        ```
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.
        sort_by: Sort results by a parameters.
        verbosity: Departments verbosity. If it is set to \&quot;verbose\&quot;, status will be returned. If it is not defined or set to \&quot;brief\&quot; only unit specific data will be returned.
        sort_order: Sort results in descending or ascending order. - Default: asc
        offset: The offset of the first item returned in the collection.
        limit: The maximum number of entries to return. - Default: 50

        ### Example:
        ```python
        DepartmentsApi(
            filter_by=['[\"name!=some-name\"]'],
                        sort_by=runai.DepartmentFilterSortFields(),
                        verbosity=runai.Verbosity(),
                        sort_order=asc,
                        offset=100,
                        limit=50
        )
        ```
        """

        # Query params:
        query_params = [
            ("filterBy", filter_by),
            ("sortBy", sort_by),
            ("verbosity", verbosity),
            ("sortOrder", sort_order),
            ("offset", offset),
            ("limit", limit),
        ]
        resource_path = f"/api/v1/org_unit/departments".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    @deprecated_message()
    def get_departments_0(
        self,
        cluster_id: str,
        exclude_permissions: Optional[bool] = None,
        memory_unit_mb: Optional[bool] = None,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        List all departments.

        ### Parameters:
        ```python
        cluster_id: str
        exclude_permissions: Optional[bool]
        memory_unit_mb: Optional[bool]
        ```
        cluster_id: The Universally Unique Identifier (UUID) of the cluster.
        exclude_permissions: Backward compatibility of the &#x60;departmentAdmins&#x60; field. If &#x60;true&#x60;, the &#x60;departmentAdmins&#x60; field in the returned departments is not set. If &#x60;false&#x60;, the &#x60;departmentAdmins&#x60; is set in the returned departments.
        memory_unit_mb: Memory returned in MB. When set to &#x60;false&#x60; (default) memory will be returned in MiB.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        exclude_permissions=true,
                        memory_unit_mb=true
        )
        ```
        """

        # Query params:
        query_params = [
            ("excludePermissions", exclude_permissions),
            ("memoryUnitMb", memory_unit_mb),
        ]
        resource_path = f"/v1/k8s/clusters/{cluster_id}/departments".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    @deprecated_message()
    def get_departments_metrics(
        self,
        cluster_uuid: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        number_of_samples: Optional[int] = None,
        nodepool_name: Optional[str] = None,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Get metrics for all departments.

        ### Parameters:
        ```python
        cluster_uuid: str
        start: Optional[datetime]
        end: Optional[datetime]
        number_of_samples: Optional[int]
        nodepool_name: Optional[str]
        ```
        cluster_uuid: The Universally Unique Identifier (UUID) of the cluster.
        start: Start of time range to fetch data from in UTC format.
        end: End of time range to fetch data from in UTC format.
        number_of_samples: The number of samples to take in the specified time range. - Default: 20
        nodepool_name: Filter by unique nodepool name.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_uuid='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        start='2013-10-20T19:20:30+01:00',
                        end='2013-10-20T19:20:30+01:00',
                        number_of_samples=20,
                        nodepool_name='default'
        )
        ```
        """

        # Query params:
        query_params = [
            ("start", start),
            ("end", end),
            ("numberOfSamples", number_of_samples),
            ("nodepoolName", nodepool_name),
        ]
        resource_path = f"/v1/k8s/clusters/{cluster_uuid}/departments/metrics".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_departments_telemetry(
        self,
        telemetry_type: models.OrgUnitTelemetryType,
        cluster_id: Optional[str] = None,
        nodepool_name: Optional[str] = None,
        department_id: Optional[str] = None,
        group_by: Optional[List[str]] = None,
    ):
        r"""


        ### Description
        Get departments telemetry

        ### Parameters:
        ```python
        telemetry_type: Optional[models.OrgUnitTelemetryType]
        cluster_id: Optional[str]
        nodepool_name: Optional[str]
        department_id: Optional[str]
        group_by: Optional[List[str]]
        ```
        telemetry_type: specifies what data to request
        cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        nodepool_name: Filter using the nodepool.
        department_id: Filter using the department id.
        group_by: department fields to group the data by

        ### Example:
        ```python
        DepartmentsApi(
            telemetry_type=runai.OrgUnitTelemetryType(),
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
        resource_path = f"/api/v1/org_unit/departments/telemetry".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def patch_department_resources(
        self,
        department_id: str,
        resources_nullable: List[models.ResourcesNullable],
    ):
        r"""


        ### Description
        Patch department resources

        ### Parameters:
        ```python
        department_id: str
        resources_nullable: List[ResourcesNullable]
        ```
        department_id: The id of the department.
        resources_nullable: Department resources to update.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1',
                        resources_nullable=[runai.ResourcesNullable()]
        )
        ```
        """

        # Body params:
        body_params = resources_nullable

        resource_path = (
            f"/api/v1/org_unit/departments/{department_id}/resources".replace("_", "-")
        )
        method = "PATCH"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def update_department(
        self,
        department_id: str,
        department_update_request: models.DepartmentUpdateRequest,
    ):
        r"""


        ### Description
        Update department

        ### Parameters:
        ```python
        department_id: str
        department_update_request: DepartmentUpdateRequest
        ```
        department_id: The id of the department.
        department_update_request: Department to update.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1',
                        department_update_request=runai.DepartmentUpdateRequest()
        )
        ```
        """

        # Body params:
        body_params = department_update_request

        resource_path = f"/api/v1/org_unit/departments/{department_id}".replace(
            "_", "-"
        )
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    @deprecated_message()
    def update_department_0(
        self,
        cluster_id: str,
        department_id: int,
        department_update_request1: models.DepartmentUpdateRequest1,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Update a department.

        ### Parameters:
        ```python
        cluster_id: str
        department_id: int
        department_update_request1: DepartmentUpdateRequest1
        ```
        cluster_id: The unique uuid identifying the cluster.
        department_id: The unique id identifying the department.
        department_update_request1: See model DepartmentUpdateRequest1 for more information.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_id=2,
                        department_update_request1=runai.DepartmentUpdateRequest1()
        )
        ```
        """

        # Body params:
        body_params = department_update_request1

        resource_path = (
            f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}".replace(
                "_", "-"
            )
        )
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    @deprecated_message()
    def update_department_admins(
        self,
        cluster_id: str,
        department_id: int,
        department_access_control: models.DepartmentAccessControl,
    ):
        r"""
        ## Deprecated endpoint, consider alternative method

        ### Description
        Set the department admins.

        ### Parameters:
        ```python
        cluster_id: str
        department_id: int
        department_access_control: DepartmentAccessControl
        ```
        cluster_id: The unique uuid identifying the cluster.
        department_id: The unique id identifying the department.
        department_access_control: See model DepartmentAccessControl for more information.

        ### Example:
        ```python
        DepartmentsApi(
            cluster_id='9f55255e-11ed-47c7-acef-fc4054768dbc',
                        department_id=2,
                        department_access_control=runai.DepartmentAccessControl()
        )
        ```
        """

        # Body params:
        body_params = department_access_control

        resource_path = f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}/access_control".replace(
            "_", "-"
        )
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def update_department_resources(
        self,
        department_id: str,
        resources_nullable: List[models.ResourcesNullable],
    ):
        r"""


        ### Description
        Update department resources

        ### Parameters:
        ```python
        department_id: str
        resources_nullable: List[ResourcesNullable]
        ```
        department_id: The id of the department.
        resources_nullable: Department resources to update.

        ### Example:
        ```python
        DepartmentsApi(
            department_id='1',
                        resources_nullable=[runai.ResourcesNullable()]
        )
        ```
        """

        # Body params:
        body_params = resources_nullable

        resource_path = (
            f"/api/v1/org_unit/departments/{department_id}/resources".replace("_", "-")
        )
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
