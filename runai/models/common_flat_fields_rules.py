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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.array_rules import ArrayRules
from runai.models.boolean_rules import BooleanRules
from runai.models.image_pull_policy_rules import ImagePullPolicyRules
from runai.models.pod_affinity_rules import PodAffinityRules
from runai.models.probes_rules import ProbesRules
from runai.models.string_rules import StringRules
from typing import Optional, Set
from typing_extensions import Self


class CommonFlatFieldsRules(BaseModel):
    """
    Pydantic class model representing CommonFlatFieldsRules.

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
    Example:
        ```python
        CommonFlatFieldsRules(
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
                            step = 56,
                            default_from = runai.models.default_from_rule.DefaultFromRule(
                                field = '',
                                factor = 1.337, ), ),
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
                    options = [
                        {"value":"value","displayed":"A description of the value."}
                        ],
                    can_edit = True, ),
                        pod_affinity=runai.models.pod_affinity_rules.PodAffinityRules(
                    type = runai.models.pod_affinity_type_rules.PodAffinityTypeRules(),
                    key = runai.models.string_rules.StringRules(), )
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
        """Create an instance of CommonFlatFieldsRules from a JSON string"""
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
        """Create an instance of CommonFlatFieldsRules from a dict"""
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
            }
        )
        return _obj
