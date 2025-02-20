# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class AuditLogRecord(BaseModel):
    """
    Pydantic class model representing AuditLogRecord.

    Parameters:
        ```python
        id: int
        cluster_uuid: str
        tenant_id: int
        happened_at: datetime
        action: str
        version: str
        entity_id: str
        entity_type: str
        entity_name: str
        source_type: str
        source_id: str
        source_name: str
        error: str
        context: object
        body: object
        ```
        id: The unique id of the audit log.
        cluster_uuid: The id of the cluster.
        tenant_id: The id of the tenant.
        happened_at: The date and time in which the event happened.
        action: The action that was performed by the user.
        version: The version of the audit log record.
        entity_id: The id of the action related entity.
        entity_type: The type of the action related entity.
        entity_name: The name of the action related entity.
        source_type: The type of the source of the action.
        source_id: The id of the source of the action.
        source_name: The name of the source of the action.
        error: In case of a failed action, the corresponding error
        context: The context of the action.
        body: The body of the action http request.
    Example:
        ```python
        AuditLogRecord(
            id=12,
                        cluster_uuid='71f69d83-ba66-4822-adf5-55ce55efd210',
                        tenant_id=1001,
                        happened_at='2022-06-08T11:28:24.131Z',
                        action='Create',
                        version='1',
                        entity_id='51',
                        entity_type='Department',
                        entity_name='MyDepartment123',
                        source_type='User',
                        source_id='96a4382e-afa5-4604-9eb1-c3071aa021fc',
                        source_name='test@run.ai',
                        error='{"status":404,"description":"Cluster with uuid '19519f4b-e3a5-45c7-9451-0def7b931546' does not exist","errorType":"BackendError"}',
                        context={"user_agent":"Thunder Client (https://www.thunderclient.com)"},
                        body={"name":"test1","deservedGpus":1,"allowOverQuota":false,"maxAllowedGpus":1}
        )
        ```
    """  # noqa: E501

    id: Optional[StrictInt] = Field(
        default=None, description="The unique id of the audit log."
    )
    cluster_uuid: Optional[StrictStr] = Field(
        default=None, description="The id of the cluster.", alias="clusterUuid"
    )
    tenant_id: Optional[StrictInt] = Field(
        default=None, description="The id of the tenant.", alias="tenantId"
    )
    happened_at: Optional[datetime] = Field(
        default=None,
        description="The date and time in which the event happened.",
        alias="happenedAt",
    )
    action: Optional[StrictStr] = Field(
        default=None, description="The action that was performed by the user."
    )
    version: Optional[StrictStr] = Field(
        default=None, description="The version of the audit log record."
    )
    entity_id: Optional[StrictStr] = Field(
        default=None,
        description="The id of the action related entity.",
        alias="entityId",
    )
    entity_type: Optional[StrictStr] = Field(
        default=None,
        description="The type of the action related entity.",
        alias="entityType",
    )
    entity_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the action related entity.",
        alias="entityName",
    )
    source_type: Optional[StrictStr] = Field(
        default=None,
        description="The type of the source of the action.",
        alias="sourceType",
    )
    source_id: Optional[StrictStr] = Field(
        default=None,
        description="The id of the source of the action.",
        alias="sourceId",
    )
    source_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the source of the action.",
        alias="sourceName",
    )
    error: Optional[StrictStr] = Field(
        default=None, description="In case of a failed action, the corresponding error"
    )
    context: Optional[Dict[str, Any]] = Field(
        default=None, description="The context of the action."
    )
    body: Optional[Dict[str, Any]] = Field(
        default=None, description="The body of the action http request."
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "clusterUuid",
        "tenantId",
        "happenedAt",
        "action",
        "version",
        "entityId",
        "entityType",
        "entityName",
        "sourceType",
        "sourceId",
        "sourceName",
        "error",
        "context",
        "body",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuditLogRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditLogRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "clusterUuid": obj.get("clusterUuid"),
                "tenantId": obj.get("tenantId"),
                "happenedAt": obj.get("happenedAt"),
                "action": obj.get("action"),
                "version": obj.get("version"),
                "entityId": obj.get("entityId"),
                "entityType": obj.get("entityType"),
                "entityName": obj.get("entityName"),
                "sourceType": obj.get("sourceType"),
                "sourceId": obj.get("sourceId"),
                "sourceName": obj.get("sourceName"),
                "error": obj.get("error"),
                "context": obj.get("context"),
                "body": obj.get("body"),
            }
        )
        return _obj
