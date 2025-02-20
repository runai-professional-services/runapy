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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.placement_strategy import PlacementStrategy
from typing import Optional, Set
from typing_extensions import Self


class UpdateNodePoolRequest(BaseModel):
    """
    Pydantic class model representing UpdateNodePoolRequest.

    Parameters:
        ```python
        label_key: str
        label_value: str
        over_provisioning_ratio: int
        placement_strategy: PlacementStrategy
        ```
        label_key: key of node label for pool
        label_value: value of node label for pool
        over_provisioning_ratio: See model int for more information. - Default: 1
        placement_strategy: See model PlacementStrategy for more information.
    Example:
        ```python
        UpdateNodePoolRequest(
            label_key='node-type',
                        label_value='type-x',
                        over_provisioning_ratio=1,
                        placement_strategy=runai.models.placement_strategy.PlacementStrategy(
                    cpu = 'spread',
                    gpu = 'binpack', )
        )
        ```
    """  # noqa: E501

    label_key: Optional[StrictStr] = Field(
        default=None, description="key of node label for pool", alias="labelKey"
    )
    label_value: Optional[StrictStr] = Field(
        default=None, description="value of node label for pool", alias="labelValue"
    )
    over_provisioning_ratio: Optional[StrictInt] = Field(
        default=1, alias="overProvisioningRatio"
    )
    placement_strategy: Optional[PlacementStrategy] = Field(
        default=None, alias="placementStrategy"
    )
    __properties: ClassVar[List[str]] = [
        "labelKey",
        "labelValue",
        "overProvisioningRatio",
        "placementStrategy",
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
        """Create an instance of UpdateNodePoolRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateNodePoolRequest from a dict"""
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
                    PlacementStrategy.from_dict(obj["placementStrategy"])
                    if obj.get("placementStrategy") is not None
                    else None
                ),
            }
        )
        return _obj
