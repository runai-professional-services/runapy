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
from typing_extensions import Annotated
from runai.models.probe_handler import ProbeHandler
from typing import Optional, Set
from typing_extensions import Self


class Probe(BaseModel):
    """
    Pydantic class model representing Probe.

    Parameters:
        ```python
        initial_delay_seconds: Optional[int]
        period_seconds: Optional[int]
        timeout_seconds: Optional[int]
        success_threshold: Optional[int]
        failure_threshold: Optional[int]
        handler: Optional[ProbeHandler]
        ```
        initial_delay_seconds: Number of seconds after the container has started before liveness or readiness probes are initiated.
        period_seconds: How often (in seconds) to perform the probe.
        timeout_seconds: Number of seconds after which the probe times out.
        success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed.
        failure_threshold: When a probe fails, the number of times to try before giving up.
        handler: See model ProbeHandler for more information.
    Example:
        ```python
        Probe(
            initial_delay_seconds=0,
                        period_seconds=1,
                        timeout_seconds=1,
                        success_threshold=1,
                        failure_threshold=1,
                        handler=runai.models.probe_handler.ProbeHandler(
                    http_get = runai.models.probe_handler_http_get.ProbeHandler_httpGet(
                        path = '/',
                        port = 1,
                        host = 'example.com',
                        scheme = 'HTTP', ), )
        )
        ```
    """  # noqa: E501

    initial_delay_seconds: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="Number of seconds after the container has started before liveness or readiness probes are initiated.",
        alias="initialDelaySeconds",
    )
    period_seconds: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="How often (in seconds) to perform the probe.",
        alias="periodSeconds",
    )
    timeout_seconds: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="Number of seconds after which the probe times out.",
        alias="timeoutSeconds",
    )
    success_threshold: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="Minimum consecutive successes for the probe to be considered successful after having failed.",
        alias="successThreshold",
    )
    failure_threshold: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="When a probe fails, the number of times to try before giving up.",
        alias="failureThreshold",
    )
    handler: Optional[ProbeHandler] = None
    __properties: ClassVar[List[str]] = [
        "initialDelaySeconds",
        "periodSeconds",
        "timeoutSeconds",
        "successThreshold",
        "failureThreshold",
        "handler",
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
        """Create an instance of Probe from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of handler
        if self.handler:
            _dict["handler"] = self.handler.to_dict()
        # set to None if initial_delay_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.initial_delay_seconds is None
            and "initial_delay_seconds" in self.model_fields_set
        ):
            _dict["initialDelaySeconds"] = None

        # set to None if period_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.period_seconds is None and "period_seconds" in self.model_fields_set:
            _dict["periodSeconds"] = None

        # set to None if timeout_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.timeout_seconds is None and "timeout_seconds" in self.model_fields_set:
            _dict["timeoutSeconds"] = None

        # set to None if success_threshold (nullable) is None
        # and model_fields_set contains the field
        if (
            self.success_threshold is None
            and "success_threshold" in self.model_fields_set
        ):
            _dict["successThreshold"] = None

        # set to None if failure_threshold (nullable) is None
        # and model_fields_set contains the field
        if (
            self.failure_threshold is None
            and "failure_threshold" in self.model_fields_set
        ):
            _dict["failureThreshold"] = None

        # set to None if handler (nullable) is None
        # and model_fields_set contains the field
        if self.handler is None and "handler" in self.model_fields_set:
            _dict["handler"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Probe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "initialDelaySeconds": obj.get("initialDelaySeconds"),
                "periodSeconds": obj.get("periodSeconds"),
                "timeoutSeconds": obj.get("timeoutSeconds"),
                "successThreshold": obj.get("successThreshold"),
                "failureThreshold": obj.get("failureThreshold"),
                "handler": (
                    ProbeHandler.from_dict(obj["handler"])
                    if obj.get("handler") is not None
                    else None
                ),
            }
        )
        return _obj
