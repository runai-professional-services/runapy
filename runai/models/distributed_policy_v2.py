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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.distributed_policy_defaults_and_rules_v2 import (
    DistributedPolicyDefaultsAndRulesV2,
)
from runai.models.policy_meta import PolicyMeta
from typing import Optional, Set
from typing_extensions import Self


class DistributedPolicyV2(BaseModel):
    """
    Pydantic class model representing DistributedPolicyV2.

    Parameters:
        ```python
        meta: PolicyMeta
        policy: Optional[DistributedPolicyDefaultsAndRulesV2]
        effective: Optional[DistributedPolicyDefaultsAndRulesV2]
        effective_updated_at: datetime
        ```
        meta: See model PolicyMeta for more information.
        policy: See model DistributedPolicyDefaultsAndRulesV2 for more information.
        effective: See model DistributedPolicyDefaultsAndRulesV2 for more information.
        effective_updated_at: The time at which an event occurred. e.g. the time an effective policy has been updated
    Example:
        ```python
        DistributedPolicyV2(
            meta="example",
                        policy=runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                    defaults = runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                        worker = runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(),
                        master = runai.models.replica_defaults_v2.ReplicaDefaultsV2(), ),
                    rules = runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(),
                    imposed_assets = runai.models.distributed_imposed_assets.DistributedImposedAssets(), ),
                        effective=runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                    defaults = runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                        worker = runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(),
                        master = runai.models.replica_defaults_v2.ReplicaDefaultsV2(), ),
                    rules = runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(),
                    imposed_assets = runai.models.distributed_imposed_assets.DistributedImposedAssets(), ),
                        effective_updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
        )
        ```
    """  # noqa: E501

    meta: Optional[PolicyMeta] = None
    policy: Optional[DistributedPolicyDefaultsAndRulesV2] = None
    effective: Optional[DistributedPolicyDefaultsAndRulesV2] = None
    effective_updated_at: Optional[datetime] = Field(
        default=None,
        description="The time at which an event occurred. e.g. the time an effective policy has been updated",
        alias="effectiveUpdatedAt",
    )
    __properties: ClassVar[List[str]] = [
        "meta",
        "policy",
        "effective",
        "effectiveUpdatedAt",
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
        """Create an instance of DistributedPolicyV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict["policy"] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective
        if self.effective:
            _dict["effective"] = self.effective.to_dict()
        # set to None if policy (nullable) is None
        # and model_fields_set contains the field
        if self.policy is None and "policy" in self.model_fields_set:
            _dict["policy"] = None

        # set to None if effective (nullable) is None
        # and model_fields_set contains the field
        if self.effective is None and "effective" in self.model_fields_set:
            _dict["effective"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistributedPolicyV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "meta": (
                    PolicyMeta.from_dict(obj["meta"])
                    if obj.get("meta") is not None
                    else None
                ),
                "policy": (
                    DistributedPolicyDefaultsAndRulesV2.from_dict(obj["policy"])
                    if obj.get("policy") is not None
                    else None
                ),
                "effective": (
                    DistributedPolicyDefaultsAndRulesV2.from_dict(obj["effective"])
                    if obj.get("effective") is not None
                    else None
                ),
                "effectiveUpdatedAt": obj.get("effectiveUpdatedAt"),
            }
        )
        return _obj
