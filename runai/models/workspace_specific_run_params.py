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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.annotation import Annotation
from runai.models.environment_variable import EnvironmentVariable
from runai.models.label import Label
from runai.models.pod_affinity import PodAffinity
from runai.models.specific_run_connection_info import SpecificRunConnectionInfo
from typing import Optional, Set
from typing_extensions import Self


class WorkspaceSpecificRunParams(BaseModel):
    """
    Pydantic class model representing WorkspaceSpecificRunParams.

    Parameters:
        ```python
        command: Optional[str]
        args: Optional[str]
        run_as_uid: Optional[int]
        run_as_gid: Optional[int]
        supplemental_groups: Optional[str]
        environment_variables: Optional[List[EnvironmentVariable]]
        node_type: Optional[str]
        node_pools: Optional[List[str]]
        pod_affinity: Optional[PodAffinity]
        terminate_after_preemption: Optional[bool]
        auto_deletion_time_after_completion_seconds: Optional[int]
        backoff_limit: Optional[int]
        annotations: Optional[List[Annotation]]
        labels: Optional[List[Label]]
        connections: Optional[List[SpecificRunConnectionInfo]]
        allow_over_quota: Optional[bool]
        ```
        command: A command to the server as the entry point of the container running the workspace.
        args: Arguments to the command that the container running the workspace executes.
        run_as_uid: The user id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset &#x60;runAsUid&#x60; field (optional). Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled.
        run_as_gid: The group id to run the entrypoint of the container which executes the workspace. Default to the value specified in the environment asset &#x60;runAsGid&#x60; field (optional). Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled.
        supplemental_groups: Comma separated list of groups that the user running the container belongs to, in addition to the group indicated by runAsGid. Use only when the source uid/gid of the environment asset is not &#x60;fromTheImage&#x60;, and &#x60;overrideUidGidInWorkspace&#x60; is enabled. Using an empty string implies reverting the supplementary groups of the image.
        environment_variables: Set of environment variables to populate into the container running the workspace.
        node_type: Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docs.run.ai/admin/admin-ui-setup/project-setup).
        node_pools: A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.
        pod_affinity: See model PodAffinity for more information.
        terminate_after_preemption: Indicates if the job should be terminated by the system after it has been preempted.
        auto_deletion_time_after_completion_seconds: Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.
        backoff_limit: Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.
        annotations: Set of annotations to populate into the container running the workspace.
        labels: Set of labels to populate into the container running the workspace.
        connections: See model List[SpecificRunConnectionInfo] for more information.
        allow_over_quota: Whether to allow the workload to exceed the quota of the project.
    Example:
        ```python
        WorkspaceSpecificRunParams(
            command='python',
                        args='-x my-script.py',
                        run_as_uid=500,
                        run_as_gid=30,
                        supplemental_groups='2,3,5,8',
                        environment_variables=[
                    runai.models.environment_variable.EnvironmentVariable(
                        name = 'HOME',
                        value = '/home/my-folder',
                        secret = runai.models.environment_variable_secret.EnvironmentVariableSecret(
                            name = 'postgress_secret',
                            key = 'POSTGRES_PASSWORD', ),
                        exclude = False, )
                    ],
                        node_type='my-node-type',
                        node_pools=[my-node-pool-a, my-node-pool-b],
                        pod_affinity=runai.models.pod_affinity.PodAffinity(
                    type = 'Required',
                    key = '', ),
                        terminate_after_preemption=False,
                        auto_deletion_time_after_completion_seconds=15,
                        backoff_limit=3,
                        annotations=[
                    runai.models.annotation.Annotation(
                        name = 'billing',
                        value = 'my-billing-unit',
                        exclude = False, )
                    ],
                        labels=[
                    runai.models.label.Label(
                        name = 'stage',
                        value = 'initial-research',
                        exclude = False, )
                    ],
                        connections=[
                    runai.models.specific_run_connection_info.SpecificRunConnectionInfo(
                        name = '0',
                        node_port = 0,
                        external_url = '0',
                        authorized_users = [
                            ''
                            ],
                        authorized_groups = [
                            ''
                            ], )
                    ],
                        allow_over_quota=True
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
    environment_variables: Optional[List[Optional[EnvironmentVariable]]] = Field(
        default=None,
        description="Set of environment variables to populate into the container running the workspace.",
        alias="environmentVariables",
    )
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
    terminate_after_preemption: Optional[StrictBool] = Field(
        default=None,
        description="Indicates if the job should be terminated by the system after it has been preempted.",
        alias="terminateAfterPreemption",
    )
    auto_deletion_time_after_completion_seconds: Optional[StrictInt] = Field(
        default=None,
        description="Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.",
        alias="autoDeletionTimeAfterCompletionSeconds",
    )
    backoff_limit: Optional[StrictInt] = Field(
        default=None,
        description="Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.",
        alias="backoffLimit",
    )
    annotations: Optional[List[Optional[Annotation]]] = Field(
        default=None,
        description="Set of annotations to populate into the container running the workspace.",
    )
    labels: Optional[List[Optional[Label]]] = Field(
        default=None,
        description="Set of labels to populate into the container running the workspace.",
    )
    connections: Optional[List[SpecificRunConnectionInfo]] = None
    allow_over_quota: Optional[StrictBool] = Field(
        default=None,
        description="Whether to allow the workload to exceed the quota of the project.",
        alias="allowOverQuota",
    )
    __properties: ClassVar[List[str]] = [
        "command",
        "args",
        "runAsUid",
        "runAsGid",
        "supplementalGroups",
        "environmentVariables",
        "nodeType",
        "nodePools",
        "podAffinity",
        "terminateAfterPreemption",
        "autoDeletionTimeAfterCompletionSeconds",
        "backoffLimit",
        "annotations",
        "labels",
        "connections",
        "allowOverQuota",
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
        """Create an instance of WorkspaceSpecificRunParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in environment_variables (list)
        _items = []
        if self.environment_variables:
            for _item_environment_variables in self.environment_variables:
                if _item_environment_variables:
                    _items.append(_item_environment_variables.to_dict())
            _dict["environmentVariables"] = _items
        # override the default output from pydantic by calling `to_dict()` of pod_affinity
        if self.pod_affinity:
            _dict["podAffinity"] = self.pod_affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item_annotations in self.annotations:
                if _item_annotations:
                    _items.append(_item_annotations.to_dict())
            _dict["annotations"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict["labels"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict["connections"] = _items
        # set to None if command (nullable) is None
        # and model_fields_set contains the field
        if self.command is None and "command" in self.model_fields_set:
            _dict["command"] = None

        # set to None if args (nullable) is None
        # and model_fields_set contains the field
        if self.args is None and "args" in self.model_fields_set:
            _dict["args"] = None

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

        # set to None if environment_variables (nullable) is None
        # and model_fields_set contains the field
        if (
            self.environment_variables is None
            and "environment_variables" in self.model_fields_set
        ):
            _dict["environmentVariables"] = None

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

        # set to None if terminate_after_preemption (nullable) is None
        # and model_fields_set contains the field
        if (
            self.terminate_after_preemption is None
            and "terminate_after_preemption" in self.model_fields_set
        ):
            _dict["terminateAfterPreemption"] = None

        # set to None if auto_deletion_time_after_completion_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.auto_deletion_time_after_completion_seconds is None
            and "auto_deletion_time_after_completion_seconds" in self.model_fields_set
        ):
            _dict["autoDeletionTimeAfterCompletionSeconds"] = None

        # set to None if backoff_limit (nullable) is None
        # and model_fields_set contains the field
        if self.backoff_limit is None and "backoff_limit" in self.model_fields_set:
            _dict["backoffLimit"] = None

        # set to None if annotations (nullable) is None
        # and model_fields_set contains the field
        if self.annotations is None and "annotations" in self.model_fields_set:
            _dict["annotations"] = None

        # set to None if labels (nullable) is None
        # and model_fields_set contains the field
        if self.labels is None and "labels" in self.model_fields_set:
            _dict["labels"] = None

        # set to None if connections (nullable) is None
        # and model_fields_set contains the field
        if self.connections is None and "connections" in self.model_fields_set:
            _dict["connections"] = None

        # set to None if allow_over_quota (nullable) is None
        # and model_fields_set contains the field
        if (
            self.allow_over_quota is None
            and "allow_over_quota" in self.model_fields_set
        ):
            _dict["allowOverQuota"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkspaceSpecificRunParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": obj.get("command"),
                "args": obj.get("args"),
                "runAsUid": obj.get("runAsUid"),
                "runAsGid": obj.get("runAsGid"),
                "supplementalGroups": obj.get("supplementalGroups"),
                "environmentVariables": (
                    [
                        EnvironmentVariable.from_dict(_item)
                        for _item in obj["environmentVariables"]
                    ]
                    if obj.get("environmentVariables") is not None
                    else None
                ),
                "nodeType": obj.get("nodeType"),
                "nodePools": obj.get("nodePools"),
                "podAffinity": (
                    PodAffinity.from_dict(obj["podAffinity"])
                    if obj.get("podAffinity") is not None
                    else None
                ),
                "terminateAfterPreemption": obj.get("terminateAfterPreemption"),
                "autoDeletionTimeAfterCompletionSeconds": obj.get(
                    "autoDeletionTimeAfterCompletionSeconds"
                ),
                "backoffLimit": obj.get("backoffLimit"),
                "annotations": (
                    [Annotation.from_dict(_item) for _item in obj["annotations"]]
                    if obj.get("annotations") is not None
                    else None
                ),
                "labels": (
                    [Label.from_dict(_item) for _item in obj["labels"]]
                    if obj.get("labels") is not None
                    else None
                ),
                "connections": (
                    [
                        SpecificRunConnectionInfo.from_dict(_item)
                        for _item in obj["connections"]
                    ]
                    if obj.get("connections") is not None
                    else None
                ),
                "allowOverQuota": obj.get("allowOverQuota"),
            }
        )
        return _obj
