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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.project_v1_node_affinity_response_train_selected_types_inner import (
    ProjectV1NodeAffinityResponseTrainSelectedTypesInner,
)
from typing import Optional, Set
from typing_extensions import Self


class ProjectV1NodeAffinityResponseInteractive(BaseModel):
    """
    Pydantic class model representing Node affinity configuration for interactive jobs..

    Parameters:
        ```python
        affinity_type: str
        selected_types: List[ProjectV1NodeAffinityResponseTrainSelectedTypesInner]
        ```
        affinity_type: The type of affinity of the jobs on the nodes.
        selected_types: See model List[ProjectV1NodeAffinityResponseTrainSelectedTypesInner] for more information.
    Example:
        ```python
        ProjectV1NodeAffinityResponseInteractive(
            affinity_type='no_limit',
                        selected_types=[
                    runai.models.project_v1_node_affinity_response_train_selected_types_inner.ProjectV1NodeAffinityResponse_train_selectedTypes_inner(
                        id = 1.337,
                        name = '', )
                    ]
        )
        ```
    """  # noqa: E501

    affinity_type: Optional[StrictStr] = Field(
        default=None,
        description="The type of affinity of the jobs on the nodes.",
        alias="affinityType",
    )
    selected_types: List[ProjectV1NodeAffinityResponseTrainSelectedTypesInner] = Field(
        alias="selectedTypes"
    )
    __properties: ClassVar[List[str]] = ["affinityType", "selectedTypes"]

    @field_validator("affinity_type")
    def affinity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["no_limit", "only_selected"]):
            raise ValueError("must be one of enum values ('no_limit', 'only_selected')")
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
        """Create an instance of ProjectV1NodeAffinityResponseInteractive from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in selected_types (list)
        _items = []
        if self.selected_types:
            for _item_selected_types in self.selected_types:
                if _item_selected_types:
                    _items.append(_item_selected_types.to_dict())
            _dict["selectedTypes"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectV1NodeAffinityResponseInteractive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "affinityType": obj.get("affinityType"),
                "selectedTypes": (
                    [
                        ProjectV1NodeAffinityResponseTrainSelectedTypesInner.from_dict(
                            _item
                        )
                        for _item in obj["selectedTypes"]
                    ]
                    if obj.get("selectedTypes") is not None
                    else None
                ),
            }
        )
        return _obj
