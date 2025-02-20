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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.policy_creation_fields import PolicyCreationFields
from runai.models.training_policy_defaults_and_rules_v2 import (
    TrainingPolicyDefaultsAndRulesV2,
)
from typing import Optional, Set
from typing_extensions import Self


class TrainingPolicyChangeRequestV2(BaseModel):
    """
    Pydantic class model representing TrainingPolicyChangeRequestV2.

    Parameters:
        ```python
        meta: PolicyCreationFields
        policy: Optional[TrainingPolicyDefaultsAndRulesV2]
        reset: List[str]
        ```
        meta: See model PolicyCreationFields for more information.
        policy: See model TrainingPolicyDefaultsAndRulesV2 for more information.
        reset: set of fields in jsonpath format that is requested to clear their policy (default and rules)
    Example:
        ```python
        TrainingPolicyChangeRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system',
                    project_id = 1,
                    department_id = '2',
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
                    name = 'my-policy', ),
                        policy=runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                    defaults = runai.models.training_policy_defaults_and_rules_v2_defaults.TrainingPolicyDefaultsAndRulesV2_defaults(),
                    rules = runai.models.rules.rules(),
                    imposed_assets = [
                        ''
                        ], ),
                        reset=["security.runAsGpu","compute.gpu"]
        )
        ```
    """  # noqa: E501

    meta: Optional[PolicyCreationFields] = None
    policy: Optional[TrainingPolicyDefaultsAndRulesV2] = None
    reset: Optional[List[StrictStr]] = Field(
        default=None,
        description="set of fields in jsonpath format that is requested to clear their policy (default and rules)",
    )
    __properties: ClassVar[List[str]] = ["meta", "policy", "reset"]

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
        """Create an instance of TrainingPolicyChangeRequestV2 from a JSON string"""
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
        # set to None if policy (nullable) is None
        # and model_fields_set contains the field
        if self.policy is None and "policy" in self.model_fields_set:
            _dict["policy"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrainingPolicyChangeRequestV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "meta": (
                    PolicyCreationFields.from_dict(obj["meta"])
                    if obj.get("meta") is not None
                    else None
                ),
                "policy": (
                    TrainingPolicyDefaultsAndRulesV2.from_dict(obj["policy"])
                    if obj.get("policy") is not None
                    else None
                ),
                "reset": obj.get("reset"),
            }
        )
        return _obj
