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
from typing_extensions import Annotated
from runai.models.capability import Capability
from runai.models.connection import Connection
from runai.models.image_pull_policy import ImagePullPolicy
from runai.models.probes import Probes
from runai.models.seccomp_profile_type import SeccompProfileType
from runai.models.uid_gid_source import UidGidSource
from typing import Optional, Set
from typing_extensions import Self


class NonOverridableSpecFields(BaseModel):
    """
    Pydantic class model representing NonOverridableSpecFields.

    Parameters:
        ```python
        image: Optional[str]
        image_pull_policy: Optional[ImagePullPolicy]
        working_dir: Optional[str]
        create_home_dir: Optional[bool]
        probes: Optional[Probes]
        tty: Optional[bool]
        stdin: Optional[bool]
        uid_gid_source: Optional[UidGidSource]
        capabilities: Optional[List[Capability]]
        seccomp_profile_type: Optional[SeccompProfileType]
        run_as_non_root: Optional[bool]
        read_only_root_filesystem: Optional[bool]
        allow_privilege_escalation: Optional[bool]
        host_ipc: Optional[bool]
        host_network: Optional[bool]
        connections: List[Connection]
        override_uid_gid_in_workspace: bool
        ```
        image: Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.
        image_pull_policy: See model ImagePullPolicy for more information.
        working_dir: Container&#39;s working directory. If not specified, the container runtime default will be used. This may be configured in the container image.
        create_home_dir: When set to &#x60;true&#x60;, creates a home directory for the container.
        probes: See model Probes for more information.
        tty: Whether this container should allocate a TTY for itself, also requires &#39;stdin&#39; to be true.
        stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF
        uid_gid_source: See model UidGidSource for more information.
        capabilities: Add POSIX capabilities to running containers. Defaults to the default set of capabilities granted by the container runtime.
        seccomp_profile_type: See model SeccompProfileType for more information.
        run_as_non_root: Force the container to run as a non-root user.
        read_only_root_filesystem: If true, mounts the container&#39;s root filesystem as read-only.
        allow_privilege_escalation: Allow the container running the workload and all launched processes to gain additional privileges after the workload starts. For more information consult the User Identity in Container guide at https://docs.run.ai/admin/runai-setup/config/non-root-containers/
        host_ipc: Whether to enable host IPC. Defaults to false.
        host_network: Whether to enable host networking. Default to false.
        connections: List of connections that either expose ports from the container (each port is associated with a tool that the container runs), or URL&#39;s to be used for connecting to an external tool that is related to the action of the container (such as Weights &amp; Biases).
        override_uid_gid_in_workspace: Allow specifying uid/gid as part of create workspace. This is relevant only for custom uigGidSource. - Default: False
    Example:
        ```python
        NonOverridableSpecFields(
            image='python:3.8',
                        image_pull_policy='Always',
                        working_dir='/home/myfolder',
                        create_home_dir=True,
                        probes=runai.models.probes.Probes(
                    readiness = runai.models.probe.Probe(
                        initial_delay_seconds = 0,
                        period_seconds = 1,
                        timeout_seconds = 1,
                        success_threshold = 1,
                        failure_threshold = 1,
                        handler = runai.models.probe_handler.ProbeHandler(
                            http_get = runai.models.probe_handler_http_get.ProbeHandler_httpGet(
                                path = '',
                                port = 1,
                                host = '',
                                scheme = 'HTTP', ), ), ), ),
                        tty=True,
                        stdin=True,
                        uid_gid_source='fromTheImage',
                        capabilities=[CHOWN, KILL],
                        seccomp_profile_type='RuntimeDefault',
                        run_as_non_root=True,
                        read_only_root_filesystem=False,
                        allow_privilege_escalation=False,
                        host_ipc=False,
                        host_network=False,
                        connections=[
                    runai.models.connection.Connection(
                        name = '0',
                        is_external = True,
                        internal_tool_info = runai.models.internal_tool_info.InternalToolInfo(
                            tool_type = 'jupyter-notebook',
                            connection_type = 'LoadBalancer',
                            container_port = 1,
                            node_port_info = runai.models.node_port_info.NodePortInfo(
                                is_custom_port = True, ),
                            external_url_info = runai.models.external_url_info.ExternalUrlInfo(
                                is_custom_url = True,
                                external_url = '0', ),
                            serving_port_info = runai.models.serving_port_info.ServingPortInfo(
                                protocol = 'grpc', ), ),
                        external_tool_info = runai.models.external_tool_info.ExternalToolInfo(
                            tool_type = 'wandb',
                            external_url = 'https://wandb.com/myteam/${PROJECT_NAME}', ), )
                    ],
                        override_uid_gid_in_workspace=True
        )
        ```
    """  # noqa: E501

    image: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.",
    )
    image_pull_policy: Optional[ImagePullPolicy] = Field(
        default=None, alias="imagePullPolicy"
    )
    working_dir: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Container's working directory. If not specified, the container runtime default will be used. This may be configured in the container image.",
        alias="workingDir",
    )
    create_home_dir: Optional[StrictBool] = Field(
        default=None,
        description="When set to `true`, creates a home directory for the container.",
        alias="createHomeDir",
    )
    probes: Optional[Probes] = None
    tty: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.",
    )
    stdin: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF",
    )
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
    connections: Optional[List[Connection]] = Field(
        default=None,
        description="List of connections that either expose ports from the container (each port is associated with a tool that the container runs), or URL's to be used for connecting to an external tool that is related to the action of the container (such as Weights & Biases).",
    )
    override_uid_gid_in_workspace: Optional[StrictBool] = Field(
        default=False,
        description="Allow specifying uid/gid as part of create workspace. This is relevant only for custom uigGidSource.",
        alias="overrideUidGidInWorkspace",
    )
    __properties: ClassVar[List[str]] = [
        "image",
        "imagePullPolicy",
        "workingDir",
        "createHomeDir",
        "probes",
        "tty",
        "stdin",
        "uidGidSource",
        "capabilities",
        "seccompProfileType",
        "runAsNonRoot",
        "readOnlyRootFilesystem",
        "allowPrivilegeEscalation",
        "hostIpc",
        "hostNetwork",
        "connections",
        "overrideUidGidInWorkspace",
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
        """Create an instance of NonOverridableSpecFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of probes
        if self.probes:
            _dict["probes"] = self.probes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict["connections"] = _items
        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict["image"] = None

        # set to None if image_pull_policy (nullable) is None
        # and model_fields_set contains the field
        if (
            self.image_pull_policy is None
            and "image_pull_policy" in self.model_fields_set
        ):
            _dict["imagePullPolicy"] = None

        # set to None if working_dir (nullable) is None
        # and model_fields_set contains the field
        if self.working_dir is None and "working_dir" in self.model_fields_set:
            _dict["workingDir"] = None

        # set to None if create_home_dir (nullable) is None
        # and model_fields_set contains the field
        if self.create_home_dir is None and "create_home_dir" in self.model_fields_set:
            _dict["createHomeDir"] = None

        # set to None if probes (nullable) is None
        # and model_fields_set contains the field
        if self.probes is None and "probes" in self.model_fields_set:
            _dict["probes"] = None

        # set to None if tty (nullable) is None
        # and model_fields_set contains the field
        if self.tty is None and "tty" in self.model_fields_set:
            _dict["tty"] = None

        # set to None if stdin (nullable) is None
        # and model_fields_set contains the field
        if self.stdin is None and "stdin" in self.model_fields_set:
            _dict["stdin"] = None

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
        """Create an instance of NonOverridableSpecFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "image": obj.get("image"),
                "imagePullPolicy": obj.get("imagePullPolicy"),
                "workingDir": obj.get("workingDir"),
                "createHomeDir": obj.get("createHomeDir"),
                "probes": (
                    Probes.from_dict(obj["probes"])
                    if obj.get("probes") is not None
                    else None
                ),
                "tty": obj.get("tty"),
                "stdin": obj.get("stdin"),
                "uidGidSource": obj.get("uidGidSource"),
                "capabilities": obj.get("capabilities"),
                "seccompProfileType": obj.get("seccompProfileType"),
                "runAsNonRoot": obj.get("runAsNonRoot"),
                "readOnlyRootFilesystem": obj.get("readOnlyRootFilesystem"),
                "allowPrivilegeEscalation": obj.get("allowPrivilegeEscalation"),
                "hostIpc": obj.get("hostIpc"),
                "hostNetwork": obj.get("hostNetwork"),
                "connections": (
                    [Connection.from_dict(_item) for _item in obj["connections"]]
                    if obj.get("connections") is not None
                    else None
                ),
                "overrideUidGidInWorkspace": (
                    obj.get("overrideUidGidInWorkspace")
                    if obj.get("overrideUidGidInWorkspace") is not None
                    else False
                ),
            }
        )
        return _obj
