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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.capability import Capability
from runai.models.seccomp_profile_type import SeccompProfileType
from runai.models.uid_gid_source import UidGidSource
from typing import Optional, Set
from typing_extensions import Self


class CommonSecurityNonOverridable(BaseModel):
    """
    Pydantic class model representing Security non overrideable fields. In the context of assets,these are environment asset fields that cannot be overriden in the submit workload request..

    Parameters:
        ```python
        uid_gid_source: Optional[UidGidSource]
        capabilities: Optional[List[Capability]]
        seccomp_profile_type: Optional[SeccompProfileType]
        run_as_non_root: Optional[bool]
        read_only_root_filesystem: Optional[bool]
        ```
        uid_gid_source: See model UidGidSource for more information.
        capabilities: Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.
        seccomp_profile_type: See model SeccompProfileType for more information.
        run_as_non_root: Force the container to run as a non-root user.
        read_only_root_filesystem: If true, mounts the container&#39;s root filesystem as read-only.
    Example:
        ```python
        CommonSecurityNonOverridable(
            uid_gid_source='fromTheImage',
                        capabilities=["CHOWN","KILL"],
                        seccomp_profile_type='RuntimeDefault',
                        run_as_non_root=True,
                        read_only_root_filesystem=False
        )
        ```
    """  # noqa: E501

    uid_gid_source: Optional[UidGidSource] = Field(default=None, alias="uidGidSource")
    capabilities: Optional[List[Capability]] = Field(
        default=None,
        description="Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.",
    )
    seccomp_profile_type: Optional[SeccompProfileType] = Field(
        default=None, alias="seccompProfileType"
    )
    run_as_non_root: Optional[StrictBool] = Field(
        default=None,
        description="Force the container to run as a non-root user.",
        alias="runAsNonRoot",
    )
    read_only_root_filesystem: Optional[StrictBool] = Field(
        default=None,
        description="If true, mounts the container's root filesystem as read-only.",
        alias="readOnlyRootFilesystem",
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
        """Create an instance of CommonSecurityNonOverridable from a JSON string"""
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
        """Create an instance of CommonSecurityNonOverridable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "uidGidSource": obj.get("uidGidSource"),
                "capabilities": obj.get("capabilities"),
                "seccompProfileType": obj.get("seccompProfileType"),
                "runAsNonRoot": obj.get("runAsNonRoot"),
                "readOnlyRootFilesystem": obj.get("readOnlyRootFilesystem"),
            }
        )
        return _obj
