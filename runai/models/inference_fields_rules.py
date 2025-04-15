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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.auto_scaling_rules import AutoScalingRules
from runai.models.serving_port_rules import ServingPortRules
from typing import Optional, Set
from typing_extensions import Self


class InferenceFieldsRules(BaseModel):
    """
    Pydantic class model representing InferenceFieldsRules.

    Parameters:
        ```python
        serving_port: Optional[ServingPortRules]
        autoscaling: Optional[AutoScalingRules]
        ```
        serving_port: See model ServingPortRules for more information.
        autoscaling: See model AutoScalingRules for more information.
    Example:
        ```python
        InferenceFieldsRules(
            serving_port=runai.models.serving_port_rules.ServingPortRules(
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
                    protocol = runai.models.serving_port_protocol_rules.ServingPortProtocolRules(), ),
                        autoscaling=runai.models.auto_scaling_rules.AutoScalingRules(
                    metric_threshold_percentage = runai.models.number_rules.NumberRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        required = True,
                        can_edit = True,
                        min = 1.337,
                        max = 1.337,
                        step = 1.337,
                        default_from = runai.models.default_from_rule.DefaultFromRule(
                            field = '',
                            factor = 1.337, ), ),
                    min_replicas = runai.models.integer_rules.IntegerRules(
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    max_replicas = runai.models.integer_rules.IntegerRules(
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    initial_replicas = ,
                    activation_replicas = ,
                    metric = runai.models.auto_scaling_metric_rules.AutoScalingMetricRules(),
                    metric_threshold = ,
                    concurrency_hard_limit = ,
                    scale_to_zero_retention_seconds = ,
                    scale_down_delay_seconds = ,
                    initialization_timeout_seconds = , )
        )
        ```
    """  # noqa: E501

    serving_port: Optional[ServingPortRules] = Field(default=None, alias="servingPort")
    autoscaling: Optional[AutoScalingRules] = None
    __properties: ClassVar[List[str]] = ["servingPort", "autoscaling"]

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
        """Create an instance of InferenceFieldsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of serving_port
        if self.serving_port:
            _dict["servingPort"] = self.serving_port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of autoscaling
        if self.autoscaling:
            _dict["autoscaling"] = self.autoscaling.to_dict()
        # set to None if serving_port (nullable) is None
        # and model_fields_set contains the field
        if self.serving_port is None and "serving_port" in self.model_fields_set:
            _dict["servingPort"] = None

        # set to None if autoscaling (nullable) is None
        # and model_fields_set contains the field
        if self.autoscaling is None and "autoscaling" in self.model_fields_set:
            _dict["autoscaling"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InferenceFieldsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "servingPort": (
                    ServingPortRules.from_dict(obj["servingPort"])
                    if obj.get("servingPort") is not None
                    else None
                ),
                "autoscaling": (
                    AutoScalingRules.from_dict(obj["autoscaling"])
                    if obj.get("autoscaling") is not None
                    else None
                ),
            }
        )
        return _obj
