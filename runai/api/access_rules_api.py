from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class AccessRulesApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def access_rules_batch(
        self,
        access_rules_batch: Optional[models.AccessRulesBatch] = None,
    ):
        r"""


        ### Description
        Access Rules batch delete operation.

        ### Parameters:
        ```python
        access_rules_batch: AccessRulesBatch
        ```
        access_rules_batch: See model AccessRulesBatch for more information.

        ### Example:
        ```python
        AccessRulesApi(
            access_rules_batch=runai.AccessRulesBatch()
        )
        ```
        """

        # Body params:
        body_params = access_rules_batch

        resource_path = f"/api/v1/authorization/access_rules/batch".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def count_access_rules(
        self,
        include_deleted: Optional[bool] = None,
        filter_by: Optional[List[str]] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        Count access rules.

        ### Parameters:
        ```python
        include_deleted: Optional[bool]
        filter_by: Optional[List[str]]
        search: Optional[str]
        ```
        include_deleted: True to include deleted objects in the result. - Default: False
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.
        search: Filter results by a free text search.

        ### Example:
        ```python
        AccessRulesApi(
            include_deleted=False,
                        filter_by=['[\"name!=some-access-rule-name\",\"createdAt>=2023-01-01T00:00:00Z\"]'],
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("includeDeleted", include_deleted),
            ("filterBy", filter_by),
            ("search", search),
        ]
        resource_path = f"/api/v1/authorization/access_rules/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def create_access_rule(
        self,
        access_rule_creation_fields: models.AccessRuleCreationFields,
    ):
        r"""


        ### Description
        Create an access rule.

        ### Parameters:
        ```python
        access_rule_creation_fields: AccessRuleCreationFields
        ```
        access_rule_creation_fields: The access rule to create.

        ### Example:
        ```python
        AccessRulesApi(
            access_rule_creation_fields=runai.AccessRuleCreationFields()
        )
        ```
        """

        # Body params:
        body_params = access_rule_creation_fields

        resource_path = f"/api/v1/authorization/access_rules".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_access_rule(
        self,
        access_rule_id: int,
    ):
        r"""


        ### Description
        Delete an access rule.

        ### Parameters:
        ```python
        access_rule_id: int
        ```
        access_rule_id: The id of the access rule to retrieve

        ### Example:
        ```python
        AccessRulesApi(
            access_rule_id=32
        )
        ```
        """

        resource_path = f"/api/v1/authorization/access_rules/{access_rule_id}".replace(
            "_", "-"
        )
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_access_rule(
        self,
        access_rule_id: int,
    ):
        r"""


        ### Description
        Get an access rule.

        ### Parameters:
        ```python
        access_rule_id: int
        ```
        access_rule_id: The id of the access rule to retrieve

        ### Example:
        ```python
        AccessRulesApi(
            access_rule_id=32
        )
        ```
        """

        resource_path = f"/api/v1/authorization/access_rules/{access_rule_id}".replace(
            "_", "-"
        )
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_access_rules(
        self,
        subject_type: Optional[str] = None,
        subject_id_filter: Optional[str] = None,
        subject_ids: Optional[List[str]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        last_updated: Optional[str] = None,
        include_deleted: Optional[bool] = None,
        cluster_id: Optional[str] = None,
        scope_type: Optional[str] = None,
        scope_id: Optional[str] = None,
        role_id: Optional[int] = None,
        sort_order: Optional[str] = None,
        sort_by: Optional[models.AccessRulesSortFilterFields] = None,
        filter_by: Optional[List[str]] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        List the access rules.

        ### Parameters:
        ```python
        subject_type: Optional[str]
        subject_id_filter: Optional[str]
        subject_ids: Optional[List[str]]
        limit: Optional[int]
        offset: Optional[int]
        last_updated: Optional[str]
        include_deleted: Optional[bool]
        cluster_id: Optional[str]
        scope_type: Optional[str]
        scope_id: Optional[str]
        role_id: Optional[int]
        sort_order: Optional[str]
        sort_by: Optional[models.AccessRulesSortFilterFields]
        filter_by: Optional[List[str]]
        search: Optional[str]
        ```
        subject_type: The type of resource we want to filter by.
        subject_id_filter: Part of the subject id that we want to filter by.
        subject_ids: The ids of the subjects to filter the response for.
        limit: The maximum number of entries to return. - Default: 50
        offset: The offset of the first item returned in the collection.
        last_updated: Filter by last update time.
        include_deleted: True to include deleted objects in the result. - Default: False
        cluster_id: Filter using the Universally Unique Identifier (UUID) of the cluster.
        scope_type: The type of resource we want to filter by.
        scope_id: The scope resource id that we want to filter by.
        role_id: The role id we want to filter by.
        sort_order: Sort results in descending or ascending order. - Default: asc
        sort_by: Sort results by a parameter.
        filter_by: Filter results by a parameter. Use the format field-name operator value. Operators are &#x3D;&#x3D; Equals, !&#x3D; Not equals, &lt;&#x3D; Less than or equal, &gt;&#x3D; Greater than or equal, &#x3D;@ contains, !@ Does not contains, &#x3D;^ Starts with and &#x3D;$ Ends with. Dates are in ISO 8601 timestamp format and available for operators &#x3D;&#x3D;, !&#x3D;, &lt;&#x3D; and &gt;&#x3D;.
        search: Filter results by a free text search.

        ### Example:
        ```python
        AccessRulesApi(
            subject_type='user',
                        subject_id_filter='some.user',
                        subject_ids=['subject_ids_example'],
                        limit=50,
                        offset=100,
                        last_updated='2021-12-14T16:04:15.099Z',
                        include_deleted=False,
                        cluster_id='d73a738f-fab3-430a-8fa3-5241493d7128',
                        scope_type='project',
                        scope_id='2',
                        role_id=56,
                        sort_order=asc,
                        sort_by=runai.AccessRulesSortFilterFields(),
                        filter_by=['[\"name!=some-access-rule-name\",\"createdAt>=2023-01-01T00:00:00Z\"]'],
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("subjectType", subject_type),
            ("subjectIdFilter", subject_id_filter),
            ("subjectIds", subject_ids),
            ("limit", limit),
            ("offset", offset),
            ("lastUpdated", last_updated),
            ("includeDeleted", include_deleted),
            ("clusterId", cluster_id),
            ("scopeType", scope_type),
            ("scopeId", scope_id),
            ("roleId", role_id),
            ("sortOrder", sort_order),
            ("sortBy", sort_by),
            ("filterBy", filter_by),
            ("search", search),
        ]
        resource_path = f"/api/v1/authorization/access_rules".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )
