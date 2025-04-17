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
from runai.models.compliance_issues_compliance_issues_inner import (
    ComplianceIssuesComplianceIssuesInner,
)
from typing import Optional, Set
from typing_extensions import Self


class ComplianceIssues(BaseModel):
    """
    Pydantic class model representing ComplianceIssues.

    Parameters:
        ```python
        compliance_issues: List[ComplianceIssuesComplianceIssuesInner]
        ```
        compliance_issues: See model List[ComplianceIssuesComplianceIssuesInner] for more information.
    Example:
        ```python
        ComplianceIssues(
            compliance_issues=[
                    runai.models.compliance_issues_compliance_issues_inner.ComplianceIssues_complianceIssues_inner(
                        field = 'compute.gpuDevicesRequest',
                        details = 'value must be no less than 3', )
                    ]
        )
        ```
    """  # noqa: E501

    compliance_issues: Optional[List[ComplianceIssuesComplianceIssuesInner]] = Field(
        default=None, alias="complianceIssues"
    )
    __properties: ClassVar[List[str]] = ["complianceIssues"]

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
        """Create an instance of ComplianceIssues from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in compliance_issues (list)
        _items = []
        if self.compliance_issues:
            for _item_compliance_issues in self.compliance_issues:
                if _item_compliance_issues:
                    _items.append(_item_compliance_issues.to_dict())
            _dict["complianceIssues"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComplianceIssues from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "complianceIssues": (
                    [
                        ComplianceIssuesComplianceIssuesInner.from_dict(_item)
                        for _item in obj["complianceIssues"]
                    ]
                    if obj.get("complianceIssues") is not None
                    else None
                )
            }
        )
        return _obj
