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
from runai.models.auto_scaling_rules import AutoScalingRules
from runai.models.boolean_rules import BooleanRules
from runai.models.common_security_flat_fields_rules import CommonSecurityFlatFieldsRules
from runai.models.common_storage_fields_rules import CommonStorageFieldsRules
from runai.models.compute_fields_rules import ComputeFieldsRules
from runai.models.exposed_urls_rules import ExposedUrlsRules
from runai.models.image_pull_policy_rules import ImagePullPolicyRules
from runai.models.instances_rules import InstancesRules
from runai.models.pod_affinity_rules import PodAffinityRules
from runai.models.ports_rules import PortsRules
from runai.models.probes_rules import ProbesRules
from runai.models.related_urls_rules import RelatedUrlsRules
from runai.models.serving_port_rules import ServingPortRules
from runai.models.string_rules import StringRules
from typing import Optional, Set
from typing_extensions import Self


class InferencePolicyRulesV2(BaseModel):
    """
    Pydantic class model representing InferencePolicyRulesV2.

    Parameters:
        ```python
        command: Optional[StringRules]
        args: Optional[StringRules]
        image: Optional[StringRules]
        image_pull_policy: Optional[ImagePullPolicyRules]
        working_dir: Optional[StringRules]
        create_home_dir: Optional[BooleanRules]
        probes: Optional[ProbesRules]
        node_type: Optional[StringRules]
        node_pools: Optional[ArrayRules]
        pod_affinity: Optional[PodAffinityRules]
        environment_variables: Optional[InstancesRules]
        annotations: Optional[InstancesRules]
        labels: Optional[InstancesRules]
        tolerations: Optional[InstancesRules]
        ports: Optional[PortsRules]
        exposed_urls: Optional[ExposedUrlsRules]
        related_urls: Optional[RelatedUrlsRules]
        compute: Optional[ComputeFieldsRules]
        security: Optional[CommonSecurityFlatFieldsRules]
        storage: Optional[CommonStorageFieldsRules]
        serving_port: Optional[ServingPortRules]
        autoscaling: Optional[AutoScalingRules]
        ```
        command: See model StringRules for more information.
        args: See model StringRules for more information.
        image: See model StringRules for more information.
        image_pull_policy: See model ImagePullPolicyRules for more information.
        working_dir: See model StringRules for more information.
        create_home_dir: See model BooleanRules for more information.
        probes: See model ProbesRules for more information.
        node_type: See model StringRules for more information.
        node_pools: See model ArrayRules for more information.
        pod_affinity: See model PodAffinityRules for more information.
        environment_variables: See model InstancesRules for more information.
        annotations: See model InstancesRules for more information.
        labels: See model InstancesRules for more information.
        tolerations: See model InstancesRules for more information.
        ports: See model PortsRules for more information.
        exposed_urls: See model ExposedUrlsRules for more information.
        related_urls: See model RelatedUrlsRules for more information.
        compute: See model ComputeFieldsRules for more information.
        security: See model CommonSecurityFlatFieldsRules for more information.
        storage: See model CommonStorageFieldsRules for more information.
        serving_port: See model ServingPortRules for more information.
        autoscaling: See model AutoScalingRules for more information.
    Example:
        ```python
        InferencePolicyRulesV2(
            command=runai.models.string_rules.StringRules(),
                        args=runai.models.string_rules.StringRules(),
                        image=runai.models.string_rules.StringRules(),
                        image_pull_policy=runai.models.image_pull_policy_rules.ImagePullPolicyRules(),
                        working_dir=runai.models.string_rules.StringRules(),
                        create_home_dir=runai.models.boolean_rules.BooleanRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        probes=runai.models.probes_rules.ProbesRules(
                    readiness = runai.models.probe_rules.ProbeRules(
                        initial_delay_seconds = runai.models.integer_rules.IntegerRules(
                            source_of_rule = {"scope":"project","projectId":3},
                            required = True,
                            can_edit = True,
                            min = 56,
                            max = 56,
                            step = 56, ),
                        period_seconds = runai.models.integer_rules.IntegerRules(
                            required = True,
                            can_edit = True,
                            min = 56,
                            max = 56,
                            step = 56, ),
                        timeout_seconds = ,
                        success_threshold = ,
                        failure_threshold = ,
                        handler = runai.models.probe_handler_rules.ProbeHandlerRules(
                            http_get = runai.models.probe_handler_rules_http_get.ProbeHandlerRules_httpGet(
                                path = runai.models.string_rules.StringRules(),
                                port = ,
                                host = runai.models.string_rules.StringRules(),
                                scheme = runai.models.string_rules.StringRules(), ), ), ), ),
                        node_type=runai.models.string_rules.StringRules(),
                        node_pools=runai.models.array_rules.ArrayRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True, ),
                        pod_affinity=runai.models.pod_affinity_rules.PodAffinityRules(
                    type = runai.models.pod_affinity_type_rules.PodAffinityTypeRules(),
                    key = runai.models.string_rules.StringRules(), ),
                        environment_variables=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        annotations=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        labels=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        tolerations=runai.models.instances_rules.InstancesRules(
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        ports=runai.models.ports_rules.PortsRules(
                    attributes = runai.models.port_rules.PortRules(
                        container = runai.models.integer_rules.IntegerRules(
                            source_of_rule = {"scope":"project","projectId":3},
                            required = True,
                            can_edit = True,
                            min = 56,
                            max = 56,
                            step = 56, ),
                        service_type = runai.models.port_service_type_rules.PortServiceTypeRules(),
                        custom_external_port = runai.models.boolean_rules.BooleanRules(
                            required = True,
                            can_edit = True, ),
                        external = runai.models.integer_rules.IntegerRules(
                            required = True,
                            can_edit = True,
                            min = 56,
                            max = 56,
                            step = 56, ),
                        tool_type = runai.models.string_rules.StringRules(),
                        tool_name = runai.models.string_rules.StringRules(), ),
                    instances = runai.models.item_rules.ItemRules(
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        exposed_urls=runai.models.exposed_urls_rules.ExposedUrlsRules(
                    attributes = runai.models.exposed_url_rules.ExposedUrlRules(
                        container = runai.models.integer_rules.IntegerRules(
                            source_of_rule = {"scope":"project","projectId":3},
                            required = True,
                            can_edit = True,
                            min = 56,
                            max = 56,
                            step = 56, ),
                        custom_url = runai.models.boolean_rules.BooleanRules(
                            required = True,
                            can_edit = True, ),
                        url = runai.models.string_rules.StringRules(),
                        authorized_users = runai.models.array_rules.ArrayRules(
                            required = True,
                            can_edit = True, ),
                        tool_type = runai.models.string_rules.StringRules(),
                        tool_name = runai.models.string_rules.StringRules(), ),
                    instances = runai.models.item_rules.ItemRules(
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        related_urls=runai.models.related_urls_rules.RelatedUrlsRules(
                    attributes = runai.models.related_url_rules.RelatedUrlRules(
                        url = runai.models.string_rules.StringRules(),
                        type = runai.models.string_rules.StringRules(),
                        name = runai.models.string_rules.StringRules(), ),
                    instances = runai.models.item_rules.ItemRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        can_add = True,
                        locked = ["HOME","USER"], ), ),
                        compute=runai.models.compute_fields_rules.ComputeFieldsRules(),
                        security=runai.models.common_security_flat_fields_rules.CommonSecurityFlatFieldsRules(),
                        storage=runai.models.common_storage_fields_rules.CommonStorageFieldsRules(
                    data_volume = runai.models.data_volumes_rules.DataVolumesRules(
                        attributes = runai.models.data_volume_rules.DataVolumeRules(
                            id = runai.models.string_rules.StringRules(),
                            mount_path = runai.models.string_rules.StringRules(), ),
                        instances = runai.models.item_rules.ItemRules(
                            source_of_rule = {"scope":"project","projectId":3},
                            can_add = True,
                            locked = ["HOME","USER"], ), ),
                    pvc = runai.models.pvcs_rules.PvcsRules(),
                    git = runai.models.gits_rules.GitsRules(),
                    config_map_volume = runai.models.config_maps_rules.ConfigMapsRules(),
                    secret_volume = runai.models.secrets_rules.SecretsRules(), ),
                        serving_port=runai.models.serving_port_rules.ServingPortRules(
                    container = runai.models.integer_rules.IntegerRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    protocol = runai.models.serving_port_protocol_rules.ServingPortProtocolRules(), ),
                        autoscaling=runai.models.auto_scaling_rules.AutoScalingRules(
                    min_replicas = runai.models.integer_rules.IntegerRules(
                        source_of_rule = {"scope":"project","projectId":3},
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    max_replicas = runai.models.integer_rules.IntegerRules(
                        required = True,
                        can_edit = True,
                        min = 56,
                        max = 56,
                        step = 56, ),
                    metric = runai.models.auto_scaling_metric_rules.AutoScalingMetricRules(),
                    metric_threshold = ,
                    scale_to_zero_retention_seconds = , )
        )
        ```
    """  # noqa: E501

    command: Optional[StringRules] = None
    args: Optional[StringRules] = None
    image: Optional[StringRules] = None
    image_pull_policy: Optional[ImagePullPolicyRules] = Field(
        default=None, alias="imagePullPolicy"
    )
    working_dir: Optional[StringRules] = Field(default=None, alias="workingDir")
    create_home_dir: Optional[BooleanRules] = Field(default=None, alias="createHomeDir")
    probes: Optional[ProbesRules] = None
    node_type: Optional[StringRules] = Field(default=None, alias="nodeType")
    node_pools: Optional[ArrayRules] = Field(default=None, alias="nodePools")
    pod_affinity: Optional[PodAffinityRules] = Field(default=None, alias="podAffinity")
    environment_variables: Optional[InstancesRules] = Field(
        default=None, alias="environmentVariables"
    )
    annotations: Optional[InstancesRules] = None
    labels: Optional[InstancesRules] = None
    tolerations: Optional[InstancesRules] = None
    ports: Optional[PortsRules] = None
    exposed_urls: Optional[ExposedUrlsRules] = Field(default=None, alias="exposedUrls")
    related_urls: Optional[RelatedUrlsRules] = Field(default=None, alias="relatedUrls")
    compute: Optional[ComputeFieldsRules] = None
    security: Optional[CommonSecurityFlatFieldsRules] = None
    storage: Optional[CommonStorageFieldsRules] = None
    serving_port: Optional[ServingPortRules] = Field(default=None, alias="servingPort")
    autoscaling: Optional[AutoScalingRules] = None
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
        "ports",
        "exposedUrls",
        "relatedUrls",
        "compute",
        "security",
        "storage",
        "servingPort",
        "autoscaling",
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
        """Create an instance of InferencePolicyRulesV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of command
        if self.command:
            _dict["command"] = self.command.to_dict()
        # override the default output from pydantic by calling `to_dict()` of args
        if self.args:
            _dict["args"] = self.args.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict["image"] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image_pull_policy
        if self.image_pull_policy:
            _dict["imagePullPolicy"] = self.image_pull_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of working_dir
        if self.working_dir:
            _dict["workingDir"] = self.working_dir.to_dict()
        # override the default output from pydantic by calling `to_dict()` of create_home_dir
        if self.create_home_dir:
            _dict["createHomeDir"] = self.create_home_dir.to_dict()
        # override the default output from pydantic by calling `to_dict()` of probes
        if self.probes:
            _dict["probes"] = self.probes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_type
        if self.node_type:
            _dict["nodeType"] = self.node_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_pools
        if self.node_pools:
            _dict["nodePools"] = self.node_pools.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict["compute"] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict["security"] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serving_port
        if self.serving_port:
            _dict["servingPort"] = self.serving_port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of autoscaling
        if self.autoscaling:
            _dict["autoscaling"] = self.autoscaling.to_dict()
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

        # set to None if compute (nullable) is None
        # and model_fields_set contains the field
        if self.compute is None and "compute" in self.model_fields_set:
            _dict["compute"] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict["security"] = None

        # set to None if storage (nullable) is None
        # and model_fields_set contains the field
        if self.storage is None and "storage" in self.model_fields_set:
            _dict["storage"] = None

        # set to None if serving_port (nullable) is None
        # and model_fields_set contains the field
        if self.serving_port is None and "serving_port" in self.model_fields_set:
            _dict["servingPort"] = None

        # set to None if autoscaling (nullable) is None
        # and model_fields_set contains the field
        if self.autoscaling is None and "autoscaling" in self.model_fields_set:
            _dict["autoscaling"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InferencePolicyRulesV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "command": (
                    StringRules.from_dict(obj["command"])
                    if obj.get("command") is not None
                    else None
                ),
                "args": (
                    StringRules.from_dict(obj["args"])
                    if obj.get("args") is not None
                    else None
                ),
                "image": (
                    StringRules.from_dict(obj["image"])
                    if obj.get("image") is not None
                    else None
                ),
                "imagePullPolicy": (
                    ImagePullPolicyRules.from_dict(obj["imagePullPolicy"])
                    if obj.get("imagePullPolicy") is not None
                    else None
                ),
                "workingDir": (
                    StringRules.from_dict(obj["workingDir"])
                    if obj.get("workingDir") is not None
                    else None
                ),
                "createHomeDir": (
                    BooleanRules.from_dict(obj["createHomeDir"])
                    if obj.get("createHomeDir") is not None
                    else None
                ),
                "probes": (
                    ProbesRules.from_dict(obj["probes"])
                    if obj.get("probes") is not None
                    else None
                ),
                "nodeType": (
                    StringRules.from_dict(obj["nodeType"])
                    if obj.get("nodeType") is not None
                    else None
                ),
                "nodePools": (
                    ArrayRules.from_dict(obj["nodePools"])
                    if obj.get("nodePools") is not None
                    else None
                ),
                "podAffinity": (
                    PodAffinityRules.from_dict(obj["podAffinity"])
                    if obj.get("podAffinity") is not None
                    else None
                ),
                "environmentVariables": (
                    InstancesRules.from_dict(obj["environmentVariables"])
                    if obj.get("environmentVariables") is not None
                    else None
                ),
                "annotations": (
                    InstancesRules.from_dict(obj["annotations"])
                    if obj.get("annotations") is not None
                    else None
                ),
                "labels": (
                    InstancesRules.from_dict(obj["labels"])
                    if obj.get("labels") is not None
                    else None
                ),
                "tolerations": (
                    InstancesRules.from_dict(obj["tolerations"])
                    if obj.get("tolerations") is not None
                    else None
                ),
                "ports": (
                    PortsRules.from_dict(obj["ports"])
                    if obj.get("ports") is not None
                    else None
                ),
                "exposedUrls": (
                    ExposedUrlsRules.from_dict(obj["exposedUrls"])
                    if obj.get("exposedUrls") is not None
                    else None
                ),
                "relatedUrls": (
                    RelatedUrlsRules.from_dict(obj["relatedUrls"])
                    if obj.get("relatedUrls") is not None
                    else None
                ),
                "compute": (
                    ComputeFieldsRules.from_dict(obj["compute"])
                    if obj.get("compute") is not None
                    else None
                ),
                "security": (
                    CommonSecurityFlatFieldsRules.from_dict(obj["security"])
                    if obj.get("security") is not None
                    else None
                ),
                "storage": (
                    CommonStorageFieldsRules.from_dict(obj["storage"])
                    if obj.get("storage") is not None
                    else None
                ),
                "servingPort": (
                    ServingPortRules.from_dict(obj["servingPort"])
                    if obj.get("servingPort") is not None
                    else None
                ),
                "autoscaling": (
                    AutoScalingRules.from_dict(obj["autoscaling"])
                    if obj.get("autoscaling") is not None
                    else None
                ),
            }
        )
        return _obj
