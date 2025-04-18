# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
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
from runai.models.compute_fields import ComputeFields
from runai.models.distributed_clean_pod_policy import DistributedCleanPodPolicy
from runai.models.distributed_framework import DistributedFramework
from runai.models.environment_variable import EnvironmentVariable
from runai.models.exposed_url import ExposedUrl
from runai.models.image_pull_policy import ImagePullPolicy
from runai.models.label import Label
from runai.models.pod_affinity import PodAffinity
from runai.models.port import Port
from runai.models.probes import Probes
from runai.models.related_url import RelatedUrl
from runai.models.restart_policy import RestartPolicy
from runai.models.security_flat_fields import SecurityFlatFields
from runai.models.storage_fields import StorageFields
from runai.models.toleration import Toleration
from typing import Optional, Set
from typing_extensions import Self


class DistributedSpecSpec(BaseModel):
    """
    Pydantic class model representing The spec of the worker(s)..

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
        tty: Optional[bool]
        stdin: Optional[bool]
        environment_variables: Optional[List[EnvironmentVariable]]
        annotations: Optional[List[Annotation]]
        labels: Optional[List[Label]]
        tolerations: Optional[List[Toleration]]
        terminate_after_preemption: Optional[bool]
        auto_deletion_time_after_completion_seconds: Optional[int]
        termination_grace_period_seconds: Optional[int]
        backoff_limit: Optional[int]
        restart_policy: Optional[RestartPolicy]
        ports: Optional[List[Port]]
        exposed_urls: Optional[List[ExposedUrl]]
        related_urls: Optional[List[RelatedUrl]]
        num_workers: Optional[int]
        distributed_framework: Optional[DistributedFramework]
        slots_per_worker: Optional[int]
        ssh_auth_mount_path: Optional[str]
        min_replicas: Optional[int]
        max_replicas: Optional[int]
        clean_pod_policy: Optional[DistributedCleanPodPolicy]
        compute: Optional[ComputeFields]
        storage: Optional[StorageFields]
        security: Optional[SecurityFlatFields]
        ```
        command: A command to the server as the entry point of the container running the workspace.
        args: Arguments to the command that the container running the workspace executes.
        image: Docker image name. For more information, see [Images](https://kubernetes.io/docs/concepts/containers/images). The image name is mandatory for creating a workspace.
        image_pull_policy: See model ImagePullPolicy for more information.
        working_dir: Container&#39;s working directory. If not specified, the container runtime default will be used. This may be configured in the container image.
        create_home_dir: When set to &#x60;true&#x60;, creates a home directory for the container.
        probes: See model Probes for more information.
        node_type: Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docshub.run.ai/guides/platform-management/aiinitiatives/organization/projects).
        node_pools: A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.
        pod_affinity: See model PodAffinity for more information.
        tty: Whether this container should allocate a TTY for itself, also requires &#39;stdin&#39; to be true.
        stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF
        environment_variables: Set of environment variables to populate into the container running the workspace.
        annotations: Set of annotations to populate into the container running the workspace.
        labels: Set of labels to populate into the container running the workspace.
        tolerations: Set of tolerations to apply to the workload.
        terminate_after_preemption: Indicates if the job should be terminated by the system after it has been preempted.
        auto_deletion_time_after_completion_seconds: Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.
        termination_grace_period_seconds: Duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down).
        backoff_limit: Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.
        restart_policy: See model RestartPolicy for more information.
        ports: Set of container ports that the workload exposes.
        exposed_urls: Set of container ports that the workload exposes via URLs.
        related_urls: Set of URLs that are related to the workload.
        num_workers: the number of workers that will be allocated for running the workload.
        distributed_framework: See model DistributedFramework for more information.
        slots_per_worker: Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI) - Default: 1
        ssh_auth_mount_path: Specifies the directory where SSH keys are mounted. (applicable only for MPI) - Default: &#39;/root/.ssh&#39;
        min_replicas: the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch)
        max_replicas: the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch)
        clean_pod_policy: See model DistributedCleanPodPolicy for more information.
        compute: See model ComputeFields for more information.
        storage: See model StorageFields for more information.
        security: See model SecurityFlatFields for more information.
    Example:
        ```python
        DistributedSpecSpec(
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
                    key = '', ),
                        tty=True,
                        stdin=True,
                        environment_variables=[
                    runai.models.environment_variable.EnvironmentVariable(
                        name = 'HOME',
                        value = '/home/my-folder',
                        secret = runai.models.environment_variable_secret.EnvironmentVariableSecret(
                            name = 'postgress_secret',
                            key = 'POSTGRES_PASSWORD', ),
                        config_map = runai.models.environment_variable_config_map.EnvironmentVariableConfigMap(
                            name = 'my-config-map',
                            key = 'MY_POSTGRES_SCHEMA', ),
                        pod_field_ref = runai.models.environment_variable_pod_field_reference.EnvironmentVariablePodFieldReference(
                            path = 'metadata.name', ),
                        exclude = False,
                        description = 'Home directory of the user.', )
                    ],
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
                        tolerations=[
                    runai.models.toleration.Toleration(
                        name = '0',
                        operator = 'Equal',
                        key = '',
                        value = '',
                        effect = 'NoSchedule',
                        seconds = 1,
                        exclude = False, )
                    ],
                        terminate_after_preemption=False,
                        auto_deletion_time_after_completion_seconds=15,
                        termination_grace_period_seconds=20,
                        backoff_limit=3,
                        restart_policy='Always',
                        ports=[
                    runai.models.port.Port(
                        container = 8080,
                        service_type = 'LoadBalancer',
                        external = 30080,
                        tool_type = 'pytorch',
                        tool_name = 'my-pytorch',
                        name = 'port-instance-a',
                        exclude = False, )
                    ],
                        exposed_urls=[
                    runai.models.exposed_url.ExposedUrl(
                        container = 8080,
                        url = 'https://my-url.com',
                        authorized_users = ["user-a","user-b"],
                        authorized_groups = ["group-a","group-b"],
                        tool_type = 'jupyter',
                        tool_name = 'my-pytorch',
                        name = 'url-instance-a',
                        exclude = False, )
                    ],
                        related_urls=[
                    runai.models.related_url.RelatedUrl(
                        url = 'https://my-url.com',
                        type = 'wandb',
                        name = 'url-instance-a',
                        exclude = False, )
                    ],
                        num_workers=1,
                        distributed_framework='MPI',
                        slots_per_worker=1,
                        ssh_auth_mount_path='/root/.ssh',
                        min_replicas=56,
                        max_replicas=56,
                        clean_pod_policy='None',
                        compute=runai.models.compute_fields.ComputeFields(),
                        storage=runai.models.storage_fields.StorageFields(),
                        security=runai.models.security_flat_fields.SecurityFlatFields()
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
        description="Nodes (machines), or a group of nodes on which the workload will run. To use this feature, your Administrator will need to label nodes. For more information, see [Group Nodes](https://docs.run.ai/latest/admin/researcher-setup/limit-to-node-group). When using this flag with with Project-based affinity, it refines the list of allowable node groups set in the Project. For more information, see [Projects](https://docshub.run.ai/guides/platform-management/aiinitiatives/organization/projects).",
        alias="nodeType",
    )
    node_pools: Optional[List[StrictStr]] = Field(
        default=None,
        description="A prioritized list of node pools for the scheduler to run the workspace on. The scheduler will always try to use the first node pool before moving to the next one if the first is not available.",
        alias="nodePools",
    )
    pod_affinity: Optional[PodAffinity] = Field(default=None, alias="podAffinity")
    tty: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.",
    )
    stdin: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF",
    )
    environment_variables: Optional[List[Optional[EnvironmentVariable]]] = Field(
        default=None,
        description="Set of environment variables to populate into the container running the workspace.",
        alias="environmentVariables",
    )
    annotations: Optional[List[Optional[Annotation]]] = Field(
        default=None,
        description="Set of annotations to populate into the container running the workspace.",
    )
    labels: Optional[List[Optional[Label]]] = Field(
        default=None,
        description="Set of labels to populate into the container running the workspace.",
    )
    tolerations: Optional[List[Optional[Toleration]]] = Field(
        default=None, description="Set of tolerations to apply to the workload."
    )
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
    termination_grace_period_seconds: Optional[
        Annotated[int, Field(strict=True, ge=0)]
    ] = Field(
        default=None,
        description="Duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down).",
        alias="terminationGracePeriodSeconds",
    )
    backoff_limit: Optional[StrictInt] = Field(
        default=None,
        description="Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.",
        alias="backoffLimit",
    )
    restart_policy: Optional[RestartPolicy] = Field(default=None, alias="restartPolicy")
    ports: Optional[List[Optional[Port]]] = Field(
        default=None, description="Set of container ports that the workload exposes."
    )
    exposed_urls: Optional[List[Optional[ExposedUrl]]] = Field(
        default=None,
        description="Set of container ports that the workload exposes via URLs.",
        alias="exposedUrls",
    )
    related_urls: Optional[List[Optional[RelatedUrl]]] = Field(
        default=None,
        description="Set of URLs that are related to the workload.",
        alias="relatedUrls",
    )
    num_workers: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="the number of workers that will be allocated for running the workload.",
        alias="numWorkers",
    )
    distributed_framework: Optional[DistributedFramework] = Field(
        default=None, alias="distributedFramework"
    )
    slots_per_worker: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=1,
        description="Specifies the number of slots per worker used in hostfile. Defaults to 1. (applicable only for MPI)",
        alias="slotsPerWorker",
    )
    ssh_auth_mount_path: Optional[StrictStr] = Field(
        default="/root/.ssh",
        description="Specifies the directory where SSH keys are mounted. (applicable only for MPI)",
        alias="sshAuthMountPath",
    )
    min_replicas: Optional[StrictInt] = Field(
        default=None,
        description="the lower limit for the number of worker pods to which the training job can scale down. (applicable only for PyTorch)",
        alias="minReplicas",
    )
    max_replicas: Optional[StrictInt] = Field(
        default=None,
        description="the upper limit for the number of worker pods that can be set by the autoscaler. Cannot be smaller than MinReplicas. (applicable only for PyTorch)",
        alias="maxReplicas",
    )
    clean_pod_policy: Optional[DistributedCleanPodPolicy] = Field(
        default=None, alias="cleanPodPolicy"
    )
    compute: Optional[ComputeFields] = None
    storage: Optional[StorageFields] = None
    security: Optional[SecurityFlatFields] = None
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
        "tty",
        "stdin",
        "environmentVariables",
        "annotations",
        "labels",
        "tolerations",
        "terminateAfterPreemption",
        "autoDeletionTimeAfterCompletionSeconds",
        "terminationGracePeriodSeconds",
        "backoffLimit",
        "restartPolicy",
        "ports",
        "exposedUrls",
        "relatedUrls",
        "numWorkers",
        "distributedFramework",
        "slotsPerWorker",
        "sshAuthMountPath",
        "minReplicas",
        "maxReplicas",
        "cleanPodPolicy",
        "compute",
        "storage",
        "security",
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
        """Create an instance of DistributedSpecSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in environment_variables (list)
        _items = []
        if self.environment_variables:
            for _item_environment_variables in self.environment_variables:
                if _item_environment_variables:
                    _items.append(_item_environment_variables.to_dict())
            _dict["environmentVariables"] = _items
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
        # override the default output from pydantic by calling `to_dict()` of each item in tolerations (list)
        _items = []
        if self.tolerations:
            for _item_tolerations in self.tolerations:
                if _item_tolerations:
                    _items.append(_item_tolerations.to_dict())
            _dict["tolerations"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item_ports in self.ports:
                if _item_ports:
                    _items.append(_item_ports.to_dict())
            _dict["ports"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exposed_urls (list)
        _items = []
        if self.exposed_urls:
            for _item_exposed_urls in self.exposed_urls:
                if _item_exposed_urls:
                    _items.append(_item_exposed_urls.to_dict())
            _dict["exposedUrls"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_urls (list)
        _items = []
        if self.related_urls:
            for _item_related_urls in self.related_urls:
                if _item_related_urls:
                    _items.append(_item_related_urls.to_dict())
            _dict["relatedUrls"] = _items
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict["compute"] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict["security"] = self.security.to_dict()
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

        # set to None if tty (nullable) is None
        # and model_fields_set contains the field
        if self.tty is None and "tty" in self.model_fields_set:
            _dict["tty"] = None

        # set to None if stdin (nullable) is None
        # and model_fields_set contains the field
        if self.stdin is None and "stdin" in self.model_fields_set:
            _dict["stdin"] = None

        # set to None if environment_variables (nullable) is None
        # and model_fields_set contains the field
        if (
            self.environment_variables is None
            and "environment_variables" in self.model_fields_set
        ):
            _dict["environmentVariables"] = None

        # set to None if annotations (nullable) is None
        # and model_fields_set contains the field
        if self.annotations is None and "annotations" in self.model_fields_set:
            _dict["annotations"] = None

        # set to None if labels (nullable) is None
        # and model_fields_set contains the field
        if self.labels is None and "labels" in self.model_fields_set:
            _dict["labels"] = None

        # set to None if tolerations (nullable) is None
        # and model_fields_set contains the field
        if self.tolerations is None and "tolerations" in self.model_fields_set:
            _dict["tolerations"] = None

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

        # set to None if termination_grace_period_seconds (nullable) is None
        # and model_fields_set contains the field
        if (
            self.termination_grace_period_seconds is None
            and "termination_grace_period_seconds" in self.model_fields_set
        ):
            _dict["terminationGracePeriodSeconds"] = None

        # set to None if backoff_limit (nullable) is None
        # and model_fields_set contains the field
        if self.backoff_limit is None and "backoff_limit" in self.model_fields_set:
            _dict["backoffLimit"] = None

        # set to None if restart_policy (nullable) is None
        # and model_fields_set contains the field
        if self.restart_policy is None and "restart_policy" in self.model_fields_set:
            _dict["restartPolicy"] = None

        # set to None if ports (nullable) is None
        # and model_fields_set contains the field
        if self.ports is None and "ports" in self.model_fields_set:
            _dict["ports"] = None

        # set to None if exposed_urls (nullable) is None
        # and model_fields_set contains the field
        if self.exposed_urls is None and "exposed_urls" in self.model_fields_set:
            _dict["exposedUrls"] = None

        # set to None if related_urls (nullable) is None
        # and model_fields_set contains the field
        if self.related_urls is None and "related_urls" in self.model_fields_set:
            _dict["relatedUrls"] = None

        # set to None if num_workers (nullable) is None
        # and model_fields_set contains the field
        if self.num_workers is None and "num_workers" in self.model_fields_set:
            _dict["numWorkers"] = None

        # set to None if distributed_framework (nullable) is None
        # and model_fields_set contains the field
        if (
            self.distributed_framework is None
            and "distributed_framework" in self.model_fields_set
        ):
            _dict["distributedFramework"] = None

        # set to None if slots_per_worker (nullable) is None
        # and model_fields_set contains the field
        if (
            self.slots_per_worker is None
            and "slots_per_worker" in self.model_fields_set
        ):
            _dict["slotsPerWorker"] = None

        # set to None if ssh_auth_mount_path (nullable) is None
        # and model_fields_set contains the field
        if (
            self.ssh_auth_mount_path is None
            and "ssh_auth_mount_path" in self.model_fields_set
        ):
            _dict["sshAuthMountPath"] = None

        # set to None if min_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.min_replicas is None and "min_replicas" in self.model_fields_set:
            _dict["minReplicas"] = None

        # set to None if max_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.max_replicas is None and "max_replicas" in self.model_fields_set:
            _dict["maxReplicas"] = None

        # set to None if clean_pod_policy (nullable) is None
        # and model_fields_set contains the field
        if (
            self.clean_pod_policy is None
            and "clean_pod_policy" in self.model_fields_set
        ):
            _dict["cleanPodPolicy"] = None

        # set to None if compute (nullable) is None
        # and model_fields_set contains the field
        if self.compute is None and "compute" in self.model_fields_set:
            _dict["compute"] = None

        # set to None if storage (nullable) is None
        # and model_fields_set contains the field
        if self.storage is None and "storage" in self.model_fields_set:
            _dict["storage"] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict["security"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistributedSpecSpec from a dict"""
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
                "tty": obj.get("tty"),
                "stdin": obj.get("stdin"),
                "environmentVariables": (
                    [
                        EnvironmentVariable.from_dict(_item)
                        for _item in obj["environmentVariables"]
                    ]
                    if obj.get("environmentVariables") is not None
                    else None
                ),
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
                "tolerations": (
                    [Toleration.from_dict(_item) for _item in obj["tolerations"]]
                    if obj.get("tolerations") is not None
                    else None
                ),
                "terminateAfterPreemption": obj.get("terminateAfterPreemption"),
                "autoDeletionTimeAfterCompletionSeconds": obj.get(
                    "autoDeletionTimeAfterCompletionSeconds"
                ),
                "terminationGracePeriodSeconds": obj.get(
                    "terminationGracePeriodSeconds"
                ),
                "backoffLimit": obj.get("backoffLimit"),
                "restartPolicy": obj.get("restartPolicy"),
                "ports": (
                    [Port.from_dict(_item) for _item in obj["ports"]]
                    if obj.get("ports") is not None
                    else None
                ),
                "exposedUrls": (
                    [ExposedUrl.from_dict(_item) for _item in obj["exposedUrls"]]
                    if obj.get("exposedUrls") is not None
                    else None
                ),
                "relatedUrls": (
                    [RelatedUrl.from_dict(_item) for _item in obj["relatedUrls"]]
                    if obj.get("relatedUrls") is not None
                    else None
                ),
                "numWorkers": obj.get("numWorkers"),
                "distributedFramework": obj.get("distributedFramework"),
                "slotsPerWorker": (
                    obj.get("slotsPerWorker")
                    if obj.get("slotsPerWorker") is not None
                    else 1
                ),
                "sshAuthMountPath": (
                    obj.get("sshAuthMountPath")
                    if obj.get("sshAuthMountPath") is not None
                    else "/root/.ssh"
                ),
                "minReplicas": obj.get("minReplicas"),
                "maxReplicas": obj.get("maxReplicas"),
                "cleanPodPolicy": obj.get("cleanPodPolicy"),
                "compute": (
                    ComputeFields.from_dict(obj["compute"])
                    if obj.get("compute") is not None
                    else None
                ),
                "storage": (
                    StorageFields.from_dict(obj["storage"])
                    if obj.get("storage") is not None
                    else None
                ),
                "security": (
                    SecurityFlatFields.from_dict(obj["security"])
                    if obj.get("security") is not None
                    else None
                ),
            }
        )
        return _obj
