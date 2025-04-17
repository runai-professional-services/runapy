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
from runai.models.integer_rules import IntegerRules
from runai.models.restart_policy_rule import RestartPolicyRule
from typing import Optional, Set
from typing_extensions import Self


class AdvancedFlatFieldsRules(BaseModel):
    """
    Pydantic class model representing AdvancedFlatFieldsRules.

    Parameters:
        ```python
        terminate_after_preemption: Optional[BooleanRules]
        auto_deletion_time_after_completion_seconds: Optional[IntegerRules]
        termination_grace_period_seconds: Optional[IntegerRules]
        backoff_limit: Optional[IntegerRules]
        restart_policy: Optional[RestartPolicyRule]
        ```
        terminate_after_preemption: See model BooleanRules for more information.
        auto_deletion_time_after_completion_seconds: See model IntegerRules for more information.
        termination_grace_period_seconds: See model IntegerRules for more information.
        backoff_limit: See model IntegerRules for more information.
        restart_policy: See model RestartPolicyRule for more information.
    Example:
        ```python
        AdvancedFlatFieldsRules(
            terminate_after_preemption=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        auto_deletion_time_after_completion_seconds=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56,
                    default_from = runai.models.default_from_rule.DefaultFromRule(
                        field = '',
                        factor = 1.337, ), ),
                        termination_grace_period_seconds=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56,
                    default_from = runai.models.default_from_rule.DefaultFromRule(
                        field = '',
                        factor = 1.337, ), ),
                        backoff_limit=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56,
                    default_from = runai.models.default_from_rule.DefaultFromRule(
                        field = '',
                        factor = 1.337, ), ),
                        restart_policy=runai.models.restart_policy_rule.RestartPolicyRule()
        )
        ```
    """  # noqa: E501

    terminate_after_preemption: Optional[BooleanRules] = Field(
        default=None, alias="terminateAfterPreemption"
    )
    auto_deletion_time_after_completion_seconds: Optional[IntegerRules] = Field(
        default=None, alias="autoDeletionTimeAfterCompletionSeconds"
    )
    termination_grace_period_seconds: Optional[IntegerRules] = Field(
        default=None, alias="terminationGracePeriodSeconds"
    )
    backoff_limit: Optional[IntegerRules] = Field(default=None, alias="backoffLimit")
    restart_policy: Optional[RestartPolicyRule] = Field(
        default=None, alias="restartPolicy"
    )
    __properties: ClassVar[List[str]] = [
        "terminateAfterPreemption",
        "autoDeletionTimeAfterCompletionSeconds",
        "terminationGracePeriodSeconds",
        "backoffLimit",
        "restartPolicy",
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
        """Create an instance of AdvancedFlatFieldsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of terminate_after_preemption
        if self.terminate_after_preemption:
            _dict["terminateAfterPreemption"] = (
                self.terminate_after_preemption.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of auto_deletion_time_after_completion_seconds
        if self.auto_deletion_time_after_completion_seconds:
            _dict["autoDeletionTimeAfterCompletionSeconds"] = (
                self.auto_deletion_time_after_completion_seconds.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of termination_grace_period_seconds
        if self.termination_grace_period_seconds:
            _dict["terminationGracePeriodSeconds"] = (
                self.termination_grace_period_seconds.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of backoff_limit
        if self.backoff_limit:
            _dict["backoffLimit"] = self.backoff_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of restart_policy
        if self.restart_policy:
            _dict["restartPolicy"] = self.restart_policy.to_dict()
        # set to None if terminate_after_preemption (nullable) is None
        # and model_fields_set contains the field
        if (
            self.terminate_after_preemption is None
            and "terminate_after_preemption" in self.model_fields_set
        ):
            _dict["terminateAfterPreemption"] = None

        # set to None if auto_deletion_time_after_completion_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.auto_deletion_time_after_completion_seconds is None
            and "auto_deletion_time_after_completion_seconds" in self.model_fields_set
        ):
            _dict["autoDeletionTimeAfterCompletionSeconds"] = None

        # set to None if termination_grace_period_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.termination_grace_period_seconds is None
            and "termination_grace_period_seconds" in self.model_fields_set
        ):
            _dict["terminationGracePeriodSeconds"] = None

        # set to None if backoff_limit (nullable) is None
        # and model_fields_set contains the field
        if self.backoff_limit is None and "backoff_limit" in self.model_fields_set:
            _dict["backoffLimit"] = None

        # set to None if restart_policy (nullable) is None
        # and model_fields_set contains the field
        if self.restart_policy is None and "restart_policy" in self.model_fields_set:
            _dict["restartPolicy"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvancedFlatFieldsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "terminateAfterPreemption": (
                    BooleanRules.from_dict(obj["terminateAfterPreemption"])
                    if obj.get("terminateAfterPreemption") is not None
                    else None
                ),
                "autoDeletionTimeAfterCompletionSeconds": (
                    IntegerRules.from_dict(
                        obj["autoDeletionTimeAfterCompletionSeconds"]
                    )
                    if obj.get("autoDeletionTimeAfterCompletionSeconds") is not None
                    else None
                ),
                "terminationGracePeriodSeconds": (
                    IntegerRules.from_dict(obj["terminationGracePeriodSeconds"])
                    if obj.get("terminationGracePeriodSeconds") is not None
                    else None
                ),
                "backoffLimit": (
                    IntegerRules.from_dict(obj["backoffLimit"])
                    if obj.get("backoffLimit") is not None
                    else None
                ),
                "restartPolicy": (
                    RestartPolicyRule.from_dict(obj["restartPolicy"])
                    if obj.get("restartPolicy") is not None
                    else None
                ),
            }
        )
        return _obj
