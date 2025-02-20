# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
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
from runai.models.nodepool_create_fields_placement_strategy import (
    NodepoolCreateFieldsPlacementStrategy,
)
from typing import Optional, Set
from typing_extensions import Self


class NodepoolSyncFieldsStatus(BaseModel):
    """
    Pydantic class model representing NodepoolSyncFieldsStatus.

    Parameters:
        ```python
        label_key: Optional[str]
        label_value: Optional[str]
        over_provisioning_ratio: Optional[int]
        placement_strategy: NodepoolCreateFieldsPlacementStrategy
        nodes: List[str]
        ```
        label_key: Label key for associated nodes to the Node Pool (with value as in labelValue)
        label_value: Label value for associated nodes to the Node Pool (with key as in labelKey)
        over_provisioning_ratio: See model int for more information. - Default: 1
        placement_strategy: See model NodepoolCreateFieldsPlacementStrategy for more information.
        nodes: See model List[str] for more information.
    Example:
        ```python
        NodepoolSyncFieldsStatus(
            label_key='node-type',
                        label_value='type-x',
                        over_provisioning_ratio=1,
                        placement_strategy=runai.models.nodepool_create_fields_placement_strategy.NodepoolCreateFields_placementStrategy(
                    cpu = 'spread',
                    gpu = 'spread', ),
                        nodes=[
                    'node1'
                    ]
        )
        ```
    """  # noqa: E501

    label_key: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Label key for associated nodes to the Node Pool (with value as in labelValue)",
        alias="labelKey",
    )
    label_value: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Label value for associated nodes to the Node Pool (with key as in labelKey)",
        alias="labelValue",
    )
    over_provisioning_ratio: Optional[
        Annotated[int, Field(le=5, strict=True, ge=1)]
    ] = Field(default=1, alias="overProvisioningRatio")
    placement_strategy: Optional[NodepoolCreateFieldsPlacementStrategy] = Field(
        default=None, alias="placementStrategy"
    )
    nodes: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "labelKey",
        "labelValue",
        "overProvisioningRatio",
        "placementStrategy",
        "nodes",
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
        """Create an instance of NodepoolSyncFieldsStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of placement_strategy
        if self.placement_strategy:
            _dict["placementStrategy"] = self.placement_strategy.to_dict()
        # set to None if label_key (nullable) is None
        # and model_fields_set contains the field
        if self.label_key is None and "label_key" in self.model_fields_set:
            _dict["labelKey"] = None

        # set to None if label_value (nullable) is None
        # and model_fields_set contains the field
        if self.label_value is None and "label_value" in self.model_fields_set:
            _dict["labelValue"] = None

        # set to None if over_provisioning_ratio (nullable) is None
        # and model_fields_set contains the field
        if (
            self.over_provisioning_ratio is None
            and "over_provisioning_ratio" in self.model_fields_set
        ):
            _dict["overProvisioningRatio"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodepoolSyncFieldsStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "labelKey": obj.get("labelKey"),
                "labelValue": obj.get("labelValue"),
                "overProvisioningRatio": (
                    obj.get("overProvisioningRatio")
                    if obj.get("overProvisioningRatio") is not None
                    else 1
                ),
                "placementStrategy": (
                    NodepoolCreateFieldsPlacementStrategy.from_dict(
                        obj["placementStrategy"]
                    )
                    if obj.get("placementStrategy") is not None
                    else None
                ),
                "nodes": obj.get("nodes"),
            }
        )
        return _obj
