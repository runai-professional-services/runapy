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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.array_rules import ArrayRules
from runai.models.boolean_rules import BooleanRules
from runai.models.seccomp_profile_type_rules import SeccompProfileTypeRules
from runai.models.uid_gid_source_rules import UidGidSourceRules
from typing import Optional, Set
from typing_extensions import Self


class CommonSecurityNonOverridableRules(BaseModel):
    """
    Pydantic class model representing CommonSecurityNonOverridableRules.

    Parameters:
        ```python
        uid_gid_source: Optional[UidGidSourceRules]
        capabilities: Optional[ArrayRules]
        seccomp_profile_type: Optional[SeccompProfileTypeRules]
        run_as_non_root: Optional[BooleanRules]
        read_only_root_filesystem: Optional[BooleanRules]
        ```
        uid_gid_source: See model UidGidSourceRules for more information.
        capabilities: See model ArrayRules for more information.
        seccomp_profile_type: See model SeccompProfileTypeRules for more information.
        run_as_non_root: See model BooleanRules for more information.
        read_only_root_filesystem: See model BooleanRules for more information.
    Example:
        ```python
        CommonSecurityNonOverridableRules(
            uid_gid_source=runai.models.uid_gid_source_rules.UidGidSourceRules(),
                        capabilities=runai.models.array_rules.ArrayRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        seccomp_profile_type=runai.models.seccomp_profile_type_rules.SeccompProfileTypeRules(),
                        run_as_non_root=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        read_only_root_filesystem=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, )
        )
        ```
    """  # noqa: E501

    uid_gid_source: Optional[UidGidSourceRules] = Field(
        default=None, alias="uidGidSource"
    )
    capabilities: Optional[ArrayRules] = None
    seccomp_profile_type: Optional[SeccompProfileTypeRules] = Field(
        default=None, alias="seccompProfileType"
    )
    run_as_non_root: Optional[BooleanRules] = Field(default=None, alias="runAsNonRoot")
    read_only_root_filesystem: Optional[BooleanRules] = Field(
        default=None, alias="readOnlyRootFilesystem"
    )
    __properties: ClassVar[List[str]] = [
        "uidGidSource",
        "capabilities",
        "seccompProfileType",
        "runAsNonRoot",
        "readOnlyRootFilesystem",
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
        """Create an instance of CommonSecurityNonOverridableRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of uid_gid_source
        if self.uid_gid_source:
            _dict["uidGidSource"] = self.uid_gid_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict["capabilities"] = self.capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seccomp_profile_type
        if self.seccomp_profile_type:
            _dict["seccompProfileType"] = self.seccomp_profile_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run_as_non_root
        if self.run_as_non_root:
            _dict["runAsNonRoot"] = self.run_as_non_root.to_dict()
        # override the default output from pydantic by calling `to_dict()` of read_only_root_filesystem
        if self.read_only_root_filesystem:
            _dict["readOnlyRootFilesystem"] = self.read_only_root_filesystem.to_dict()
        # set to None if uid_gid_source (nullable) is None
        # and model_fields_set contains the field
        if self.uid_gid_source is None and "uid_gid_source" in self.model_fields_set:
            _dict["uidGidSource"] = None

        # set to None if capabilities (nullable) is None
        # and model_fields_set contains the field
        if self.capabilities is None and "capabilities" in self.model_fields_set:
            _dict["capabilities"] = None

        # set to None if seccomp_profile_type (nullable) is None
        # and model_fields_set contains the field
        if (
            self.seccomp_profile_type is None
            and "seccomp_profile_type" in self.model_fields_set
        ):
            _dict["seccompProfileType"] = None

        # set to None if run_as_non_root (nullable) is None
        # and model_fields_set contains the field
        if self.run_as_non_root is None and "run_as_non_root" in self.model_fields_set:
            _dict["runAsNonRoot"] = None

        # set to None if read_only_root_filesystem (nullable) is None
        # and model_fields_set contains the field
        if (
            self.read_only_root_filesystem is None
            and "read_only_root_filesystem" in self.model_fields_set
        ):
            _dict["readOnlyRootFilesystem"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonSecurityNonOverridableRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "uidGidSource": (
                    UidGidSourceRules.from_dict(obj["uidGidSource"])
                    if obj.get("uidGidSource") is not None
                    else None
                ),
                "capabilities": (
                    ArrayRules.from_dict(obj["capabilities"])
                    if obj.get("capabilities") is not None
                    else None
                ),
                "seccompProfileType": (
                    SeccompProfileTypeRules.from_dict(obj["seccompProfileType"])
                    if obj.get("seccompProfileType") is not None
                    else None
                ),
                "runAsNonRoot": (
                    BooleanRules.from_dict(obj["runAsNonRoot"])
                    if obj.get("runAsNonRoot") is not None
                    else None
                ),
                "readOnlyRootFilesystem": (
                    BooleanRules.from_dict(obj["readOnlyRootFilesystem"])
                    if obj.get("readOnlyRootFilesystem") is not None
                    else None
                ),
            }
        )
        return _obj
