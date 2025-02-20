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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.asset_update_request import AssetUpdateRequest
from runai.models.pvc_updatable_fields import PvcUpdatableFields
from typing import Optional, Set
from typing_extensions import Self


class PVCUpdateRequest(BaseModel):
    """
    Pydantic class model representing PVCUpdateRequest.

    Parameters:
        ```python
        meta: AssetUpdateRequest
        spec: Optional[PvcUpdatableFields]
        ```
        meta: See model AssetUpdateRequest for more information.
        spec: See model PvcUpdatableFields for more information.
    Example:
        ```python
        PVCUpdateRequest(
            meta={"name":"my-asset"},
                        spec=runai.models.pvc_updatable_fields.PvcUpdatableFields(
                    path = '/container/my-claim', )
        )
        ```
    """  # noqa: E501

    meta: AssetUpdateRequest
    spec: Optional[PvcUpdatableFields] = None
    __properties: ClassVar[List[str]] = ["meta", "spec"]

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
        """Create an instance of PVCUpdateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict["spec"] = self.spec.to_dict()
        # set to None if spec (nullable) is None
        # and model_fields_set contains the field
        if self.spec is None and "spec" in self.model_fields_set:
            _dict["spec"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PVCUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "meta": (
                    AssetUpdateRequest.from_dict(obj["meta"])
                    if obj.get("meta") is not None
                    else None
                ),
                "spec": (
                    PvcUpdatableFields.from_dict(obj["spec"])
                    if obj.get("spec") is not None
                    else None
                ),
            }
        )
        return _obj
