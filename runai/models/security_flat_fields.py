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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.capability import Capability
from runai.models.seccomp_profile_type import SeccompProfileType
from runai.models.uid_gid_source import UidGidSource
from typing import Optional, Set
from typing_extensions import Self


class SecurityFlatFields(BaseModel):
    """
    Pydantic class model representing SecurityFlatFields.

    Parameters:
        ```python
        uid_gid_source: Optional[UidGidSource]
        capabilities: Optional[List[Capability]]
        seccomp_profile_type: Optional[SeccompProfileType]
        run_as_non_root: Optional[bool]
        read_only_root_filesystem: Optional[bool]
        run_as_uid: Optional[int]
        run_as_gid: Optional[int]
        supplemental_groups: Optional[str]
        allow_privilege_escalation: Optional[bool]
        host_ipc: Optional[bool]
        host_network: Optional[bool]
        ```
        uid_gid_source: See model UidGidSource for more information.
        capabilities: Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.
        seccomp_profile_type: See model SeccompProfileType for more information.
        run_as_non_root: Force the container to run as a non-root user.
        read_only_root_filesystem: If true, mounts the container&#39;s root filesystem as read-only.
        run_as_uid: The user id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset &#x60;runAsUid&#x60; field (optional). Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled.
        run_as_gid: The group id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset &#x60;runAsGid&#x60; field (optional). Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled.
        supplemental_groups: Comma separated list of groups that the user running the container belongs to, in addition to the group indicated by runAsGid. Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled. Using an empty string implies reverting the supplementary groups of the image.
        allow_privilege_escalation: Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/
        host_ipc: Whether to enable host IPC. Defaults to false.
        host_network: Whether to enable host networking. Default to false.
    Example:
        ```python
        SecurityFlatFields(
            uid_gid_source='fromTheImage',
                        capabilities=[CHOWN, KILL],
                        seccomp_profile_type='RuntimeDefault',
                        run_as_non_root=True,
                        read_only_root_filesystem=False,
                        run_as_uid=500,
                        run_as_gid=30,
                        supplemental_groups='2,3,5,8',
                        allow_privilege_escalation=False,
                        host_ipc=False,
                        host_network=False
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
    run_as_uid: Optional[StrictInt] = Field(
        default=None,
        description="The user id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsUid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.",
        alias="runAsUid",
    )
    run_as_gid: Optional[StrictInt] = Field(
        default=None,
        description="The group id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset `runAsGid` field (optional). Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled.",
        alias="runAsGid",
    )
    supplemental_groups: Optional[StrictStr] = Field(
        default=None,
        description="Comma separated list of groups that the user running the container belongs to, in addition to the group indicated by runAsGid. Use only when the source uid/gid of the environment asset is not `fromTheImage`, and `overrideUidGidInWorkspace` is enabled. Using an empty string implies reverting the supplementary groups of the image.",
        alias="supplementalGroups",
    )
    allow_privilege_escalation: Optional[StrictBool] = Field(
        default=None,
        description="Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/",
        alias="allowPrivilegeEscalation",
    )
    host_ipc: Optional[StrictBool] = Field(
        default=None,
        description="Whether to enable host IPC. Defaults to false.",
        alias="hostIpc",
    )
    host_network: Optional[StrictBool] = Field(
        default=None,
        description="Whether to enable host networking. Default to false.",
        alias="hostNetwork",
    )
    __properties: ClassVar[List[str]] = [
        "uidGidSource",
        "capabilities",
        "seccompProfileType",
        "runAsNonRoot",
        "readOnlyRootFilesystem",
        "runAsUid",
        "runAsGid",
        "supplementalGroups",
        "allowPrivilegeEscalation",
        "hostIpc",
        "hostNetwork",
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
        """Create an instance of SecurityFlatFields from a JSON string"""
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

        # set to None if run_as_uid (nullable) is None
        # and model_fields_set contains the field
        if self.run_as_uid is None and "run_as_uid" in self.model_fields_set:
            _dict["runAsUid"] = None

        # set to None if run_as_gid (nullable) is None
        # and model_fields_set contains the field
        if self.run_as_gid is None and "run_as_gid" in self.model_fields_set:
            _dict["runAsGid"] = None

        # set to None if supplemental_groups (nullable) is None
        # and model_fields_set contains the field
        if (
            self.supplemental_groups is None
            and "supplemental_groups" in self.model_fields_set
        ):
            _dict["supplementalGroups"] = None

        # set to None if allow_privilege_escalation (nullable) is None
        # and model_fields_set contains the field
        if (
            self.allow_privilege_escalation is None
            and "allow_privilege_escalation" in self.model_fields_set
        ):
            _dict["allowPrivilegeEscalation"] = None

        # set to None if host_ipc (nullable) is None
        # and model_fields_set contains the field
        if self.host_ipc is None and "host_ipc" in self.model_fields_set:
            _dict["hostIpc"] = None

        # set to None if host_network (nullable) is None
        # and model_fields_set contains the field
        if self.host_network is None and "host_network" in self.model_fields_set:
            _dict["hostNetwork"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityFlatFields from a dict"""
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
                "runAsUid": obj.get("runAsUid"),
                "runAsGid": obj.get("runAsGid"),
                "supplementalGroups": obj.get("supplementalGroups"),
                "allowPrivilegeEscalation": obj.get("allowPrivilegeEscalation"),
                "hostIpc": obj.get("hostIpc"),
                "hostNetwork": obj.get("hostNetwork"),
            }
        )
        return _obj
