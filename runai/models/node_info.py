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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.gpu_info import GpuInfo
from runai.models.node_status_condition_details import NodeStatusConditionDetails
from runai.models.node_taint import NodeTaint
from typing import Optional, Set
from typing_extensions import Self


class NodeInfo(BaseModel):
    """
    Pydantic class model representing NodeInfo.

    Parameters:
        ```python
        status: str
        conditions: List[NodeStatusConditionDetails]
        taints: List[NodeTaint]
        node_pool: str
        created_at: datetime
        gpu_info: Optional[GpuInfo]
        nv_link_domain_uid: Optional[str]
        nv_link_clique_id: Optional[str]
        ```
        status: The calculated status of the node.
        conditions: See model List[NodeStatusConditionDetails] for more information.
        taints: See model List[NodeTaint] for more information.
        node_pool: The node&#39;s NodePool.
        created_at: See model datetime for more information.
        gpu_info: See model GpuInfo for more information.
        nv_link_domain_uid: NV Link Domain Uid
        nv_link_clique_id: NV Link Clique Id
    Example:
        ```python
        NodeInfo(
            status='Ready',
                        conditions=[
                    runai.models.node_status_condition_details.NodeStatusConditionDetails(
                        type = '',
                        reason = 'KubeletNotReady',
                        message = 'container runtime status check may not have completed yet', )
                    ],
                        taints=[
                    runai.models.node_taint.NodeTaint(
                        key = 'foo',
                        value = 'bar',
                        effect = 'NoSchedule', )
                    ],
                        node_pool='node-pool-1',
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        gpu_info=runai.models.gpu_info.GpuInfo(
                    gpu_type = 'Tesla-V100',
                    gpu_count = 56, ),
                        nv_link_domain_uid='nvlink-domain-uid',
                        nv_link_clique_id='clique-id'
        )
        ```
    """  # noqa: E501

    status: StrictStr = Field(description="The calculated status of the node.")
    conditions: Optional[List[NodeStatusConditionDetails]] = None
    taints: Optional[List[NodeTaint]] = None
    node_pool: StrictStr = Field(description="The node's NodePool.", alias="nodePool")
    created_at: datetime = Field(alias="createdAt")
    gpu_info: Optional[GpuInfo] = Field(default=None, alias="gpuInfo")
    nv_link_domain_uid: Optional[StrictStr] = Field(
        default=None, description="NV Link Domain Uid", alias="nvLinkDomainUid"
    )
    nv_link_clique_id: Optional[StrictStr] = Field(
        default=None, description="NV Link Clique Id", alias="nvLinkCliqueId"
    )
    __properties: ClassVar[List[str]] = [
        "status",
        "conditions",
        "taints",
        "nodePool",
        "createdAt",
        "gpuInfo",
        "nvLinkDomainUid",
        "nvLinkCliqueId",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["Ready", "NotReady", "Unknown"]):
            raise ValueError(
                "must be one of enum values ('Ready', 'NotReady', 'Unknown')"
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
        """Create an instance of NodeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict["conditions"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in taints (list)
        _items = []
        if self.taints:
            for _item_taints in self.taints:
                if _item_taints:
                    _items.append(_item_taints.to_dict())
            _dict["taints"] = _items
        # override the default output from pydantic by calling `to_dict()` of gpu_info
        if self.gpu_info:
            _dict["gpuInfo"] = self.gpu_info.to_dict()
        # set to None if gpu_info (nullable) is None
        # and model_fields_set contains the field
        if self.gpu_info is None and "gpu_info" in self.model_fields_set:
            _dict["gpuInfo"] = None

        # set to None if nv_link_domain_uid (nullable) is None
        # and model_fields_set contains the field
        if (
            self.nv_link_domain_uid is None
            and "nv_link_domain_uid" in self.model_fields_set
        ):
            _dict["nvLinkDomainUid"] = None

        # set to None if nv_link_clique_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.nv_link_clique_id is None
            and "nv_link_clique_id" in self.model_fields_set
        ):
            _dict["nvLinkCliqueId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "status": obj.get("status"),
                "conditions": (
                    [
                        NodeStatusConditionDetails.from_dict(_item)
                        for _item in obj["conditions"]
                    ]
                    if obj.get("conditions") is not None
                    else None
                ),
                "taints": (
                    [NodeTaint.from_dict(_item) for _item in obj["taints"]]
                    if obj.get("taints") is not None
                    else None
                ),
                "nodePool": obj.get("nodePool"),
                "createdAt": obj.get("createdAt"),
                "gpuInfo": (
                    GpuInfo.from_dict(obj["gpuInfo"])
                    if obj.get("gpuInfo") is not None
                    else None
                ),
                "nvLinkDomainUid": obj.get("nvLinkDomainUid"),
                "nvLinkCliqueId": obj.get("nvLinkCliqueId"),
            }
        )
        return _obj
