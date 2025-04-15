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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.phase import Phase
from runai.models.workload_desired_phase import WorkloadDesiredPhase
from typing import Optional, Set
from typing_extensions import Self


class WorkloadMeta1(BaseModel):
    """
    Pydantic class model representing WorkloadMeta1.

    Parameters:
        ```python
        name: str
        requested_name: str
        workload_id: str
        project_id: str
        department_id: str
        cluster_id: str
        created_by: str
        created_at: datetime
        deleted_at: Optional[datetime]
        desired_phase: WorkloadDesiredPhase
        actual_phase: Phase
        ```
        name: The name of the workload.
        requested_name: The name as was requested for the workload. If useGivenNameAsPrefix, in the creation request, is false, name and requestedName should be identical. Otherwise, name should be composed of requestedName followed by a suffix of random characters.
        workload_id: A unique ID of the workload.
        project_id: The id of the project.
        department_id: The id of the department.
        cluster_id: The id of the cluster.
        created_by: The user who created the workload
        created_at: The creation time of the workload.
        deleted_at: The deletion time of the workload.
        desired_phase: See model WorkloadDesiredPhase for more information.
        actual_phase: See model Phase for more information.
    Example:
        ```python
        WorkloadMeta1(
            name='my-workload-name',
                        requested_name='',
                        workload_id='',
                        project_id='1',
                        department_id='2',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        created_by='test@lab.com',
                        created_at='2022-01-01T03:49:52.531Z',
                        deleted_at='2022-01-01T03:49:52.531Z',
                        desired_phase='Running',
                        actual_phase='Creating'
        )
        ```
    """  # noqa: E501

    name: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The name of the workload."
    )
    requested_name: StrictStr = Field(
        description="The name as was requested for the workload. If useGivenNameAsPrefix, in the creation request, is false, name and requestedName should be identical. Otherwise, name should be composed of requestedName followed by a suffix of random characters.",
        alias="requestedName",
    )
    workload_id: StrictStr = Field(
        description="A unique ID of the workload.", alias="workloadId"
    )
    project_id: StrictStr = Field(
        description="The id of the project.", alias="projectId"
    )
    department_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The id of the department.", alias="departmentId"
    )
    cluster_id: StrictStr = Field(
        description="The id of the cluster.", alias="clusterId"
    )
    created_by: StrictStr = Field(
        description="The user who created the workload", alias="createdBy"
    )
    created_at: datetime = Field(
        description="The creation time of the workload.", alias="createdAt"
    )
    deleted_at: Optional[datetime] = Field(
        default=None,
        description="The deletion time of the workload.",
        alias="deletedAt",
    )
    desired_phase: WorkloadDesiredPhase = Field(alias="desiredPhase")
    actual_phase: Optional[Phase] = Field(default=None, alias="actualPhase")
    __properties: ClassVar[List[str]] = [
        "name",
        "requestedName",
        "workloadId",
        "projectId",
        "departmentId",
        "clusterId",
        "createdBy",
        "createdAt",
        "deletedAt",
        "desiredPhase",
        "actualPhase",
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
        """Create an instance of WorkloadMeta1 from a JSON string"""
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
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict["deletedAt"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadMeta1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "requestedName": obj.get("requestedName"),
                "workloadId": obj.get("workloadId"),
                "projectId": obj.get("projectId"),
                "departmentId": obj.get("departmentId"),
                "clusterId": obj.get("clusterId"),
                "createdBy": obj.get("createdBy"),
                "createdAt": obj.get("createdAt"),
                "deletedAt": obj.get("deletedAt"),
                "desiredPhase": obj.get("desiredPhase"),
                "actualPhase": obj.get("actualPhase"),
            }
        )
        return _obj
