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
from runai.models.source_of_rule import SourceOfRule
from typing import Optional, Set
from typing_extensions import Self


class ItemRules(BaseModel):
    """
    Pydantic class model representing ItemRules.

    Parameters:
        ```python
        source_of_rule: Optional[SourceOfRule]
        can_add: Optional[bool]
        locked: List[str]
        ```
        source_of_rule: See model SourceOfRule for more information.
        can_add: Whether it is permitted to add items. Default to true.
        locked: Set of keys for items that are \&quot;locked\&quot;, i.e. cannot be removed or deleted.
    Example:
        ```python
        ItemRules(
            source_of_rule={"scope":"project","projectId":3},
                        can_add=True,
                        locked=["HOME","USER"]
        )
        ```
    """  # noqa: E501

    source_of_rule: Optional[SourceOfRule] = Field(default=None, alias="sourceOfRule")
    can_add: Optional[StrictBool] = Field(
        default=None,
        description="Whether it is permitted to add items. Default to true.",
        alias="canAdd",
    )
    locked: Optional[List[StrictStr]] = Field(
        default=None,
        description='Set of keys for items that are "locked", i.e. cannot be removed or deleted.',
    )
    __properties: ClassVar[List[str]] = ["sourceOfRule", "canAdd", "locked"]

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
        """Create an instance of ItemRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_of_rule
        if self.source_of_rule:
            _dict["sourceOfRule"] = self.source_of_rule.to_dict()
        # set to None if source_of_rule (nullable) is None
        # and model_fields_set contains the field
        if self.source_of_rule is None and "source_of_rule" in self.model_fields_set:
            _dict["sourceOfRule"] = None

        # set to None if can_add (nullable) is None
        # and model_fields_set contains the field
        if self.can_add is None and "can_add" in self.model_fields_set:
            _dict["canAdd"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "sourceOfRule": (
                    SourceOfRule.from_dict(obj["sourceOfRule"])
                    if obj.get("sourceOfRule") is not None
                    else None
                ),
                "canAdd": obj.get("canAdd"),
                "locked": obj.get("locked"),
            }
        )
        return _obj
