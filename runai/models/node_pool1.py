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

from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from runai.models.placement_strategy1 import PlacementStrategy1
from typing import Optional, Set
from typing_extensions import Self


class NodePool1(BaseModel):
    """
    Pydantic class model representing NodePool1.

    Parameters:
        ```python
        name: str
        over_provisioning_ratio: int
        label_key: str
        label_value: str
        placement_strategy: PlacementStrategy1
        id: float
        cluster_id: str
        created_at: datetime
        updated_at: datetime
        deleted_at: datetime
        status: str
        status_message: str
        nodes: str
        created_by: str
        updated_by: str
        is_default: bool
        ```
        name: Node Pool Name
        over_provisioning_ratio: See model int for more information. - Default: 1
        label_key: Label key for associated nodes to the Node Pool (with value as in labelValue)
        label_value: Label value for associated nodes to the Node Pool (with key as in labelKey)
        placement_strategy: See model PlacementStrategy1 for more information.
        id: Node Pool unique id
        cluster_id: Node Pool cluster id
        created_at: Node Pool creation time
        updated_at: Node Pool update time
        deleted_at: Node Pool delete time
        status: Node Pool status
        status_message: Node Pool status details
        nodes: List of Nodes that are assigned to this nodepool - as json string
        created_by: Node Pool creator
        updated_by: Node Pool updater
        is_default: Is the Node Pool the default Node Pool for all nodes not assigned to any other Node Pool
    Example:
        ```python
        NodePool1(
            name='node-pool-a',
                        over_provisioning_ratio=1,
                        label_key='node-type',
                        label_value='type-x',
                        placement_strategy=runai.models.placement_strategy1.PlacementStrategy1(
                    cpu = 'spread',
                    gpu = 'binpack', ),
                        id=5,
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        created_at='2021-12-14T16:04:15.099Z',
                        updated_at='2021-12-14T16:04:15.099Z',
                        deleted_at='2021-12-14T16:04:15.099Z',
                        status='Creating',
                        status_message='all nodes are down',
                        nodes='["node-a","node-b"]',
                        created_by='user@run.ai',
                        updated_by='user@run.ai',
                        is_default=False
        )
        ```
    """  # noqa: E501

    name: Optional[StrictStr] = Field(default=None, description="Node Pool Name")
    over_provisioning_ratio: Optional[StrictInt] = Field(
        default=1, alias="overProvisioningRatio"
    )
    label_key: Optional[StrictStr] = Field(
        default=None,
        description="Label key for associated nodes to the Node Pool (with value as in labelValue)",
        alias="labelKey",
    )
    label_value: Optional[StrictStr] = Field(
        default=None,
        description="Label value for associated nodes to the Node Pool (with key as in labelKey)",
        alias="labelValue",
    )
    placement_strategy: Optional[PlacementStrategy1] = Field(
        default=None, alias="placementStrategy"
    )
    id: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Node Pool unique id"
    )
    cluster_id: Optional[StrictStr] = Field(
        default=None, description="Node Pool cluster id", alias="clusterId"
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Node Pool creation time", alias="createdAt"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Node Pool update time", alias="updatedAt"
    )
    deleted_at: Optional[datetime] = Field(
        default=None, description="Node Pool delete time", alias="deletedAt"
    )
    status: Optional[StrictStr] = Field(default=None, description="Node Pool status")
    status_message: Optional[StrictStr] = Field(
        default=None, description="Node Pool status details", alias="statusMessage"
    )
    nodes: Optional[StrictStr] = Field(
        default=None,
        description="List of Nodes that are assigned to this nodepool - as json string",
    )
    created_by: Optional[StrictStr] = Field(
        default=None, description="Node Pool creator", alias="createdBy"
    )
    updated_by: Optional[StrictStr] = Field(
        default=None, description="Node Pool updater", alias="updatedBy"
    )
    is_default: Optional[StrictBool] = Field(
        default=None,
        description="Is the Node Pool the default Node Pool for all nodes not assigned to any other Node Pool",
        alias="isDefault",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "overProvisioningRatio",
        "labelKey",
        "labelValue",
        "placementStrategy",
        "id",
        "clusterId",
        "createdAt",
        "updatedAt",
        "deletedAt",
        "status",
        "statusMessage",
        "nodes",
        "createdBy",
        "updatedBy",
        "isDefault",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "Creating",
                "Updating",
                "Deleting",
                "Empty",
                "Unschedulable",
                "Ready",
                "Deleted",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('Creating', 'Updating', 'Deleting', 'Empty', 'Unschedulable', 'Ready', 'Deleted')"
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
        """Create an instance of NodePool1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of placement_strategy
        if self.placement_strategy:
            _dict["placementStrategy"] = self.placement_strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodePool1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "overProvisioningRatio": (
                    obj.get("overProvisioningRatio")
                    if obj.get("overProvisioningRatio") is not None
                    else 1
                ),
                "labelKey": obj.get("labelKey"),
                "labelValue": obj.get("labelValue"),
                "placementStrategy": (
                    PlacementStrategy1.from_dict(obj["placementStrategy"])
                    if obj.get("placementStrategy") is not None
                    else None
                ),
                "id": obj.get("id"),
                "clusterId": obj.get("clusterId"),
                "createdAt": obj.get("createdAt"),
                "updatedAt": obj.get("updatedAt"),
                "deletedAt": obj.get("deletedAt"),
                "status": obj.get("status"),
                "statusMessage": obj.get("statusMessage"),
                "nodes": obj.get("nodes"),
                "createdBy": obj.get("createdBy"),
                "updatedBy": obj.get("updatedBy"),
                "isDefault": obj.get("isDefault"),
            }
        )
        return _obj
