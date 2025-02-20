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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class ClusterReportedStatusConditionsInner(BaseModel):
    """
    Pydantic class model representing Condition contains details for one aspect of the current state of this API Resource.

    Parameters:
        ```python
        last_transition_time: datetime
        message: str
        observed_generation: int
        reason: str
        status: str
        type: str
        ```
        last_transition_time: lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
        message: message is a human readable message indicating details about the transition. This may be an empty string.
        observed_generation: observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.
        reason: reason contains a programmatic identifier indicating the reason for the condition&#39;s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.
        status: status of the condition, one of True, False, Unknown.
        type: type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)
    Example:
        ```python
        ClusterReportedStatusConditionsInner(
            last_transition_time=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        message='',
                        observed_generation=0,
                        reason='AbUUGjjNSwg1_bs:ZayIMrKdgNvb7gvxmPb:GcsM72ate2RA9:q4w2l5eH5XxEz06awo0',
                        status='True',
                        type=''
        )
        ```
    """  # noqa: E501

    last_transition_time: datetime = Field(
        description="lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.",
        alias="lastTransitionTime",
    )
    message: Annotated[str, Field(strict=True, max_length=32768)] = Field(
        description="message is a human readable message indicating details about the transition. This may be an empty string."
    )
    observed_generation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.",
        alias="observedGeneration",
    )
    reason: Annotated[str, Field(min_length=1, strict=True, max_length=1024)] = Field(
        description="reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty."
    )
    status: StrictStr = Field(
        description="status of the condition, one of True, False, Unknown."
    )
    type: Annotated[str, Field(strict=True, max_length=316)] = Field(
        description="type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)"
    )
    __properties: ClassVar[List[str]] = [
        "lastTransitionTime",
        "message",
        "observedGeneration",
        "reason",
        "status",
        "type",
    ]

    @field_validator("reason")
    def reason_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$", value):
            raise ValueError(
                r"must validate the regular expression /^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$/"
            )
        return value

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["True", "False", "Unknown"]):
            raise ValueError("must be one of enum values ('True', 'False', 'Unknown')")
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
        """Create an instance of ClusterReportedStatusConditionsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterReportedStatusConditionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "lastTransitionTime": obj.get("lastTransitionTime"),
                "message": obj.get("message"),
                "observedGeneration": obj.get("observedGeneration"),
                "reason": obj.get("reason"),
                "status": obj.get("status"),
                "type": obj.get("type"),
            }
        )
        return _obj
