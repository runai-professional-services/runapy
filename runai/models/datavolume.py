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
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.datavolume_status import DatavolumeStatus
from runai.models.shared_scope import SharedScope
from typing import Optional, Set
from typing_extensions import Self


class Datavolume(BaseModel):
    """
    Pydantic class model representing Datavolume.

    Parameters:
        ```python
        id: str
        created_at: datetime
        updated_at: datetime
        created_by: str
        updated_by: str
        name: str
        description: str
        origin_pvc_name: str
        project_id: str
        should_delete_original_volume: bool
        project_name: str
        department_id: str
        cluster_id: str
        shared_scopes: List[SharedScope]
        status: DatavolumeStatus
        ```
        id: See model str for more information.
        created_at: See model datetime for more information.
        updated_at: See model datetime for more information.
        created_by: See model str for more information.
        updated_by: See model str for more information.
        name: See model str for more information.
        description: See model str for more information.
        origin_pvc_name: The name of the PVC that the datavolume is based on
        project_id: The ID of the project that in its namespace the origin pvc is located
        should_delete_original_volume: If true, the original storage volume will be deleted together with the datavolume - Default: False
        project_name: See model str for more information.
        department_id: See model str for more information.
        cluster_id: The id of the cluster.
        shared_scopes: Will be returned only if the user has the required permissions to view those scopes
        status: See model DatavolumeStatus for more information.
    Example:
        ```python
        Datavolume(
            id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        created_by='user@run.ai',
                        updated_by='user@run.ai',
                        name='datavolume-a',
                        description='Results of experiment X',
                        origin_pvc_name='pvc-a',
                        project_id='5',
                        should_delete_original_volume=False,
                        project_name='project-a',
                        department_id='department-a',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        shared_scopes=[
                    null
                    ],
                        status=runai.models.datavolume_status.DatavolumeStatus(
                    phase = 'Ready',
                    phase_message = 'Failed to copy pvc to project 'project-a'',
                    conditions = [
                        runai.models.condition1.Condition1(
                            type = 'PvcsCreated',
                            status = 'False',
                            message = 'Failed to create pvc in namespace 'runai-proj1'',
                            reason = 'ErrorCreatingPvc',
                            last_transition_time = '2022-01-01T03:49:52.531Z', )
                        ],
                    datavolume_pvc_name = 'datavolume-pvc-1',
                    datavolume_pv_name = 'datavolume-pv-1', )
        )
        ```
    """  # noqa: E501

    id: StrictStr
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    updated_by: Optional[StrictStr] = Field(default=None, alias="updatedBy")
    name: Annotated[str, Field(strict=True, max_length=63)]
    description: Optional[Annotated[str, Field(strict=True, max_length=127)]] = None
    origin_pvc_name: StrictStr = Field(
        description="The name of the PVC that the datavolume is based on",
        alias="originPvcName",
    )
    project_id: StrictStr = Field(
        description="The ID of the project that in its namespace the origin pvc is located",
        alias="projectId",
    )
    should_delete_original_volume: Optional[StrictBool] = Field(
        default=False,
        description="If true, the original storage volume will be deleted together with the datavolume",
        alias="shouldDeleteOriginalVolume",
    )
    project_name: StrictStr = Field(alias="projectName")
    department_id: Optional[StrictStr] = Field(default=None, alias="departmentId")
    cluster_id: Optional[StrictStr] = Field(
        default=None, description="The id of the cluster.", alias="clusterId"
    )
    shared_scopes: Optional[List[SharedScope]] = Field(
        default=None,
        description="Will be returned only if the user has the required permissions to view those scopes",
        alias="sharedScopes",
    )
    status: DatavolumeStatus
    __properties: ClassVar[List[str]] = [
        "id",
        "createdAt",
        "updatedAt",
        "createdBy",
        "updatedBy",
        "name",
        "description",
        "originPvcName",
        "projectId",
        "shouldDeleteOriginalVolume",
        "projectName",
        "departmentId",
        "clusterId",
        "sharedScopes",
        "status",
    ]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][-a-z0-9]{0,62}$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-z][-a-z0-9]{0,62}$/"
            )
        return value

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
        """Create an instance of Datavolume from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shared_scopes (list)
        _items = []
        if self.shared_scopes:
            for _item_shared_scopes in self.shared_scopes:
                if _item_shared_scopes:
                    _items.append(_item_shared_scopes.to_dict())
            _dict["sharedScopes"] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Datavolume from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
                "createdBy": obj.get("createdBy"),
                "updatedBy": obj.get("updatedBy"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "originPvcName": obj.get("originPvcName"),
                "projectId": obj.get("projectId"),
                "shouldDeleteOriginalVolume": (
                    obj.get("shouldDeleteOriginalVolume")
                    if obj.get("shouldDeleteOriginalVolume") is not None
                    else False
                ),
                "projectName": obj.get("projectName"),
                "departmentId": obj.get("departmentId"),
                "clusterId": obj.get("clusterId"),
                "sharedScopes": (
                    [SharedScope.from_dict(_item) for _item in obj["sharedScopes"]]
                    if obj.get("sharedScopes") is not None
                    else None
                ),
                "status": (
                    DatavolumeStatus.from_dict(obj["status"])
                    if obj.get("status") is not None
                    else None
                ),
            }
        )
        return _obj
