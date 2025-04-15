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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.claim_info import ClaimInfo
from typing import Optional, Set
from typing_extensions import Self


class PvcFieldsNonUpdatable(BaseModel):
    """
    Pydantic class model representing PvcFieldsNonUpdatable.

    Parameters:
        ```python
        existing_pvc: Optional[bool]
        claim_name: Optional[str]
        read_only: Optional[bool]
        ephemeral: Optional[bool]
        claim_info: Optional[ClaimInfo]
        ```
        existing_pvc: Verify existing PVC. PVC is assumed to exist when set to &#x60;true&#x60;. If set to &#x60;false&#x60;, the PVC will be created, if it does not exist. - Default: False
        claim_name: Name for the PVC. Allow referencing it across workloads. If not provided, a name based on the workload name and scope will be auto-generated.
        read_only: Permit only read access to PVC. - Default: False
        ephemeral: Use &#x60;true&#x60; to set PVC to ephemeral. If set to &#x60;true&#x60;, the PVC will be deleted when the workload is stopped. Not supported for inference workloads. - Default: False
        claim_info: See model ClaimInfo for more information.
    Example:
        ```python
        PvcFieldsNonUpdatable(
            existing_pvc=True,
                        claim_name='my-claim',
                        read_only=True,
                        ephemeral=False,
                        claim_info=runai.models.claim_info.ClaimInfo(
                    size = '1G',
                    storage_class = 'my-storage-class',
                    access_modes = runai.models.pvc_access_modes.PvcAccessModes(
                        read_write_once = True,
                        read_only_many = True,
                        read_write_many = True, ),
                    volume_mode = 'Filesystem', )
        )
        ```
    """  # noqa: E501

    existing_pvc: Optional[StrictBool] = Field(
        default=False,
        description="Verify existing PVC. PVC is assumed to exist when set to `true`. If set to `false`, the PVC will be created, if it does not exist.",
        alias="existingPvc",
    )
    claim_name: Optional[
        Annotated[str, Field(min_length=1, strict=True, max_length=63)]
    ] = Field(
        default=None,
        description="Name for the PVC. Allow referencing it across workloads. If not provided, a name based on the workload name and scope will be auto-generated.",
        alias="claimName",
    )
    read_only: Optional[StrictBool] = Field(
        default=False, description="Permit only read access to PVC.", alias="readOnly"
    )
    ephemeral: Optional[StrictBool] = Field(
        default=False,
        description="Use `true` to set PVC to ephemeral. If set to `true`, the PVC will be deleted when the workload is stopped. Not supported for inference workloads.",
    )
    claim_info: Optional[ClaimInfo] = Field(default=None, alias="claimInfo")
    __properties: ClassVar[List[str]] = [
        "existingPvc",
        "claimName",
        "readOnly",
        "ephemeral",
        "claimInfo",
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
        """Create an instance of PvcFieldsNonUpdatable from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of claim_info
        if self.claim_info:
            _dict["claimInfo"] = self.claim_info.to_dict()
        # set to None if existing_pvc (nullable) is None
        # and model_fields_set contains the field
        if self.existing_pvc is None and "existing_pvc" in self.model_fields_set:
            _dict["existingPvc"] = None

        # set to None if claim_name (nullable) is None
        # and model_fields_set contains the field
        if self.claim_name is None and "claim_name" in self.model_fields_set:
            _dict["claimName"] = None

        # set to None if read_only (nullable) is None
        # and model_fields_set contains the field
        if self.read_only is None and "read_only" in self.model_fields_set:
            _dict["readOnly"] = None

        # set to None if ephemeral (nullable) is None
        # and model_fields_set contains the field
        if self.ephemeral is None and "ephemeral" in self.model_fields_set:
            _dict["ephemeral"] = None

        # set to None if claim_info (nullable) is None
        # and model_fields_set contains the field
        if self.claim_info is None and "claim_info" in self.model_fields_set:
            _dict["claimInfo"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PvcFieldsNonUpdatable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "existingPvc": (
                    obj.get("existingPvc")
                    if obj.get("existingPvc") is not None
                    else False
                ),
                "claimName": obj.get("claimName"),
                "readOnly": (
                    obj.get("readOnly") if obj.get("readOnly") is not None else False
                ),
                "ephemeral": (
                    obj.get("ephemeral") if obj.get("ephemeral") is not None else False
                ),
                "claimInfo": (
                    ClaimInfo.from_dict(obj["claimInfo"])
                    if obj.get("claimInfo") is not None
                    else None
                ),
            }
        )
        return _obj
