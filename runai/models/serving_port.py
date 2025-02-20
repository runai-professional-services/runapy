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

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.serving_port_protocol import ServingPortProtocol
from typing import Optional, Set
from typing_extensions import Self


class ServingPort(BaseModel):
    """
    Pydantic class model representing A port for accessing the inference service.

    Parameters:
        ```python
        container: Optional[int]
        protocol: Optional[ServingPortProtocol]
        authorization_type: Optional[str]
        authorized_users: Optional[List[str]]
        authorized_groups: Optional[List[str]]
        cluster_local_access_only: Optional[bool]
        ```
        container: The port that the container running the inference service exposes (mandatory).
        protocol: See model ServingPortProtocol for more information.
        authorization_type: The authorization type for serving port URL access. Defaults to public, which means no authorization is required. If set to authenticatedUsers, only authenticated Run:ai users are allowed to access the URL. If set to authorizedUsersOrGroups, only users or groups specified in authorizedUsers or authorizedGroups are allowed to access the URL.
        authorized_users: List of users that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        authorized_groups: List of groups that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        cluster_local_access_only: Configure the serving port URL to be available only on the cluster-local network, and not externally. Defaults to false
    Example:
        ```python
        ServingPort(
            container=8080,
                        protocol='http',
                        authorization_type='public',
                        authorized_users=[user.a@example.com, user.b@example.com],
                        authorized_groups=[group-a, group-b],
                        cluster_local_access_only=True
        )
        ```
    """  # noqa: E501

    container: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(
        default=None,
        description="The port that the container running the inference service exposes (mandatory).",
    )
    protocol: Optional[ServingPortProtocol] = None
    authorization_type: Optional[StrictStr] = Field(
        default=None,
        description="The authorization type for serving port URL access. Defaults to public, which means no authorization is required. If set to authenticatedUsers, only authenticated Run:ai users are allowed to access the URL. If set to authorizedUsersOrGroups, only users or groups specified in authorizedUsers or authorizedGroups are allowed to access the URL.",
        alias="authorizationType",
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
        "container",
        "protocol",
        "authorizationType",
        "authorizedUsers",
        "authorizedGroups",
        "clusterLocalAccessOnly",
    ]

    @field_validator("authorization_type")
    def authorization_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            ["public", "authenticatedUsers", "authorizedUsersOrGroups"]
        ):
            raise ValueError(
                "must be one of enum values ('public', 'authenticatedUsers', 'authorizedUsersOrGroups')"
            )
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
        """Create an instance of ServingPort from a JSON string"""
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
        # set to None if container (nullable) is None
        # and model_fields_set contains the field
        if self.container is None and "container" in self.model_fields_set:
            _dict["container"] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict["protocol"] = None

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
        """Create an instance of ServingPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "container": obj.get("container"),
                "protocol": obj.get("protocol"),
                "authorizationType": obj.get("authorizationType"),
                "authorizedUsers": obj.get("authorizedUsers"),
                "authorizedGroups": obj.get("authorizedGroups"),
                "clusterLocalAccessOnly": obj.get("clusterLocalAccessOnly"),
            }
        )
        return _obj
