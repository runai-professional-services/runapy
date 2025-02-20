# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class SpecificRunMetricFields(BaseModel):
    """
    Pydantic class model representing SpecificRunMetricFields.

    Parameters:
        ```python
        threshold_metric: Optional[str]
        threshold_value: Optional[int]
        ```
        threshold_metric: The metric to use for autoscaling. Mandatory if minReplicas &lt; maxReplicas, except for the special case where minReplicas is set to 0 and maxReplicas is set to 1, as in this case autoscaling decisions are made according to network activity rather than metrics. Use one of the built-in metrics of &#39;throughput&#39;, &#39;concurrency&#39; or &#39;latency&#39;, or any other available custom metric. Only the &#39;throughput&#39; and &#39;concurrency&#39; metrics support scale-to-zero
        threshold_value: The threshold value to use with the specified metric for autoscaling
    Example:
        ```python
        SpecificRunMetricFields(
            threshold_metric='http_requests_total',
                        threshold_value=56
        )
        ```
    """  # noqa: E501

    threshold_metric: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="The metric to use for autoscaling. Mandatory if minReplicas < maxReplicas, except for the special case where minReplicas is set to 0 and maxReplicas is set to 1, as in this case autoscaling decisions are made according to network activity rather than metrics. Use one of the built-in metrics of 'throughput', 'concurrency' or 'latency', or any other available custom metric. Only the 'throughput' and 'concurrency' metrics support scale-to-zero",
        alias="thresholdMetric",
    )
    threshold_value: Optional[StrictInt] = Field(
        default=None,
        description="The threshold value to use with the specified metric for autoscaling",
        alias="thresholdValue",
    )
    __properties: ClassVar[List[str]] = ["thresholdMetric", "thresholdValue"]

    @field_validator("threshold_metric")
    def threshold_metric_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z_:][a-zA-Z0-9_:]*$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-zA-Z_:][a-zA-Z0-9_:]*$/"
            )
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
        """Create an instance of SpecificRunMetricFields from a JSON string"""
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
        # set to None if threshold_metric (nullable) is None
        # and model_fields_set contains the field
        if (
            self.threshold_metric is None
            and "threshold_metric" in self.model_fields_set
        ):
            _dict["thresholdMetric"] = None

        # set to None if threshold_value (nullable) is None
        # and model_fields_set contains the field
        if self.threshold_value is None and "threshold_value" in self.model_fields_set:
            _dict["thresholdValue"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpecificRunMetricFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "thresholdMetric": obj.get("thresholdMetric"),
                "thresholdValue": obj.get("thresholdValue"),
            }
        )
        return _obj
