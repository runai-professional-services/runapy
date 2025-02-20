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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class ExposedUrl(BaseModel):
    """
    Pydantic class model representing A URL for accessing the workload..

    Parameters:
        ```python
        container: Optional[int]
        url: Optional[str]
        authorized_users: Optional[List[str]]
        authorized_groups: Optional[List[str]]
        tool_type: Optional[str]
        tool_name: Optional[str]
        name: Optional[str]
        ```
        container: The port that the container running the workload exposes. (mandatory)
        url: The URL for connecting to the container port. If not specified, the URL will be auto-generated by the system..
        authorized_users: List of users that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        authorized_groups: List of groups that are allowed to access the URL. Note that authorizedUsers and authorizedGroups are mutually exclusive.
        tool_type: The tool type that runs on this container port.
        tool_name: A name describing the tool that runs on this url.
        name: Unique name to identify the instance. primarily used for policy locked rules.
    Example:
        ```python
        ExposedUrl(
            container=8080,
                        url='https://my-url.com',
                        authorized_users=["user-a","user-b"],
                        authorized_groups=["group-a","group-b"],
                        tool_type='jupyter',
                        tool_name='my-pytorch',
                        name='url-instance-a'
        )
        ```
    """  # noqa: E501

    container: Optional[StrictInt] = Field(
        default=None,
        description="The port that the container running the workload exposes. (mandatory)",
    )
    url: Optional[StrictStr] = Field(
        default=None,
        description="The URL for connecting to the container port. If not specified, the URL will be auto-generated by the system..",
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
    tool_type: Optional[StrictStr] = Field(
        default=None,
        description="The tool type that runs on this container port.",
        alias="toolType",
    )
    tool_name: Optional[StrictStr] = Field(
        default=None,
        description="A name describing the tool that runs on this url.",
        alias="toolName",
    )
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Unique name to identify the instance. primarily used for policy locked rules.",
    )
    __properties: ClassVar[List[str]] = [
        "container",
        "url",
        "authorizedUsers",
        "authorizedGroups",
        "toolType",
        "toolName",
        "name",
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
        """Create an instance of ExposedUrl from a JSON string"""
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

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict["url"] = None

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

        # set to None if tool_type (nullable) is None
        # and model_fields_set contains the field
        if self.tool_type is None and "tool_type" in self.model_fields_set:
            _dict["toolType"] = None

        # set to None if tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.tool_name is None and "tool_name" in self.model_fields_set:
            _dict["toolName"] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExposedUrl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "container": obj.get("container"),
                "url": obj.get("url"),
                "authorizedUsers": obj.get("authorizedUsers"),
                "authorizedGroups": obj.get("authorizedGroups"),
                "toolType": obj.get("toolType"),
                "toolName": obj.get("toolName"),
                "name": obj.get("name"),
            }
        )
        return _obj
