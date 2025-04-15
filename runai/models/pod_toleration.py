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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class PodToleration(BaseModel):
    """
    Pydantic class model representing PodToleration.

    Parameters:
        ```python
        key: str
        operator: str
        value: str
        effect: str
        toleration_seconds: Optional[int]
        ```
        key: Key is the taint key that the toleration applies to. Empty means match all taint keys.
        operator: Operator represents a key&#39;s relationship to the value.
        value: Value is the taint value the toleration matches to.
        effect: Effect indicates the taint effect to match. Empty means match all taint effects.
        toleration_seconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint.
    Example:
        ```python
        PodToleration(
            key='',
                        operator='Exists',
                        value='',
                        effect='NoExecute',
                        toleration_seconds=10
        )
        ```
    """  # noqa: E501

    key: Optional[StrictStr] = Field(
        default=None,
        description="Key is the taint key that the toleration applies to. Empty means match all taint keys.",
    )
    operator: Optional[StrictStr] = Field(
        default=None,
        description="Operator represents a key's relationship to the value.",
    )
    value: Optional[StrictStr] = Field(
        default=None, description="Value is the taint value the toleration matches to."
    )
    effect: Optional[StrictStr] = Field(
        default=None,
        description="Effect indicates the taint effect to match. Empty means match all taint effects.",
    )
    toleration_seconds: Optional[StrictInt] = Field(
        default=None,
        description="TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint.",
        alias="tolerationSeconds",
    )
    __properties: ClassVar[List[str]] = [
        "key",
        "operator",
        "value",
        "effect",
        "tolerationSeconds",
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
        """Create an instance of PodToleration from a JSON string"""
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
        # set to None if toleration_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.toleration_seconds is None
            and "toleration_seconds" in self.model_fields_set
        ):
            _dict["tolerationSeconds"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PodToleration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "key": obj.get("key"),
                "operator": obj.get("operator"),
                "value": obj.get("value"),
                "effect": obj.get("effect"),
                "tolerationSeconds": obj.get("tolerationSeconds"),
            }
        )
        return _obj
