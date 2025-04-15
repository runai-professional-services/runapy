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
from runai.models.item_rules import ItemRules
from runai.models.port_rules import PortRules
from typing import Optional, Set
from typing_extensions import Self


class PortsRules(BaseModel):
    """
    Pydantic class model representing PortsRules.

    Parameters:
        ```python
        attributes: Optional[PortRules]
        instances: Optional[ItemRules]
        ```
        attributes: See model PortRules for more information.
        instances: See model ItemRules for more information.
    Example:
        ```python
        PortsRules(
            attributes=runai.models.port_rules.PortRules(
                    container = runai.models.integer_rules.IntegerRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56,
                        default_from = runai.models.default_from_rule.DefaultFromRule(
                            field = '',
                            factor = 1.337, ), ),
                    service_type = runai.models.port_service_type_rules.PortServiceTypeRules(),
                    custom_external_port = runai.models.boolean_rules.BooleanRules(
                        required = True,
                        can_edit = True, ),
                    external = runai.models.integer_rules.IntegerRules(
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    tool_type = runai.models.string_rules.StringRules(),
                    tool_name = runai.models.string_rules.StringRules(), ),
                        instances=runai.models.item_rules.ItemRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    can_add = True,
                    locked = ["HOME","USER"], )
        )
        ```
    """  # noqa: E501

    attributes: Optional[PortRules] = None
    instances: Optional[ItemRules] = None
    __properties: ClassVar[List[str]] = ["attributes", "instances"]

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
        """Create an instance of PortsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict["attributes"] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instances
        if self.instances:
            _dict["instances"] = self.instances.to_dict()
        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict["attributes"] = None

        # set to None if instances (nullable) is None
        # and model_fields_set contains the field
        if self.instances is None and "instances" in self.model_fields_set:
            _dict["instances"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "attributes": (
                    PortRules.from_dict(obj["attributes"])
                    if obj.get("attributes") is not None
                    else None
                ),
                "instances": (
                    ItemRules.from_dict(obj["instances"])
                    if obj.get("instances") is not None
                    else None
                ),
            }
        )
        return _obj
