# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.integer_rules import IntegerRules
from runai.models.string_rules import StringRules
from typing import Optional, Set
from typing_extensions import Self


class ProbeHandlerRulesHttpGet(BaseModel):
    """
    Pydantic class model representing ProbeHandlerRulesHttpGet.

    Parameters:
        ```python
        path: Optional[StringRules]
        port: Optional[IntegerRules]
        host: Optional[StringRules]
        scheme: Optional[StringRules]
        ```
        path: See model StringRules for more information.
        port: See model IntegerRules for more information.
        host: See model StringRules for more information.
        scheme: See model StringRules for more information.
    Example:
        ```python
        ProbeHandlerRulesHttpGet(
            path=runai.models.string_rules.StringRules(),
                        port=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56,
                    default_from = runai.models.default_from_rule.DefaultFromRule(
                        field = '',
                        factor = 1.337, ), ),
                        host=runai.models.string_rules.StringRules(),
                        scheme=runai.models.string_rules.StringRules()
        )
        ```
    """  # noqa: E501

    path: Optional[StringRules] = None
    port: Optional[IntegerRules] = None
    host: Optional[StringRules] = None
    scheme: Optional[StringRules] = None
    __properties: ClassVar[List[str]] = ["path", "port", "host", "scheme"]

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
        """Create an instance of ProbeHandlerRulesHttpGet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict["port"] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of host
        if self.host:
            _dict["host"] = self.host.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheme
        if self.scheme:
            _dict["scheme"] = self.scheme.to_dict()
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict["port"] = None

        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict["host"] = None

        # set to None if scheme (nullable) is None
        # and model_fields_set contains the field
        if self.scheme is None and "scheme" in self.model_fields_set:
            _dict["scheme"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProbeHandlerRulesHttpGet from a dict"""
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
                "port": (
                    IntegerRules.from_dict(obj["port"])
                    if obj.get("port") is not None
                    else None
                ),
                "host": (
                    StringRules.from_dict(obj["host"])
                    if obj.get("host") is not None
                    else None
                ),
                "scheme": (
                    StringRules.from_dict(obj["scheme"])
                    if obj.get("scheme") is not None
                    else None
                ),
            }
        )
        return _obj
