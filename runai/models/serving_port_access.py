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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.serving_port_access_authorization_type_enum import (
    ServingPortAccessAuthorizationTypeEnum,
)
from typing import Optional, Set
from typing_extensions import Self


class ServingPortAccess(BaseModel):
    """
    Pydantic class model representing ServingPortAccess.

    Parameters:
        ```python
        authorization_type: Optional[ServingPortAccessAuthorizationTypeEnum]
        authorized_users: Optional[List[str]]
        authorized_groups: Optional[List[str]]
        cluster_local_access_only: Optional[bool]
        ```
        authorization_type: See model ServingPortAccessAuthorizationTypeEnum for more information.
        authorized_users: List of users that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        authorized_groups: List of groups that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        cluster_local_access_only: Configure the serving port URL to be available only on the cluster-local network, and not externally. Defaults to false
    Example:
        ```python
        ServingPortAccess(
            authorization_type='public',
                        authorized_users=["user.a@example.com","user.b@example.com"],
                        authorized_groups=["group-a","group-b"],
                        cluster_local_access_only=True
        )
        ```
    """  # noqa: E501

    authorization_type: Optional[ServingPortAccessAuthorizationTypeEnum] = Field(
        default=None, alias="authorizationType"
    )
    authorized_users: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of users that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.",
        alias="authorizedUsers",
    )
    authorized_groups: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of groups that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.",
        alias="authorizedGroups",
    )
    cluster_local_access_only: Optional[StrictBool] = Field(
        default=None,
        description="Configure the serving port URL to be available only on the cluster-local network, and not externally. Defaults to false",
        alias="clusterLocalAccessOnly",
    )
    __properties: ClassVar[List[str]] = [
        "authorizationType",
        "authorizedUsers",
        "authorizedGroups",
        "clusterLocalAccessOnly",
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
        """Create an instance of ServingPortAccess from a JSON string"""
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
        # set to None if authorization_type (nullable) is None
        # and model_fields_set contains the field
        if (
            self.authorization_type is None
            and "authorization_type" in self.model_fields_set
        ):
            _dict["authorizationType"] = None

        # set to None if authorized_users (nullable) is None
        # and model_fields_set contains the field
        if (
            self.authorized_users is None
            and "authorized_users" in self.model_fields_set
        ):
            _dict["authorizedUsers"] = None

        # set to None if authorized_groups (nullable) is None
        # and model_fields_set contains the field
        if (
            self.authorized_groups is None
            and "authorized_groups" in self.model_fields_set
        ):
            _dict["authorizedGroups"] = None

        # set to None if cluster_local_access_only (nullable) is None
        # and model_fields_set contains the field
        if (
            self.cluster_local_access_only is None
            and "cluster_local_access_only" in self.model_fields_set
        ):
            _dict["clusterLocalAccessOnly"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServingPortAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "authorizationType": obj.get("authorizationType"),
                "authorizedUsers": obj.get("authorizedUsers"),
                "authorizedGroups": obj.get("authorizedGroups"),
                "clusterLocalAccessOnly": obj.get("clusterLocalAccessOnly"),
            }
        )
        return _obj
