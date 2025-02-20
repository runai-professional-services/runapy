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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class NonNullResourceV1(BaseModel):
    """
    Pydantic class model representing NonNullResourceV1.

    Parameters:
        ```python
        deserved: float
        max_allowed: Optional[float]
        over_quota_weight: Optional[float]
        ```
        deserved: The amount of resources guaranteed to be allocated in case the cluster has those resources.
        max_allowed: Maximum amount of resources that can be allocated. If equal to deserved, no over-quota will be allowed. Use \&quot;-1\&quot; for unlimited over quota.
        over_quota_weight: The priority for over quota resources.
    Example:
        ```python
        NonNullResourceV1(
            deserved=0,
                        max_allowed=1000,
                        over_quota_weight=2
        )
        ```
    """  # noqa: E501

    deserved: Union[StrictFloat, StrictInt] = Field(
        description="The amount of resources guaranteed to be allocated in case the cluster has those resources."
    )
    max_allowed: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description='Maximum amount of resources that can be allocated. If equal to deserved, no over-quota will be allowed. Use "-1" for unlimited over quota.',
        alias="maxAllowed",
    )
    over_quota_weight: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="The priority for over quota resources.",
        alias="overQuotaWeight",
    )
    __properties: ClassVar[List[str]] = ["deserved", "maxAllowed", "overQuotaWeight"]

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
        """Create an instance of NonNullResourceV1 from a JSON string"""
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
        # set to None if max_allowed (nullable) is None
        # and model_fields_set contains the field
        if self.max_allowed is None and "max_allowed" in self.model_fields_set:
            _dict["maxAllowed"] = None

        # set to None if over_quota_weight (nullable) is None
        # and model_fields_set contains the field
        if (
            self.over_quota_weight is None
            and "over_quota_weight" in self.model_fields_set
        ):
            _dict["overQuotaWeight"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NonNullResourceV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "deserved": obj.get("deserved"),
                "maxAllowed": obj.get("maxAllowed"),
                "overQuotaWeight": obj.get("overQuotaWeight"),
            }
        )
        return _obj
