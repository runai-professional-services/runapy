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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.boolean_rules import BooleanRules
from runai.models.string_rules import StringRules
from typing import Optional, Set
from typing_extensions import Self


class NfsRules(BaseModel):
    """
    Pydantic class model representing NfsRules.

    Parameters:
        ```python
        path: Optional[StringRules]
        read_only: Optional[BooleanRules]
        server: Optional[StringRules]
        mount_path: Optional[StringRules]
        ```
        path: See model StringRules for more information.
        read_only: See model BooleanRules for more information.
        server: See model StringRules for more information.
        mount_path: See model StringRules for more information.
    Example:
        ```python
        NfsRules(
            path=runai.models.string_rules.StringRules(),
                        read_only=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        server=runai.models.string_rules.StringRules(),
                        mount_path=runai.models.string_rules.StringRules()
        )
        ```
    """  # noqa: E501

    path: Optional[StringRules] = None
    read_only: Optional[BooleanRules] = Field(default=None, alias="readOnly")
    server: Optional[StringRules] = None
    mount_path: Optional[StringRules] = Field(default=None, alias="mountPath")
    __properties: ClassVar[List[str]] = ["path", "readOnly", "server", "mountPath"]

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
        """Create an instance of NfsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of path
        if self.path:
            _dict["path"] = self.path.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_only
        if self.read_only:
            _dict["readOnly"] = self.read_only.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict["server"] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mount_path
        if self.mount_path:
            _dict["mountPath"] = self.mount_path.to_dict()
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if read_only (nullable) is None
        # and model_fields_set contains the field
        if self.read_only is None and "read_only" in self.model_fields_set:
            _dict["readOnly"] = None

        # set to None if server (nullable) is None
        # and model_fields_set contains the field
        if self.server is None and "server" in self.model_fields_set:
            _dict["server"] = None

        # set to None if mount_path (nullable) is None
        # and model_fields_set contains the field
        if self.mount_path is None and "mount_path" in self.model_fields_set:
            _dict["mountPath"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NfsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "path": (
                    StringRules.from_dict(obj["path"])
                    if obj.get("path") is not None
                    else None
                ),
                "readOnly": (
                    BooleanRules.from_dict(obj["readOnly"])
                    if obj.get("readOnly") is not None
                    else None
                ),
                "server": (
                    StringRules.from_dict(obj["server"])
                    if obj.get("server") is not None
                    else None
                ),
                "mountPath": (
                    StringRules.from_dict(obj["mountPath"])
                    if obj.get("mountPath") is not None
                    else None
                ),
            }
        )
        return _obj
