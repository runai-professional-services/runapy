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
from typing import Optional, Set
from typing_extensions import Self


class PvcAccessModesRules(BaseModel):
    """
    Pydantic class model representing Rules for access mode(s) for a newly created PVC..

    Parameters:
        ```python
        read_write_once: Optional[BooleanRules]
        read_only_many: Optional[BooleanRules]
        read_write_many: Optional[BooleanRules]
        ```
        read_write_once: See model BooleanRules for more information.
        read_only_many: See model BooleanRules for more information.
        read_write_many: See model BooleanRules for more information.
    Example:
        ```python
        PvcAccessModesRules(
            read_write_once=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        read_only_many=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        read_write_many=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, )
        )
        ```
    """  # noqa: E501

    read_write_once: Optional[BooleanRules] = Field(default=None, alias="readWriteOnce")
    read_only_many: Optional[BooleanRules] = Field(default=None, alias="readOnlyMany")
    read_write_many: Optional[BooleanRules] = Field(default=None, alias="readWriteMany")
    __properties: ClassVar[List[str]] = [
        "readWriteOnce",
        "readOnlyMany",
        "readWriteMany",
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
        """Create an instance of PvcAccessModesRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of read_write_once
        if self.read_write_once:
            _dict["readWriteOnce"] = self.read_write_once.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_only_many
        if self.read_only_many:
            _dict["readOnlyMany"] = self.read_only_many.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_write_many
        if self.read_write_many:
            _dict["readWriteMany"] = self.read_write_many.to_dict()
        # set to None if read_write_once (nullable) is None
        # and model_fields_set contains the field
        if self.read_write_once is None and "read_write_once" in self.model_fields_set:
            _dict["readWriteOnce"] = None

        # set to None if read_only_many (nullable) is None
        # and model_fields_set contains the field
        if self.read_only_many is None and "read_only_many" in self.model_fields_set:
            _dict["readOnlyMany"] = None

        # set to None if read_write_many (nullable) is None
        # and model_fields_set contains the field
        if self.read_write_many is None and "read_write_many" in self.model_fields_set:
            _dict["readWriteMany"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PvcAccessModesRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "readWriteOnce": (
                    BooleanRules.from_dict(obj["readWriteOnce"])
                    if obj.get("readWriteOnce") is not None
                    else None
                ),
                "readOnlyMany": (
                    BooleanRules.from_dict(obj["readOnlyMany"])
                    if obj.get("readOnlyMany") is not None
                    else None
                ),
                "readWriteMany": (
                    BooleanRules.from_dict(obj["readWriteMany"])
                    if obj.get("readWriteMany") is not None
                    else None
                ),
            }
        )
        return _obj
