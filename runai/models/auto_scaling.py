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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.auto_scaling_metric import AutoScalingMetric
from typing import Optional, Set
from typing_extensions import Self


class AutoScaling(BaseModel):
    """
    Pydantic class model representing AutoScaling.

    Parameters:
        ```python
        min_replicas: Optional[int]
        max_replicas: Optional[int]
        scale_to_zero_retention_seconds: Optional[int]
        metric: Optional[AutoScalingMetric]
        metric_threshold: Optional[int]
        ```
        min_replicas: The minimum number of replicas for autoscaling. Defaults to 1. Use 0 to allow scale-to-zero
        max_replicas: The maximum number of replicas for autoscaling. Defaults to minReplicas, or to 1 if minReplicas is set to 0
        scale_to_zero_retention_seconds: The minimum amount of time (in seconds) that the last replica will remain active after a scale-to-zero decision. Defaults to 0. Available only if minReplicas is set to 0
        metric: See model AutoScalingMetric for more information.
        metric_threshold: The threshold to use with the specified metric for autoscaling. Mandatory if metric is specified
    Example:
        ```python
        AutoScaling(
            min_replicas=0,
                        max_replicas=1,
                        scale_to_zero_retention_seconds=0,
                        metric='throughput',
                        metric_threshold=56
        )
        ```
    """  # noqa: E501

    min_replicas: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="The minimum number of replicas for autoscaling. Defaults to 1. Use 0 to allow scale-to-zero",
        alias="minReplicas",
    )
    max_replicas: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="The maximum number of replicas for autoscaling. Defaults to minReplicas, or to 1 if minReplicas is set to 0",
        alias="maxReplicas",
    )
    scale_to_zero_retention_seconds: Optional[
        Annotated[int, Field(le=3600, strict=True, ge=0)]
    ] = Field(
        default=None,
        description="The minimum amount of time (in seconds) that the last replica will remain active after a scale-to-zero decision. Defaults to 0. Available only if minReplicas is set to 0",
        alias="scaleToZeroRetentionSeconds",
    )
    metric: Optional[AutoScalingMetric] = None
    metric_threshold: Optional[StrictInt] = Field(
        default=None,
        description="The threshold to use with the specified metric for autoscaling. Mandatory if metric is specified",
        alias="metricThreshold",
    )
    __properties: ClassVar[List[str]] = [
        "minReplicas",
        "maxReplicas",
        "scaleToZeroRetentionSeconds",
        "metric",
        "metricThreshold",
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
        """Create an instance of AutoScaling from a JSON string"""
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
        # set to None if min_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.min_replicas is None and "min_replicas" in self.model_fields_set:
            _dict["minReplicas"] = None

        # set to None if max_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.max_replicas is None and "max_replicas" in self.model_fields_set:
            _dict["maxReplicas"] = None

        # set to None if scale_to_zero_retention_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.scale_to_zero_retention_seconds is None
            and "scale_to_zero_retention_seconds" in self.model_fields_set
        ):
            _dict["scaleToZeroRetentionSeconds"] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AutoScaling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "minReplicas": obj.get("minReplicas"),
                "maxReplicas": obj.get("maxReplicas"),
                "scaleToZeroRetentionSeconds": obj.get("scaleToZeroRetentionSeconds"),
                "metric": obj.get("metric"),
                "metricThreshold": obj.get("metricThreshold"),
            }
        )
        return _obj
