# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
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
from runai.models.scope_type import ScopeType
from runai.models.subject_type import SubjectType
from typing import Optional, Set
from typing_extensions import Self


class AccessRule(BaseModel):
    """
    Pydantic class model representing AccessRule.

    Parameters:
        ```python
        subject_id: str
        subject_type: SubjectType
        role_id: int
        scope_id: str
        scope_type: ScopeType
        cluster_id: str
        role_name: str
        scope_name: str
        id: int
        created_at: datetime
        updated_at: datetime
        deleted_at: Optional[datetime]
        tenant_id: int
        created_by: str
        ```
        subject_id: See model str for more information.
        subject_type: See model SubjectType for more information.
        role_id: See model int for more information.
        scope_id: See model str for more information.
        scope_type: See model ScopeType for more information.
        cluster_id: The id of the cluster.
        role_name: See model str for more information.
        scope_name: See model str for more information.
        id: See model int for more information.
        created_at: See model datetime for more information.
        updated_at: See model datetime for more information.
        deleted_at: See model datetime for more information.
        tenant_id: The id of the tenant.
        created_by: See model str for more information.
    Example:
        ```python
        AccessRule(
            subject_id='user@run.ai',
                        subject_type='user',
                        role_id=53142648,
                        scope_id='a418ed33-9399-48c0-a890-122cadd13bfd',
                        scope_type='system',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        role_name='admin',
                        scope_name='tenant-x',
                        id=32,
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        deleted_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        tenant_id=1001,
                        created_by='user@run.ai'
        )
        ```
    """  # noqa: E501

    subject_id: StrictStr = Field(alias="subjectId")
    subject_type: SubjectType = Field(alias="subjectType")
    role_id: StrictInt = Field(alias="roleId")
    scope_id: StrictStr = Field(alias="scopeId")
    scope_type: ScopeType = Field(alias="scopeType")
    cluster_id: Optional[StrictStr] = Field(
        default=None, description="The id of the cluster.", alias="clusterId"
    )
    role_name: StrictStr = Field(alias="roleName")
    scope_name: StrictStr = Field(alias="scopeName")
    id: StrictInt
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")
    tenant_id: StrictInt = Field(description="The id of the tenant.", alias="tenantId")
    created_by: StrictStr = Field(alias="createdBy")
    __properties: ClassVar[List[str]] = [
        "subjectId",
        "subjectType",
        "roleId",
        "scopeId",
        "scopeType",
        "clusterId",
        "roleName",
        "scopeName",
        "id",
        "createdAt",
        "updatedAt",
        "deletedAt",
        "tenantId",
        "createdBy",
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
        """Create an instance of AccessRule from a JSON string"""
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
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict["deletedAt"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "subjectId": obj.get("subjectId"),
                "subjectType": obj.get("subjectType"),
                "roleId": obj.get("roleId"),
                "scopeId": obj.get("scopeId"),
                "scopeType": obj.get("scopeType"),
                "clusterId": obj.get("clusterId"),
                "roleName": obj.get("roleName"),
                "scopeName": obj.get("scopeName"),
                "id": obj.get("id"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
                "deletedAt": obj.get("deletedAt"),
                "tenantId": obj.get("tenantId"),
                "createdBy": obj.get("createdBy"),
            }
        )
        return _obj
