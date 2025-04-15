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
from typing_extensions import Annotated
from runai.models.asset_id_and_kind import AssetIdAndKind
from typing import Optional, Set
from typing_extensions import Self


class AssetsIds(BaseModel):
    """
    Pydantic class model representing Set of assets comprising a workspace or a workspace template..

    Parameters:
        ```python
        environment: str
        compute: Optional[str]
        datasources: List[AssetIdAndKind]
        workload_volumes: List[str]
        ```
        environment: Unique identifier of the asset.
        compute: Unique identifier of the asset.
        datasources: See model List[AssetIdAndKind] for more information.
        workload_volumes: See model List[str] for more information.
    Example:
        ```python
        AssetsIds(
            environment='0',
                        compute='0',
                        datasources=[
                    runai.models.asset_id_and_kind.AssetIdAndKind(
                        id = '0',
                        kind = 'compute',
                        overrides = runai.models.data_source_overrides.DataSourceOverrides(
                            container_path = '/container/directory', ), )
                    ],
                        workload_volumes=[
                    ''
                    ]
        )
        ```
    """  # noqa: E501

    environment: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="Unique identifier of the asset."
    )
    compute: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="Unique identifier of the asset."
    )
    datasources: Optional[List[AssetIdAndKind]] = None
    workload_volumes: Optional[List[StrictStr]] = Field(
        default=None, alias="workloadVolumes"
    )
    __properties: ClassVar[List[str]] = [
        "environment",
        "compute",
        "datasources",
        "workloadVolumes",
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
        """Create an instance of AssetsIds from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in datasources (list)
        _items = []
        if self.datasources:
            for _item_datasources in self.datasources:
                if _item_datasources:
                    _items.append(_item_datasources.to_dict())
            _dict["datasources"] = _items
        # set to None if compute (nullable) is None
        # and model_fields_set contains the field
        if self.compute is None and "compute" in self.model_fields_set:
            _dict["compute"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetsIds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "environment": obj.get("environment"),
                "compute": obj.get("compute"),
                "datasources": (
                    [AssetIdAndKind.from_dict(_item) for _item in obj["datasources"]]
                    if obj.get("datasources") is not None
                    else None
                ),
                "workloadVolumes": obj.get("workloadVolumes"),
            }
        )
        return _obj
