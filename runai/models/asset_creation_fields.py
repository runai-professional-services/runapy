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
from runai.models.scope import Scope
from runai.models.workload_supported_types import WorkloadSupportedTypes
from typing import Optional, Set
from typing_extensions import Self


class AssetCreationFields(BaseModel):
    """
    Pydantic class model representing AssetCreationFields.

    Parameters:
        ```python
        scope: Scope
        cluster_id: Optional[str]
        department_id: Optional[str]
        project_id: Optional[int]
        auto_delete: Optional[bool]
        workload_supported_types: Optional[WorkloadSupportedTypes]
        ```
        scope: See model Scope for more information.
        cluster_id: The id of the cluster.
        department_id: The id of the department. Must be specified for department scoped assets.
        project_id: The id of the project. Must be specified for project scoped assets.
        auto_delete: The asset will be deleted automatically. This is intended for internal use. - Default: False
        workload_supported_types: See model WorkloadSupportedTypes for more information.
    Example:
        ```python
        AssetCreationFields(
            scope='system',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        department_id='0',
                        project_id=56,
                        auto_delete=True,
                        workload_supported_types=runai.models.workload_supported_types.WorkloadSupportedTypes(
                    inference = True,
                    workspace = True,
                    training = True,
                    distributed = True,
                    dist_framework = 'MPI', )
        )
        ```
    """  # noqa: E501

    scope: Scope
    cluster_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The id of the cluster.", alias="clusterId"
    )
    department_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="The id of the department. Must be specified for department scoped assets.",
        alias="departmentId",
    )
    project_id: Optional[StrictInt] = Field(
        default=None,
        description="The id of the project. Must be specified for project scoped assets.",
        alias="projectId",
    )
    auto_delete: Optional[StrictBool] = Field(
        default=False,
        description="The asset will be deleted automatically. This is intended for internal use.",
        alias="autoDelete",
    )
    workload_supported_types: Optional[WorkloadSupportedTypes] = Field(
        default=None, alias="workloadSupportedTypes"
    )
    __properties: ClassVar[List[str]] = [
        "scope",
        "clusterId",
        "departmentId",
        "projectId",
        "autoDelete",
        "workloadSupportedTypes",
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
        """Create an instance of AssetCreationFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workload_supported_types
        if self.workload_supported_types:
            _dict["workloadSupportedTypes"] = self.workload_supported_types.to_dict()
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict["clusterId"] = None

        # set to None if department_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_id is None and "department_id" in self.model_fields_set:
            _dict["departmentId"] = None

        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict["projectId"] = None

        # set to None if auto_delete (nullable) is None
        # and model_fields_set contains the field
        if self.auto_delete is None and "auto_delete" in self.model_fields_set:
            _dict["autoDelete"] = None

        # set to None if workload_supported_types (nullable) is None
        # and model_fields_set contains the field
        if (
            self.workload_supported_types is None
            and "workload_supported_types" in self.model_fields_set
        ):
            _dict["workloadSupportedTypes"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetCreationFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "scope": obj.get("scope"),
                "clusterId": obj.get("clusterId"),
                "departmentId": obj.get("departmentId"),
                "projectId": obj.get("projectId"),
                "autoDelete": (
                    obj.get("autoDelete")
                    if obj.get("autoDelete") is not None
                    else False
                ),
                "workloadSupportedTypes": (
                    WorkloadSupportedTypes.from_dict(obj["workloadSupportedTypes"])
                    if obj.get("workloadSupportedTypes") is not None
                    else None
                ),
            }
        )
        return _obj
