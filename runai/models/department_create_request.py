# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from runai.models.assigned_resources import AssignedResources
from runai.models.node_pool_assigned_resources_create import (
    NodePoolAssignedResourcesCreate,
)
from typing import Optional, Set
from typing_extensions import Self


class DepartmentCreateRequest(BaseModel):
    """
    Pydantic class model representing DepartmentCreateRequest.

    Parameters:
        ```python
        name: str
        deserved_gpus: float
        allow_over_quota: bool
        max_allowed_gpus: float
        resources: AssignedResources
        node_pools_resources: List[NodePoolAssignedResourcesCreate]
        ```
        name: The name of the department.
        deserved_gpus: Deprecated. Instead, use &#x60;deserved&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Deserved GPUs for the department.
        allow_over_quota: Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Is over quota allowed for the department.
        max_allowed_gpus: Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. Max allowed GPUs for the department.
        resources: Deprecated. Instead, use &#39;nodePoolsResources&#39;. Total resources assigned to the Department. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in GET are the sum of all Node Pool Resources.
        node_pools_resources: Resources assigned to this Department per Node Pool
    Example:
        ```python
        DepartmentCreateRequest(
            name='default',
                        deserved_gpus=2,
                        allow_over_quota=False,
                        max_allowed_gpus=2,
                        resources=runai.models.assigned_resources.AssignedResources(
                    id = 1.337,
                    gpu = null,
                    cpu = null,
                    memory = null, ),
                        node_pools_resources=[
                    runai.models.node_pool_assigned_resources_create.NodePoolAssignedResourcesCreate(
                        node_pool = null,
                        gpu = null,
                        cpu = null,
                        memory = null, )
                    ]
        )
        ```
    """  # noqa: E501

    name: StrictStr = Field(description="The name of the department.")
    deserved_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Deprecated. Instead, use `deserved` for the relevant resource type under `NodePoolResources`. Deserved GPUs for the department.",
        alias="deservedGpus",
    )
    allow_over_quota: Optional[StrictBool] = Field(
        default=None,
        description="Deprecated. Instead, use `maxAllowed` for the relevant resource type under `NodePoolResources`. Is over quota allowed for the department.",
        alias="allowOverQuota",
    )
    max_allowed_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Deprecated. Instead, use `maxAllowed` for the relevant resource type under `NodePoolResources`. Max allowed GPUs for the department.",
        alias="maxAllowedGpus",
    )
    resources: Optional[AssignedResources] = Field(
        default=None,
        description="Deprecated. Instead, use 'nodePoolsResources'. Total resources assigned to the Department. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in GET are the sum of all Node Pool Resources.",
    )
    node_pools_resources: Optional[List[NodePoolAssignedResourcesCreate]] = Field(
        default=None,
        description="Resources assigned to this Department per Node Pool",
        alias="nodePoolsResources",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "deservedGpus",
        "allowOverQuota",
        "maxAllowedGpus",
        "resources",
        "nodePoolsResources",
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
        """Create an instance of DepartmentCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict["resources"] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_pools_resources (list)
        _items = []
        if self.node_pools_resources:
            for _item_node_pools_resources in self.node_pools_resources:
                if _item_node_pools_resources:
                    _items.append(_item_node_pools_resources.to_dict())
            _dict["nodePoolsResources"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DepartmentCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "deservedGpus": obj.get("deservedGpus"),
                "allowOverQuota": obj.get("allowOverQuota"),
                "maxAllowedGpus": obj.get("maxAllowedGpus"),
                "resources": (
                    AssignedResources.from_dict(obj["resources"])
                    if obj.get("resources") is not None
                    else None
                ),
                "nodePoolsResources": (
                    [
                        NodePoolAssignedResourcesCreate.from_dict(_item)
                        for _item in obj["nodePoolsResources"]
                    ]
                    if obj.get("nodePoolsResources") is not None
                    else None
                ),
            }
        )
        return _obj
