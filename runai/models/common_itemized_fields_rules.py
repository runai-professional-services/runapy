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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.instances_rules import InstancesRules
from typing import Optional, Set
from typing_extensions import Self


class CommonItemizedFieldsRules(BaseModel):
    """
    Pydantic class model representing CommonItemizedFieldsRules.

    Parameters:
        ```python
        environment_variables: Optional[InstancesRules]
        annotations: Optional[InstancesRules]
        labels: Optional[InstancesRules]
        tolerations: Optional[InstancesRules]
        ```
        environment_variables: See model InstancesRules for more information.
        annotations: See model InstancesRules for more information.
        labels: See model InstancesRules for more information.
        tolerations: See model InstancesRules for more information.
    Example:
        ```python
        CommonItemizedFieldsRules(
            environment_variables=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        annotations=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        labels=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        tolerations=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), )
        )
        ```
    """  # noqa: E501

    environment_variables: Optional[InstancesRules] = Field(
        default=None, alias="environmentVariables"
    )
    annotations: Optional[InstancesRules] = None
    labels: Optional[InstancesRules] = None
    tolerations: Optional[InstancesRules] = None
    __properties: ClassVar[List[str]] = [
        "environmentVariables",
        "annotations",
        "labels",
        "tolerations",
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
        """Create an instance of CommonItemizedFieldsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environment_variables
        if self.environment_variables:
            _dict["environmentVariables"] = self.environment_variables.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict["annotations"] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict["labels"] = self.labels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tolerations
        if self.tolerations:
            _dict["tolerations"] = self.tolerations.to_dict()
        # set to None if environment_variables (nullable) is None
        # and model_fields_set contains the field
        if (
            self.environment_variables is None
            and "environment_variables" in self.model_fields_set
        ):
            _dict["environmentVariables"] = None

        # set to None if annotations (nullable) is None
        # and model_fields_set contains the field
        if self.annotations is None and "annotations" in self.model_fields_set:
            _dict["annotations"] = None

        # set to None if labels (nullable) is None
        # and model_fields_set contains the field
        if self.labels is None and "labels" in self.model_fields_set:
            _dict["labels"] = None

        # set to None if tolerations (nullable) is None
        # and model_fields_set contains the field
        if self.tolerations is None and "tolerations" in self.model_fields_set:
            _dict["tolerations"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonItemizedFieldsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "environmentVariables": (
                    InstancesRules.from_dict(obj["environmentVariables"])
                    if obj.get("environmentVariables") is not None
                    else None
                ),
                "annotations": (
                    InstancesRules.from_dict(obj["annotations"])
                    if obj.get("annotations") is not None
                    else None
                ),
                "labels": (
                    InstancesRules.from_dict(obj["labels"])
                    if obj.get("labels") is not None
                    else None
                ),
                "tolerations": (
                    InstancesRules.from_dict(obj["tolerations"])
                    if obj.get("tolerations") is not None
                    else None
                ),
            }
        )
        return _obj
