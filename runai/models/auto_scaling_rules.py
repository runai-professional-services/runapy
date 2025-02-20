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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.auto_scaling_metric_rules import AutoScalingMetricRules
from runai.models.integer_rules import IntegerRules
from typing import Optional, Set
from typing_extensions import Self


class AutoScalingRules(BaseModel):
    """
    Pydantic class model representing AutoScalingRules.

    Parameters:
        ```python
        min_replicas: Optional[IntegerRules]
        max_replicas: Optional[IntegerRules]
        metric: Optional[AutoScalingMetricRules]
        metric_threshold: Optional[IntegerRules]
        scale_to_zero_retention_seconds: Optional[IntegerRules]
        ```
        min_replicas: See model IntegerRules for more information.
        max_replicas: See model IntegerRules for more information.
        metric: See model AutoScalingMetricRules for more information.
        metric_threshold: See model IntegerRules for more information.
        scale_to_zero_retention_seconds: See model IntegerRules for more information.
    Example:
        ```python
        AutoScalingRules(
            min_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        max_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        metric=runai.models.auto_scaling_metric_rules.AutoScalingMetricRules(),
                        metric_threshold=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        scale_to_zero_retention_seconds=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, )
        )
        ```
    """  # noqa: E501

    min_replicas: Optional[IntegerRules] = Field(default=None, alias="minReplicas")
    max_replicas: Optional[IntegerRules] = Field(default=None, alias="maxReplicas")
    metric: Optional[AutoScalingMetricRules] = None
    metric_threshold: Optional[IntegerRules] = Field(
        default=None, alias="metricThreshold"
    )
    scale_to_zero_retention_seconds: Optional[IntegerRules] = Field(
        default=None, alias="scaleToZeroRetentionSeconds"
    )
    __properties: ClassVar[List[str]] = [
        "minReplicas",
        "maxReplicas",
        "metric",
        "metricThreshold",
        "scaleToZeroRetentionSeconds",
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
        """Create an instance of AutoScalingRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of min_replicas
        if self.min_replicas:
            _dict["minReplicas"] = self.min_replicas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_replicas
        if self.max_replicas:
            _dict["maxReplicas"] = self.max_replicas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict["metric"] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric_threshold
        if self.metric_threshold:
            _dict["metricThreshold"] = self.metric_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scale_to_zero_retention_seconds
        if self.scale_to_zero_retention_seconds:
            _dict["scaleToZeroRetentionSeconds"] = (
                self.scale_to_zero_retention_seconds.to_dict()
            )
        # set to None if min_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.min_replicas is None and "min_replicas" in self.model_fields_set:
            _dict["minReplicas"] = None

        # set to None if max_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.max_replicas is None and "max_replicas" in self.model_fields_set:
            _dict["maxReplicas"] = None

        # set to None if metric (nullable) is None
        # and model_fields_set contains the field
        if self.metric is None and "metric" in self.model_fields_set:
            _dict["metric"] = None

        # set to None if metric_threshold (nullable) is None
        # and model_fields_set contains the field
        if (
            self.metric_threshold is None
            and "metric_threshold" in self.model_fields_set
        ):
            _dict["metricThreshold"] = None

        # set to None if scale_to_zero_retention_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.scale_to_zero_retention_seconds is None
            and "scale_to_zero_retention_seconds" in self.model_fields_set
        ):
            _dict["scaleToZeroRetentionSeconds"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoScalingRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "minReplicas": (
                    IntegerRules.from_dict(obj["minReplicas"])
                    if obj.get("minReplicas") is not None
                    else None
                ),
                "maxReplicas": (
                    IntegerRules.from_dict(obj["maxReplicas"])
                    if obj.get("maxReplicas") is not None
                    else None
                ),
                "metric": (
                    AutoScalingMetricRules.from_dict(obj["metric"])
                    if obj.get("metric") is not None
                    else None
                ),
                "metricThreshold": (
                    IntegerRules.from_dict(obj["metricThreshold"])
                    if obj.get("metricThreshold") is not None
                    else None
                ),
                "scaleToZeroRetentionSeconds": (
                    IntegerRules.from_dict(obj["scaleToZeroRetentionSeconds"])
                    if obj.get("scaleToZeroRetentionSeconds") is not None
                    else None
                ),
            }
        )
        return _obj
