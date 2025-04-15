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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.node_types_per_workload import NodeTypesPerWorkload
from runai.models.overtime_data import OvertimeData
from runai.models.resources import Resources
from runai.models.scheduling_rules import SchedulingRules
from typing import Optional, Set
from typing_extensions import Self


class DataDepartmentFields(BaseModel):
    """
    Pydantic class model representing DataDepartmentFields.

    Parameters:
        ```python
        description: str
        resources: List[Resources]
        scheduling_rules: Optional[SchedulingRules]
        default_node_pools: Optional[List[str]]
        node_types: NodeTypesPerWorkload
        name: str
        cluster_id: str
        overtime_data: OvertimeData
        ```
        description: department&#39;s description
        resources: Resources assigned to this Organization per Node Pool
        scheduling_rules: See model SchedulingRules for more information.
        default_node_pools: default order of node pools for workloads. will be enforced if no list is defined in workload policy
        node_types: See model NodeTypesPerWorkload for more information.
        name: See model str for more information.
        cluster_id: The id of the cluster.
        overtime_data: See model OvertimeData for more information.
    Example:
        ```python
        DataDepartmentFields(
            description='',
                        resources=[
                    runai.models.resources.Resources(
                        node_pool = runai.models.resources_node_pool.Resources_nodePool(
                            id = '22',
                            name = 'default', ),
                        gpu = null,
                        cpu = runai.models.resources_cpu.Resources_cpu(),
                        memory = runai.models.resources_memory.Resources_memory(),
                        priority = 'Normal', )
                    ],
                        scheduling_rules=runai.models.scheduling_rules.SchedulingRules(
                    interactive_job_time_limit_seconds = 100,
                    interactive_job_max_idle_duration_seconds = 100,
                    interactive_job_preempt_idle_duration_seconds = 100,
                    training_job_max_idle_duration_seconds = 100,
                    training_job_time_limit_seconds = 100, ),
                        default_node_pools=[
                    ''
                    ],
                        node_types=runai.models.node_types_per_workload.NodeTypesPerWorkload(
                    training = [
                        ''
                        ],
                    workspace = [
                        ''
                        ],
                    names = {
                        'key' : ''
                        }, ),
                        name='organization1',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        overtime_data=runai.models.overtime_data.OvertimeData(
                    range24h_data = runai.models.range24h_data.range24hData(),
                    range7d_data = runai.models.range7d_data.range7dData(),
                    range30d_data = runai.models.range30d_data.range30dData(), )
        )
        ```
    """  # noqa: E501

    description: Optional[StrictStr] = Field(
        default=None, description="department's description"
    )
    resources: List[Resources] = Field(
        description="Resources assigned to this Organization per Node Pool"
    )
    scheduling_rules: Optional[SchedulingRules] = Field(
        default=None, alias="schedulingRules"
    )
    default_node_pools: Optional[List[StrictStr]] = Field(
        default=None,
        description="default order of node pools for workloads. will be enforced if no list is defined in workload policy",
        alias="defaultNodePools",
    )
    node_types: Optional[NodeTypesPerWorkload] = Field(default=None, alias="nodeTypes")
    name: StrictStr
    cluster_id: StrictStr = Field(
        description="The id of the cluster.", alias="clusterId"
    )
    overtime_data: Optional[OvertimeData] = Field(default=None, alias="overtimeData")
    __properties: ClassVar[List[str]] = [
        "description",
        "resources",
        "schedulingRules",
        "defaultNodePools",
        "nodeTypes",
        "name",
        "clusterId",
        "overtimeData",
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
        """Create an instance of DataDepartmentFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict["resources"] = _items
        # override the default output from pydantic by calling `to_dict()` of scheduling_rules
        if self.scheduling_rules:
            _dict["schedulingRules"] = self.scheduling_rules.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_types
        if self.node_types:
            _dict["nodeTypes"] = self.node_types.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overtime_data
        if self.overtime_data:
            _dict["overtimeData"] = self.overtime_data.to_dict()
        # set to None if scheduling_rules (nullable) is None
        # and model_fields_set contains the field
        if (
            self.scheduling_rules is None
            and "scheduling_rules" in self.model_fields_set
        ):
            _dict["schedulingRules"] = None

        # set to None if default_node_pools (nullable) is None
        # and model_fields_set contains the field
        if (
            self.default_node_pools is None
            and "default_node_pools" in self.model_fields_set
        ):
            _dict["defaultNodePools"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataDepartmentFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "resources": (
                    [Resources.from_dict(_item) for _item in obj["resources"]]
                    if obj.get("resources") is not None
                    else None
                ),
                "schedulingRules": (
                    SchedulingRules.from_dict(obj["schedulingRules"])
                    if obj.get("schedulingRules") is not None
                    else None
                ),
                "defaultNodePools": obj.get("defaultNodePools"),
                "nodeTypes": (
                    NodeTypesPerWorkload.from_dict(obj["nodeTypes"])
                    if obj.get("nodeTypes") is not None
                    else None
                ),
                "name": obj.get("name"),
                "clusterId": obj.get("clusterId"),
                "overtimeData": (
                    OvertimeData.from_dict(obj["overtimeData"])
                    if obj.get("overtimeData") is not None
                    else None
                ),
            }
        )
        return _obj
