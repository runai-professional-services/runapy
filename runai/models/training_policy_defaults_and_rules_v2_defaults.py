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
from runai.models.annotations_defaults import AnnotationsDefaults
from runai.models.compute_fields_defaults import ComputeFieldsDefaults
from runai.models.environment_variables_defaults import EnvironmentVariablesDefaults
from runai.models.exposed_urls_defaults import ExposedUrlsDefaults
from runai.models.image_pull_policy import ImagePullPolicy
from runai.models.labels_defaults import LabelsDefaults
from runai.models.pod_affinity import PodAffinity
from runai.models.ports_defaults import PortsDefaults
from runai.models.priority_class import PriorityClass
from runai.models.probes import Probes
from runai.models.related_urls_defaults import RelatedUrlsDefaults
from runai.models.restart_policy import RestartPolicy
from runai.models.security_flat_fields import SecurityFlatFields
from runai.models.storage_fields_defaults import StorageFieldsDefaults
from runai.models.tolerations_defaults import TolerationsDefaults
from typing import Optional, Set
from typing_extensions import Self


class TrainingPolicyDefaultsAndRulesV2Defaults(BaseModel):
    """
    Pydantic class model representing TrainingPolicyDefaultsAndRulesV2Defaults.

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
        environment_variables: Optional[EnvironmentVariablesDefaults]
        annotations: Optional[AnnotationsDefaults]
        labels: Optional[LabelsDefaults]
        tolerations: Optional[TolerationsDefaults]
        terminate_after_preemption: Optional[bool]
        auto_deletion_time_after_completion_seconds: Optional[int]
        termination_grace_period_seconds: Optional[int]
        backoff_limit: Optional[int]
        restart_policy: Optional[RestartPolicy]
        ports: Optional[PortsDefaults]
        exposed_urls: Optional[ExposedUrlsDefaults]
        related_urls: Optional[RelatedUrlsDefaults]
        priority_class: Optional[PriorityClass]
        completions: Optional[int]
        parallelism: Optional[int]
        security: Optional[SecurityFlatFields]
        compute: Optional[ComputeFieldsDefaults]
        storage: Optional[StorageFieldsDefaults]
        tty: Optional[bool]
        stdin: Optional[bool]
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
        environment_variables: See model EnvironmentVariablesDefaults for more information.
        annotations: See model AnnotationsDefaults for more information.
        labels: See model LabelsDefaults for more information.
        tolerations: See model TolerationsDefaults for more information.
        terminate_after_preemption: Indicates if the job should be terminated by the system after it has been preempted.
        auto_deletion_time_after_completion_seconds: Specifies the duration after which a finished workload (completed or failed) will be automatically deleted. The default is 30 days.
        termination_grace_period_seconds: Duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down).
        backoff_limit: Specifies the number of retries before marking a workload as failed (not applicable to Inference workloads). The default value is 6.
        restart_policy: See model RestartPolicy for more information.
        ports: See model PortsDefaults for more information.
        exposed_urls: See model ExposedUrlsDefaults for more information.
        related_urls: See model RelatedUrlsDefaults for more information.
        priority_class: See model PriorityClass for more information.
        completions: Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached (applicable to standard training only).
        parallelism: Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time (applicable to standard training only).
        security: See model SecurityFlatFields for more information.
        compute: See model ComputeFieldsDefaults for more information.
        storage: See model StorageFieldsDefaults for more information.
        tty: Whether this container should allocate a TTY for itself, also requires &#39;stdin&#39; to be true.
        stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF
    Example:
        ```python
        TrainingPolicyDefaultsAndRulesV2Defaults(
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
                        environment_variables=runai.models.environment_variables_defaults.EnvironmentVariablesDefaults(
                    instances = [
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
                        ], ),
                        annotations=runai.models.annotations_defaults.AnnotationsDefaults(
                    instances = [
                        runai.models.annotation.Annotation(
                            name = 'billing',
                            value = 'my-billing-unit',
                            exclude = False, )
                        ], ),
                        labels=runai.models.labels_defaults.LabelsDefaults(
                    instances = [
                        runai.models.label.Label(
                            name = 'stage',
                            value = 'initial-research',
                            exclude = False, )
                        ], ),
                        tolerations=runai.models.tolerations_defaults.TolerationsDefaults(
                    attributes = runai.models.toleration.Toleration(
                        name = '0',
                        operator = 'Equal',
                        key = '',
                        value = '',
                        effect = 'NoSchedule',
                        seconds = 1,
                        exclude = False, ),
                    instances = [
                        runai.models.toleration.Toleration(
                            name = '0',
                            key = '',
                            value = '',
                            seconds = 1,
                            exclude = False, )
                        ], ),
                        terminate_after_preemption=False,
                        auto_deletion_time_after_completion_seconds=15,
                        termination_grace_period_seconds=20,
                        backoff_limit=3,
                        restart_policy='Always',
                        ports=runai.models.ports_defaults.PortsDefaults(
                    attributes = runai.models.port.Port(
                        container = 8080,
                        service_type = 'LoadBalancer',
                        external = 30080,
                        tool_type = 'pytorch',
                        tool_name = 'my-pytorch',
                        name = 'port-instance-a',
                        exclude = False, ),
                    instances = [
                        runai.models.port.Port(
                            container = 8080,
                            external = 30080,
                            tool_type = 'pytorch',
                            tool_name = 'my-pytorch',
                            name = 'port-instance-a',
                            exclude = False, )
                        ], ),
                        exposed_urls=runai.models.exposed_urls_defaults.ExposedUrlsDefaults(
                    attributes = runai.models.exposed_url.ExposedUrl(
                        container = 8080,
                        url = 'https://my-url.com',
                        authorized_users = ["user-a","user-b"],
                        authorized_groups = ["group-a","group-b"],
                        tool_type = 'jupyter',
                        tool_name = 'my-pytorch',
                        name = 'url-instance-a',
                        exclude = False, ),
                    instances = [
                        runai.models.exposed_url.ExposedUrl(
                            container = 8080,
                            url = 'https://my-url.com',
                            authorized_users = ["user-a","user-b"],
                            authorized_groups = ["group-a","group-b"],
                            tool_type = 'jupyter',
                            tool_name = 'my-pytorch',
                            name = 'url-instance-a',
                            exclude = False, )
                        ], ),
                        related_urls=runai.models.related_urls_defaults.RelatedUrlsDefaults(
                    attributes = runai.models.related_url.RelatedUrl(
                        url = 'https://my-url.com',
                        type = 'wandb',
                        name = 'url-instance-a',
                        exclude = False, ),
                    instances = [
                        runai.models.related_url.RelatedUrl(
                            url = 'https://my-url.com',
                            type = 'wandb',
                            name = 'url-instance-a',
                            exclude = False, )
                        ], ),
                        priority_class='build',
                        completions=1,
                        parallelism=1,
                        security=runai.models.security_flat_fields.SecurityFlatFields(),
                        compute=runai.models.compute_fields_defaults.ComputeFieldsDefaults(),
                        storage=runai.models.storage_fields_defaults.StorageFieldsDefaults(),
                        tty=True,
                        stdin=True
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
    environment_variables: Optional[EnvironmentVariablesDefaults] = Field(
        default=None, alias="environmentVariables"
    )
    annotations: Optional[AnnotationsDefaults] = None
    labels: Optional[LabelsDefaults] = None
    tolerations: Optional[TolerationsDefaults] = None
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
    ports: Optional[PortsDefaults] = None
    exposed_urls: Optional[ExposedUrlsDefaults] = Field(
        default=None, alias="exposedUrls"
    )
    related_urls: Optional[RelatedUrlsDefaults] = Field(
        default=None, alias="relatedUrls"
    )
    priority_class: Optional[PriorityClass] = Field(default=None, alias="priorityClass")
    completions: Optional[StrictInt] = Field(
        default=None,
        description="Used with Hyperparameter Optimization. Specifies the number of successful pods the job should reach to be completed. The Job will be marked as successful once the specified amount of pods has been reached (applicable to standard training only).",
    )
    parallelism: Optional[StrictInt] = Field(
        default=None,
        description="Used with Hyperparameter Optimization. Specifies the maximum number of pods the workload should run at any given time (applicable to standard training only).",
    )
    security: Optional[SecurityFlatFields] = None
    compute: Optional[ComputeFieldsDefaults] = None
    storage: Optional[StorageFieldsDefaults] = None
    tty: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.",
    )
    stdin: Optional[StrictBool] = Field(
        default=None,
        description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF",
    )
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
        "priorityClass",
        "completions",
        "parallelism",
        "security",
        "compute",
        "storage",
        "tty",
        "stdin",
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
        """Create an instance of TrainingPolicyDefaultsAndRulesV2Defaults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environment_variables
        if self.environment_variables:
            _dict["environmentVariables"] = self.environment_variables.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict["annotations"] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict["labels"] = self.labels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tolerations
        if self.tolerations:
            _dict["tolerations"] = self.tolerations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ports
        if self.ports:
            _dict["ports"] = self.ports.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposed_urls
        if self.exposed_urls:
            _dict["exposedUrls"] = self.exposed_urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_urls
        if self.related_urls:
            _dict["relatedUrls"] = self.related_urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict["security"] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict["compute"] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
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

        # set to None if priority_class (nullable) is None
        # and model_fields_set contains the field
        if self.priority_class is None and "priority_class" in self.model_fields_set:
            _dict["priorityClass"] = None

        # set to None if completions (nullable) is None
        # and model_fields_set contains the field
        if self.completions is None and "completions" in self.model_fields_set:
            _dict["completions"] = None

        # set to None if parallelism (nullable) is None
        # and model_fields_set contains the field
        if self.parallelism is None and "parallelism" in self.model_fields_set:
            _dict["parallelism"] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict["security"] = None

        # set to None if compute (nullable) is None
        # and model_fields_set contains the field
        if self.compute is None and "compute" in self.model_fields_set:
            _dict["compute"] = None

        # set to None if storage (nullable) is None
        # and model_fields_set contains the field
        if self.storage is None and "storage" in self.model_fields_set:
            _dict["storage"] = None

        # set to None if tty (nullable) is None
        # and model_fields_set contains the field
        if self.tty is None and "tty" in self.model_fields_set:
            _dict["tty"] = None

        # set to None if stdin (nullable) is None
        # and model_fields_set contains the field
        if self.stdin is None and "stdin" in self.model_fields_set:
            _dict["stdin"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrainingPolicyDefaultsAndRulesV2Defaults from a dict"""
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
                "environmentVariables": (
                    EnvironmentVariablesDefaults.from_dict(obj["environmentVariables"])
                    if obj.get("environmentVariables") is not None
                    else None
                ),
                "annotations": (
                    AnnotationsDefaults.from_dict(obj["annotations"])
                    if obj.get("annotations") is not None
                    else None
                ),
                "labels": (
                    LabelsDefaults.from_dict(obj["labels"])
                    if obj.get("labels") is not None
                    else None
                ),
                "tolerations": (
                    TolerationsDefaults.from_dict(obj["tolerations"])
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
                    PortsDefaults.from_dict(obj["ports"])
                    if obj.get("ports") is not None
                    else None
                ),
                "exposedUrls": (
                    ExposedUrlsDefaults.from_dict(obj["exposedUrls"])
                    if obj.get("exposedUrls") is not None
                    else None
                ),
                "relatedUrls": (
                    RelatedUrlsDefaults.from_dict(obj["relatedUrls"])
                    if obj.get("relatedUrls") is not None
                    else None
                ),
                "priorityClass": obj.get("priorityClass"),
                "completions": obj.get("completions"),
                "parallelism": obj.get("parallelism"),
                "security": (
                    SecurityFlatFields.from_dict(obj["security"])
                    if obj.get("security") is not None
                    else None
                ),
                "compute": (
                    ComputeFieldsDefaults.from_dict(obj["compute"])
                    if obj.get("compute") is not None
                    else None
                ),
                "storage": (
                    StorageFieldsDefaults.from_dict(obj["storage"])
                    if obj.get("storage") is not None
                    else None
                ),
                "tty": obj.get("tty"),
                "stdin": obj.get("stdin"),
            }
        )
        return _obj
