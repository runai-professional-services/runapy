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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class Application(BaseModel):
    """
    Pydantic class model representing Application.

    Parameters:
        ```python
        name: str
        created_by: str
        created_at: Optional[datetime]
        updated_at: Optional[datetime]
        enabled: bool
        tenant_id: str
        last_login: Optional[datetime]
        id: str
        client_id: str
        ```
        name: See model str for more information.
        created_by: See model str for more information.
        created_at: See model datetime for more information.
        updated_at: See model datetime for more information.
        enabled: See model bool for more information.
        tenant_id: See model str for more information.
        last_login: See model datetime for more information.
        id: See model str for more information.
        client_id: See model str for more information.
    Example:
        ```python
        Application(
            name='',
                        created_by='',
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        enabled=True,
                        tenant_id='',
                        last_login=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        id='',
                        client_id=''
        )
        ```
    """  # noqa: E501

    name: StrictStr
    created_by: StrictStr = Field(alias="createdBy")
    created_at: Optional[datetime] = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(alias="updatedAt")
    enabled: StrictBool
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    last_login: Optional[datetime] = Field(alias="lastLogin")
    id: StrictStr
    client_id: StrictStr = Field(alias="clientId")
    __properties: ClassVar[List[str]] = [
        "name",
        "createdBy",
        "createdAt",
        "updatedAt",
        "enabled",
        "tenantId",
        "lastLogin",
        "id",
        "clientId",
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
        """Create an instance of Application from a JSON string"""
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
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict["createdAt"] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict["updatedAt"] = None

        # set to None if last_login (nullable) is None
        # and model_fields_set contains the field
        if self.last_login is None and "last_login" in self.model_fields_set:
            _dict["lastLogin"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Application from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "createdBy": obj.get("createdBy"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
                "enabled": obj.get("enabled"),
                "tenantId": obj.get("tenantId"),
                "lastLogin": obj.get("lastLogin"),
                "id": obj.get("id"),
                "clientId": obj.get("clientId"),
            }
        )
        return _obj
