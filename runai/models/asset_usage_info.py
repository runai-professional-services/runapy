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
from runai.models.asset_ref import AssetRef
from runai.models.assets_usage_ref import AssetsUsageRef
from runai.models.workload_ref_and_status import WorkloadRefAndStatus
from typing import Optional, Set
from typing_extensions import Self


class AssetUsageInfo(BaseModel):
    """
    Pydantic class model representing Details about resources that use the asset..

    Parameters:
        ```python
        workspaces: List[WorkloadRefAndStatus]
        trainings: List[WorkloadRefAndStatus]
        distributed: List[WorkloadRefAndStatus]
        inferences: List[WorkloadRefAndStatus]
        templates: List[AssetRef]
        assets: AssetsUsageRef
        ```
        workspaces: workspaces that rely on this asset.
        trainings: trainings that rely on this asset.
        distributed: distributed trainings that rely on this asset.
        inferences: inferences that rely on this asset.
        templates: templates that rely on this asset.
        assets: See model AssetsUsageRef for more information.
    Example:
        ```python
        AssetUsageInfo(
            workspaces=[
                    runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                        id = '',
                        name = 'my-workload-name',
                        status = '0', )
                    ],
                        trainings=[
                    runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                        id = '',
                        name = 'my-workload-name',
                        status = '0', )
                    ],
                        distributed=[
                    runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                        id = '',
                        name = 'my-workload-name',
                        status = '0', )
                    ],
                        inferences=[
                    runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                        id = '',
                        name = 'my-workload-name',
                        status = '0', )
                    ],
                        templates=[
                    runai.models.asset_ref.AssetRef(
                        id = '0',
                        name = 'my-asset', )
                    ],
                        assets=runai.models.assets_usage_ref.AssetsUsageRef(
                    environment = runai.models.environment.environment(),
                    environments = [
                        runai.models.asset_ref.AssetRef(
                            id = '0',
                            name = 'my-asset', )
                        ],
                    compute = runai.models.assets_usage_ref_compute.AssetsUsageRefCompute(),
                    computes = [
                        runai.models.asset_ref.AssetRef(
                            id = '0',
                            name = 'my-asset', )
                        ],
                    datasources = [
                        runai.models.asset_datasource_ref.AssetDatasourceRef(
                            id = '0',
                            name = 'my-asset',
                            kind = 'compute',
                            overrides = runai.models.data_source_overrides.DataSourceOverrides(
                                container_path = '/container/directory', ), )
                        ], )
        )
        ```
    """  # noqa: E501

    workspaces: Optional[List[WorkloadRefAndStatus]] = Field(
        default=None, description="workspaces that rely on this asset."
    )
    trainings: Optional[List[WorkloadRefAndStatus]] = Field(
        default=None, description="trainings that rely on this asset."
    )
    distributed: Optional[List[WorkloadRefAndStatus]] = Field(
        default=None, description="distributed trainings that rely on this asset."
    )
    inferences: Optional[List[WorkloadRefAndStatus]] = Field(
        default=None, description="inferences that rely on this asset."
    )
    templates: Optional[List[AssetRef]] = Field(
        default=None, description="templates that rely on this asset."
    )
    assets: Optional[AssetsUsageRef] = None
    __properties: ClassVar[List[str]] = [
        "workspaces",
        "trainings",
        "distributed",
        "inferences",
        "templates",
        "assets",
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
        """Create an instance of AssetUsageInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in workspaces (list)
        _items = []
        if self.workspaces:
            for _item_workspaces in self.workspaces:
                if _item_workspaces:
                    _items.append(_item_workspaces.to_dict())
            _dict["workspaces"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trainings (list)
        _items = []
        if self.trainings:
            for _item_trainings in self.trainings:
                if _item_trainings:
                    _items.append(_item_trainings.to_dict())
            _dict["trainings"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in distributed (list)
        _items = []
        if self.distributed:
            for _item_distributed in self.distributed:
                if _item_distributed:
                    _items.append(_item_distributed.to_dict())
            _dict["distributed"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inferences (list)
        _items = []
        if self.inferences:
            for _item_inferences in self.inferences:
                if _item_inferences:
                    _items.append(_item_inferences.to_dict())
            _dict["inferences"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in templates (list)
        _items = []
        if self.templates:
            for _item_templates in self.templates:
                if _item_templates:
                    _items.append(_item_templates.to_dict())
            _dict["templates"] = _items
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict["assets"] = self.assets.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetUsageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "workspaces": (
                    [
                        WorkloadRefAndStatus.from_dict(_item)
                        for _item in obj["workspaces"]
                    ]
                    if obj.get("workspaces") is not None
                    else None
                ),
                "trainings": (
                    [
                        WorkloadRefAndStatus.from_dict(_item)
                        for _item in obj["trainings"]
                    ]
                    if obj.get("trainings") is not None
                    else None
                ),
                "distributed": (
                    [
                        WorkloadRefAndStatus.from_dict(_item)
                        for _item in obj["distributed"]
                    ]
                    if obj.get("distributed") is not None
                    else None
                ),
                "inferences": (
                    [
                        WorkloadRefAndStatus.from_dict(_item)
                        for _item in obj["inferences"]
                    ]
                    if obj.get("inferences") is not None
                    else None
                ),
                "templates": (
                    [AssetRef.from_dict(_item) for _item in obj["templates"]]
                    if obj.get("templates") is not None
                    else None
                ),
                "assets": (
                    AssetsUsageRef.from_dict(obj["assets"])
                    if obj.get("assets") is not None
                    else None
                ),
            }
        )
        return _obj
