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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.restart_policy import RestartPolicy
from typing import Optional, Set
from typing_extensions import Self


class AdvancedFlatFields(BaseModel):
    """
    Pydantic class model representing AdvancedFlatFields.

    Parameters:
        ```python
        terminate_after_preemption: Optional[bool]
        auto_deletion_time_after_completion_seconds: Optional[int]
        termination_grace_period_seconds: Optional[int]
        backoff_limit: Optional[int]
        restart_policy: Optional[RestartPolicy]
        ```
        terminate_after_preemption: Indicates if the job should be terminated by the system after it has been preempted.
        auto_deletion_time_after_completion_seconds: Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.
        termination_grace_period_seconds: Duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down).
        backoff_limit: Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.
        restart_policy: See model RestartPolicy for more information.
    Example:
        ```python
        AdvancedFlatFields(
            terminate_after_preemption=False,
                        auto_deletion_time_after_completion_seconds=15,
                        termination_grace_period_seconds=20,
                        backoff_limit=3,
                        restart_policy='Always'
        )
        ```
    """  # noqa: E501

    terminate_after_preemption: Optional[StrictBool] = Field(
        default=None,
        description="Indicates if the job should be terminated by the system after it has been preempted.",
        alias="terminateAfterPreemption",
    )
    auto_deletion_time_after_completion_seconds: Optional[StrictInt] = Field(
        default=None,
        description="Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.",
        alias="autoDeletionTimeAfterCompletionSeconds",
    )
    termination_grace_period_seconds: Optional[
        Annotated[int, Field(strict=True, ge=0)]
    ] = Field(
        default=None,
        description="Duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down).",
        alias="terminationGracePeriodSeconds",
    )
    backoff_limit: Optional[StrictInt] = Field(
        default=None,
        description="Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.",
        alias="backoffLimit",
    )
    restart_policy: Optional[RestartPolicy] = Field(default=None, alias="restartPolicy")
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
        """Create an instance of AdvancedFlatFields from a JSON string"""
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
        """Create an instance of AdvancedFlatFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "terminateAfterPreemption": obj.get("terminateAfterPreemption"),
                "autoDeletionTimeAfterCompletionSeconds": obj.get(
                    "autoDeletionTimeAfterCompletionSeconds"
                ),
                "terminationGracePeriodSeconds": obj.get(
                    "terminationGracePeriodSeconds"
                ),
                "backoffLimit": obj.get("backoffLimit"),
                "restartPolicy": obj.get("restartPolicy"),
            }
        )
        return _obj
