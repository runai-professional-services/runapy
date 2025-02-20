# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from runai.models.source_of_rule import SourceOfRule
from typing import Optional, Set
from typing_extensions import Self


class NumberRules(BaseModel):
    """
    Pydantic class model representing NumberRules.

    Parameters:
        ```python
        source_of_rule: Optional[SourceOfRule]
        required: Optional[bool]
        can_edit: Optional[bool]
        min: Optional[float]
        max: Optional[float]
        step: Optional[float]
        ```
        source_of_rule: See model SourceOfRule for more information.
        required: Whether the field is mandatory. default to false.
        can_edit: Whether the value of the field is editable. default to true
        min: The minimum value that the field can be assigned to.
        max: The maximum value that the field can be assigned to.
        step: The minimal difference between two values the field can be assigned to. For example, min&#x3D;2, max&#x3D;3, step&#x3D;0.25 implies that the values the field can hold are 2, 2.25, 2.5 and 3.
    Example:
        ```python
        NumberRules(
            source_of_rule={"scope":"project","projectId":3},
                        required=True,
                        can_edit=True,
                        min=1.337,
                        max=1.337,
                        step=1.337
        )
        ```
    """  # noqa: E501

    source_of_rule: Optional[SourceOfRule] = Field(default=None, alias="sourceOfRule")
    required: Optional[StrictBool] = Field(
        default=None, description="Whether the field is mandatory. default to false."
    )
    can_edit: Optional[StrictBool] = Field(
        default=None,
        description="Whether the value of the field is editable. default to true",
        alias="canEdit",
    )
    min: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="The minimum value that the field can be assigned to."
    )
    max: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="The maximum value that the field can be assigned to."
    )
    step: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The minimal difference between two values the field can be assigned to. For example, min=2, max=3, step=0.25 implies that the values the field can hold are 2, 2.25, 2.5 and 3.",
    )
    __properties: ClassVar[List[str]] = [
        "sourceOfRule",
        "required",
        "canEdit",
        "min",
        "max",
        "step",
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
        """Create an instance of NumberRules from a JSON string"""
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

        # set to None if required (nullable) is None
        # and model_fields_set contains the field
        if self.required is None and "required" in self.model_fields_set:
            _dict["required"] = None

        # set to None if can_edit (nullable) is None
        # and model_fields_set contains the field
        if self.can_edit is None and "can_edit" in self.model_fields_set:
            _dict["canEdit"] = None

        # set to None if min (nullable) is None
        # and model_fields_set contains the field
        if self.min is None and "min" in self.model_fields_set:
            _dict["min"] = None

        # set to None if max (nullable) is None
        # and model_fields_set contains the field
        if self.max is None and "max" in self.model_fields_set:
            _dict["max"] = None

        # set to None if step (nullable) is None
        # and model_fields_set contains the field
        if self.step is None and "step" in self.model_fields_set:
            _dict["step"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NumberRules from a dict"""
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
                "required": obj.get("required"),
                "canEdit": obj.get("canEdit"),
                "min": obj.get("min"),
                "max": obj.get("max"),
                "step": obj.get("step"),
            }
        )
        return _obj
