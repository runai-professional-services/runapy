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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.asset_datasource_ref import AssetDatasourceRef
from runai.models.asset_ref import AssetRef
from runai.models.assets_usage_ref_compute import AssetsUsageRefCompute
from runai.models.environment_asset_ref import EnvironmentAssetRef
from typing import Optional, Set
from typing_extensions import Self


class AssetsUsageRef(BaseModel):
    """
    Pydantic class model representing Reference information about usage of assets by other assets, for example datasources that uses credentials..

    Parameters:
        ```python
        environment: Optional[EnvironmentAssetRef]
        environments: List[AssetRef]
        compute: Optional[AssetsUsageRefCompute]
        computes: List[AssetRef]
        datasources: List[AssetDatasourceRef]
        ```
        environment: environment asset.
        environments: See model List[AssetRef] for more information.
        compute: See model AssetsUsageRefCompute for more information.
        computes: See model List[AssetRef] for more information.
        datasources: See model List[AssetDatasourceRef] for more information.
    Example:
        ```python
        AssetsUsageRef(
            environment=runai.models.environment_asset_ref.EnvironmentAssetRef(
                    id = '0',
                    name = 'my-asset',
                    tool_types = [
                        'jupyter-notebook'
                        ], ),
                        environments=[
                    runai.models.asset_ref.AssetRef(
                        id = '0',
                        name = 'my-asset', )
                    ],
                        compute=runai.models.assets_usage_ref_compute.AssetsUsageRefCompute(),
                        computes=[
                    runai.models.asset_ref.AssetRef(
                        id = '0',
                        name = 'my-asset', )
                    ],
                        datasources=[
                    runai.models.asset_datasource_ref.AssetDatasourceRef(
                        id = '0',
                        name = 'my-asset',
                        kind = 'compute',
                        overrides = runai.models.data_source_overrides.DataSourceOverrides(
                            container_path = '/container/directory', ), )
                    ]
        )
        ```
    """  # noqa: E501

    environment: Optional[EnvironmentAssetRef] = Field(
        default=None, description="environment asset."
    )
    environments: Optional[List[AssetRef]] = None
    compute: Optional[AssetsUsageRefCompute] = None
    computes: Optional[List[AssetRef]] = None
    datasources: Optional[List[AssetDatasourceRef]] = None
    __properties: ClassVar[List[str]] = [
        "environment",
        "environments",
        "compute",
        "computes",
        "datasources",
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
        """Create an instance of AssetsUsageRef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict["environment"] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in environments (list)
        _items = []
        if self.environments:
            for _item_environments in self.environments:
                if _item_environments:
                    _items.append(_item_environments.to_dict())
            _dict["environments"] = _items
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict["compute"] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in computes (list)
        _items = []
        if self.computes:
            for _item_computes in self.computes:
                if _item_computes:
                    _items.append(_item_computes.to_dict())
            _dict["computes"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in datasources (list)
        _items = []
        if self.datasources:
            for _item_datasources in self.datasources:
                if _item_datasources:
                    _items.append(_item_datasources.to_dict())
            _dict["datasources"] = _items
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict["environment"] = None

        # set to None if compute (nullable) is None
        # and model_fields_set contains the field
        if self.compute is None and "compute" in self.model_fields_set:
            _dict["compute"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetsUsageRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "environment": (
                    EnvironmentAssetRef.from_dict(obj["environment"])
                    if obj.get("environment") is not None
                    else None
                ),
                "environments": (
                    [AssetRef.from_dict(_item) for _item in obj["environments"]]
                    if obj.get("environments") is not None
                    else None
                ),
                "compute": (
                    AssetsUsageRefCompute.from_dict(obj["compute"])
                    if obj.get("compute") is not None
                    else None
                ),
                "computes": (
                    [AssetRef.from_dict(_item) for _item in obj["computes"]]
                    if obj.get("computes") is not None
                    else None
                ),
                "datasources": (
                    [
                        AssetDatasourceRef.from_dict(_item)
                        for _item in obj["datasources"]
                    ]
                    if obj.get("datasources") is not None
                    else None
                ),
            }
        )
        return _obj
