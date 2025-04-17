# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class AuditLog(BaseModel):
    """
    Pydantic class model representing AuditLog.

    Parameters:
        ```python
        id: str
        timestamp: datetime
        tenant_id: str
        subject: str
        subject_type: str
        source_ip: str
        action: str
        http_method: str
        url: str
        entity_type: str
        entity_name: str
        entity_id: str
        result: str
        http_status_code: int
        cluster_name: str
        cluster_id: str
        request_id: str
        metadata: Dict[str, str]
        ```
        id: See model str for more information.
        timestamp: See model datetime for more information.
        tenant_id: the ID of the tenant
        subject: the user/app which triggered this API
        subject_type: See model str for more information. - Default: &#39;User&#39;
        source_ip: See model str for more information.
        action: See model str for more information.
        http_method: See model str for more information.
        url: See model str for more information.
        entity_type: See model str for more information.
        entity_name: See model str for more information.
        entity_id: See model str for more information.
        result: See model str for more information.
        http_status_code: See model int for more information.
        cluster_name: See model str for more information.
        cluster_id: See model str for more information.
        request_id: See model str for more information.
        metadata: See model Dict[str, str] for more information.
    Example:
        ```python
        AuditLog(
            id='',
                        timestamp='2022-01-01T03:49:52.531Z',
                        tenant_id='12345',
                        subject='researcher@run.ai',
                        subject_type='User',
                        source_ip='',
                        action='create',
                        http_method='GET',
                        url='',
                        entity_type='project',
                        entity_name='project-1',
                        entity_id='1234',
                        result='Succeeded',
                        http_status_code=200,
                        cluster_name='my favorite cluster',
                        cluster_id='',
                        request_id='bb0c4742-e52f-4d5e-bfee-2c4ff57c339c',
                        metadata={
                    'key' : ''
                    }
        )
        ```
    """  # noqa: E501

    id: StrictStr
    timestamp: datetime
    tenant_id: StrictStr = Field(description="the ID of the tenant")
    subject: StrictStr = Field(description="the user/app which triggered this API")
    subject_type: StrictStr
    source_ip: StrictStr
    action: StrictStr
    http_method: StrictStr
    url: StrictStr
    entity_type: StrictStr
    entity_name: StrictStr
    entity_id: StrictStr
    result: StrictStr
    http_status_code: StrictInt
    cluster_name: Optional[StrictStr] = None
    cluster_id: Optional[StrictStr] = None
    request_id: Optional[StrictStr] = None
    metadata: Dict[str, StrictStr]
    __properties: ClassVar[List[str]] = [
        "id",
        "timestamp",
        "tenant_id",
        "subject",
        "subject_type",
        "source_ip",
        "action",
        "http_method",
        "url",
        "entity_type",
        "entity_name",
        "entity_id",
        "result",
        "http_status_code",
        "cluster_name",
        "cluster_id",
        "request_id",
        "metadata",
    ]

    @field_validator("subject_type")
    def subject_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["User", "App"]):
            raise ValueError("must be one of enum values ('User', 'App')")
        return value

    @field_validator("action")
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            ["create", "update", "delete", "sign-in", "sign-out", "reset-password"]
        ):
            raise ValueError(
                "must be one of enum values ('create', 'update', 'delete', 'sign-in', 'sign-out', 'reset-password')"
            )
        return value

    @field_validator("http_method")
    def http_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["GET", "POST", "PUT", "PATCH", "DELETE", "CREATE"]):
            raise ValueError(
                "must be one of enum values ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'CREATE')"
            )
        return value

    @field_validator("result")
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["Succeeded", "Failed"]):
            raise ValueError("must be one of enum values ('Succeeded', 'Failed')")
        return value

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
        """Create an instance of AuditLog from a JSON string"""
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
        """Create an instance of AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "timestamp": obj.get("timestamp"),
                "tenant_id": obj.get("tenant_id"),
                "subject": obj.get("subject"),
                "subject_type": (
                    obj.get("subject_type")
                    if obj.get("subject_type") is not None
                    else "User"
                ),
                "source_ip": obj.get("source_ip"),
                "action": obj.get("action"),
                "http_method": obj.get("http_method"),
                "url": obj.get("url"),
                "entity_type": obj.get("entity_type"),
                "entity_name": obj.get("entity_name"),
                "entity_id": obj.get("entity_id"),
                "result": obj.get("result"),
                "http_status_code": obj.get("http_status_code"),
                "cluster_name": obj.get("cluster_name"),
                "cluster_id": obj.get("cluster_id"),
                "request_id": obj.get("request_id"),
                "metadata": obj.get("metadata"),
            }
        )
        return _obj
