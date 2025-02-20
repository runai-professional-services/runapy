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
from runai.models.permission import Permission
from typing import Optional, Set
from typing_extensions import Self


class Role1(BaseModel):
    """
    Pydantic class model representing Role1.

    Parameters:
        ```python
        name: str
        description: str
        permissions: List[Permission]
        id: int
        created_at: datetime
        updated_at: datetime
        deleted_at: Optional[datetime]
        tenant_id: int
        created_by: str
        ```
        name: See model str for more information.
        description: See model str for more information.
        permissions: See model List[Permission] for more information.
        id: See model int for more information.
        created_at: See model datetime for more information.
        updated_at: See model datetime for more information.
        deleted_at: See model datetime for more information.
        tenant_id: The id of the tenant.
        created_by: See model str for more information.
    Example:
        ```python
        Role1(
            name='admin',
                        description='can manage all resources',
                        permissions=[
                    runai.models.permission.Permission(
                        resource_type = 'department',
                        display_name = 'Projects',
                        group_id = 'organization',
                        actions = [
                            'create'
                            ], )
                    ],
                        id=32,
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        deleted_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        tenant_id=1001,
                        created_by='user@run.ai'
        )
        ```
    """  # noqa: E501

    name: StrictStr
    description: StrictStr
    permissions: List[Permission]
    id: StrictInt
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")
    tenant_id: Optional[StrictInt] = Field(
        default=None, description="The id of the tenant.", alias="tenantId"
    )
    created_by: StrictStr = Field(alias="createdBy")
    __properties: ClassVar[List[str]] = [
        "name",
        "description",
        "permissions",
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
        """Create an instance of Role1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict["permissions"] = _items
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict["deletedAt"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Role1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "permissions": (
                    [Permission.from_dict(_item) for _item in obj["permissions"]]
                    if obj.get("permissions") is not None
                    else None
                ),
                "id": obj.get("id"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
                "deletedAt": obj.get("deletedAt"),
                "tenantId": obj.get("tenantId"),
                "createdBy": obj.get("createdBy"),
            }
        )
        return _obj
