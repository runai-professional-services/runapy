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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.image_pull_policy import ImagePullPolicy
from runai.models.pod_affinity import PodAffinity
from runai.models.probes import Probes
from typing import Optional, Set
from typing_extensions import Self


class CommonFlatFields(BaseModel):
    """
    Pydantic class model representing CommonFlatFields.

    Parameters:
        ```python
        command: Optional[str]
        args: Optional[str]
        image: Optional[str]
        image_pull_policy: Optional[ImagePullPolicy]
        working_dir: Optional[str]
        create_home_dir: Optional[bool]
        probes: Optional[Probes]
        node_type: Optional[str]
        node_pools: Optional[List[str]]
        pod_affinity: Optional[PodAffinity]
        ```
        command: A command to the server as the entry point of the container running the workspace.
        args: Arguments to the command that the container running the workspace executes.
        image: Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.
        image_pull_policy: See model ImagePullPolicy for more information.
        working_dir: Container&#39;s working directory. If not specified, the container runtime default will be used. This may be configured in the container image.
        create_home_dir: When set to &#x60;true&#x60;, creates a home directory for the container.
        probes: See model Probes for more information.
        node_type: Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup).
        node_pools: A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.
        pod_affinity: See model PodAffinity for more information.
    Example:
        ```python
        CommonFlatFields(
            command='python',
                        args='-x my-script.py',
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
                                path = '/',
                                port = 1,
                                host = 'example.com',
                                scheme = 'HTTP', ), ), ), ),
                        node_type='my-node-type',
                        node_pools=[my-node-pool-a, my-node-pool-b],
                        pod_affinity=runai.models.pod_affinity.PodAffinity(
                    type = 'Required',
                    key = '', )
        )
        ```
    """  # noqa: E501

    command: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="A command to the server as the entry point of the container running the workspace.",
    )
    args: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Arguments to the command that the container running the workspace executes.",
    )
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
    node_type: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup).",
        alias="nodeType",
    )
    node_pools: Optional[List[StrictStr]] = Field(
        default=None,
        description="A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.",
        alias="nodePools",
    )
    pod_affinity: Optional[PodAffinity] = Field(default=None, alias="podAffinity")
    __properties: ClassVar[List[str]] = [
        "command",
        "args",
        "image",
        "imagePullPolicy",
        "workingDir",
        "createHomeDir",
        "probes",
        "nodeType",
        "nodePools",
        "podAffinity",
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
        """Create an instance of CommonFlatFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pod_affinity
        if self.pod_affinity:
            _dict["podAffinity"] = self.pod_affinity.to_dict()
        # set to None if command (nullable) is None
        # and model_fields_set contains the field
        if self.command is None and "command" in self.model_fields_set:
            _dict["command"] = None

        # set to None if args (nullable) is None
        # and model_fields_set contains the field
        if self.args is None and "args" in self.model_fields_set:
            _dict["args"] = None

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

        # set to None if node_type (nullable) is None
        # and model_fields_set contains the field
        if self.node_type is None and "node_type" in self.model_fields_set:
            _dict["nodeType"] = None

        # set to None if node_pools (nullable) is None
        # and model_fields_set contains the field
        if self.node_pools is None and "node_pools" in self.model_fields_set:
            _dict["nodePools"] = None

        # set to None if pod_affinity (nullable) is None
        # and model_fields_set contains the field
        if self.pod_affinity is None and "pod_affinity" in self.model_fields_set:
            _dict["podAffinity"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonFlatFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "args": obj.get("args"),
                "image": obj.get("image"),
                "imagePullPolicy": obj.get("imagePullPolicy"),
                "workingDir": obj.get("workingDir"),
                "createHomeDir": obj.get("createHomeDir"),
                "probes": (
                    Probes.from_dict(obj["probes"])
                    if obj.get("probes") is not None
                    else None
                ),
                "nodeType": obj.get("nodeType"),
                "nodePools": obj.get("nodePools"),
                "podAffinity": (
                    PodAffinity.from_dict(obj["podAffinity"])
                    if obj.get("podAffinity") is not None
                    else None
                ),
            }
        )
        return _obj
