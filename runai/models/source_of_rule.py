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
from runai.models.scope_type import ScopeType
from typing import Optional, Set
from typing_extensions import Self


class SourceOfRule(BaseModel):
    """
    Pydantic class model representing This field is used by the system along with effective rules, in order to specify the org unit from which this effective rule has been derived. It should be left empty when sending apply policy requests..

    Parameters:
        ```python
        scope: ScopeType
        project_id: Optional[int]
        department_id: Optional[str]
        cluster_id: Optional[str]
        is_fallback: bool
        ```
        scope: See model ScopeType for more information.
        project_id: The id of the project.
        department_id: The id of the department.
        cluster_id: The id of the cluster.
        is_fallback: source of this rule is the fallback policy
    Example:
        ```python
        SourceOfRule(
            scope='system',
                        project_id=1,
                        department_id='2',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        is_fallback=True
        )
        ```
    """  # noqa: E501

    scope: ScopeType
    project_id: Optional[StrictInt] = Field(
        default=None, description="The id of the project.", alias="projectId"
    )
    department_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The id of the department.", alias="departmentId"
    )
    cluster_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The id of the cluster.", alias="clusterId"
    )
    is_fallback: Optional[StrictBool] = Field(
        default=None,
        description="source of this rule is the fallback policy",
        alias="isFallback",
    )
    __properties: ClassVar[List[str]] = [
        "scope",
        "projectId",
        "departmentId",
        "clusterId",
        "isFallback",
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
        """Create an instance of SourceOfRule from a JSON string"""
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
        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict["projectId"] = None

        # set to None if department_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_id is None and "department_id" in self.model_fields_set:
            _dict["departmentId"] = None

        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict["clusterId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceOfRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "scope": obj.get("scope"),
                "projectId": obj.get("projectId"),
                "departmentId": obj.get("departmentId"),
                "clusterId": obj.get("clusterId"),
                "isFallback": obj.get("isFallback"),
            }
        )
        return _obj
