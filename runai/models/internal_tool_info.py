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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.external_url_info import ExternalUrlInfo
from runai.models.internal_connection_type import InternalConnectionType
from runai.models.internal_tool_type import InternalToolType
from runai.models.node_port_info import NodePortInfo
from runai.models.serving_port_info import ServingPortInfo
from typing import Optional, Set
from typing_extensions import Self


class InternalToolInfo(BaseModel):
    """
    Pydantic class model representing Information of the internal tool..

    Parameters:
        ```python
        tool_type: InternalToolType
        connection_type: InternalConnectionType
        container_port: int
        node_port_info: Optional[NodePortInfo]
        external_url_info: Optional[ExternalUrlInfo]
        serving_port_info: Optional[ServingPortInfo]
        ```
        tool_type: See model InternalToolType for more information.
        connection_type: See model InternalConnectionType for more information.
        container_port: The port within the container that the connection exposes.
        node_port_info: See model NodePortInfo for more information.
        external_url_info: See model ExternalUrlInfo for more information.
        serving_port_info: See model ServingPortInfo for more information.
    Example:
        ```python
        InternalToolInfo(
            tool_type='jupyter-notebook',
                        connection_type='LoadBalancer',
                        container_port=1,
                        node_port_info=runai.models.node_port_info.NodePortInfo(
                    is_custom_port = True, ),
                        external_url_info=runai.models.external_url_info.ExternalUrlInfo(
                    is_custom_url = True,
                    external_url = '0', ),
                        serving_port_info=runai.models.serving_port_info.ServingPortInfo(
                    protocol = 'grpc', )
        )
        ```
    """  # noqa: E501

    tool_type: InternalToolType = Field(alias="toolType")
    connection_type: InternalConnectionType = Field(alias="connectionType")
    container_port: Annotated[int, Field(le=65535, strict=True, ge=1)] = Field(
        description="The port within the container that the connection exposes.",
        alias="containerPort",
    )
    node_port_info: Optional[NodePortInfo] = Field(default=None, alias="nodePortInfo")
    external_url_info: Optional[ExternalUrlInfo] = Field(
        default=None, alias="externalUrlInfo"
    )
    serving_port_info: Optional[ServingPortInfo] = Field(
        default=None, alias="servingPortInfo"
    )
    __properties: ClassVar[List[str]] = [
        "toolType",
        "connectionType",
        "containerPort",
        "nodePortInfo",
        "externalUrlInfo",
        "servingPortInfo",
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
        """Create an instance of InternalToolInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of node_port_info
        if self.node_port_info:
            _dict["nodePortInfo"] = self.node_port_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_url_info
        if self.external_url_info:
            _dict["externalUrlInfo"] = self.external_url_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serving_port_info
        if self.serving_port_info:
            _dict["servingPortInfo"] = self.serving_port_info.to_dict()
        # set to None if node_port_info (nullable) is None
        # and model_fields_set contains the field
        if self.node_port_info is None and "node_port_info" in self.model_fields_set:
            _dict["nodePortInfo"] = None

        # set to None if external_url_info (nullable) is None
        # and model_fields_set contains the field
        if (
            self.external_url_info is None
            and "external_url_info" in self.model_fields_set
        ):
            _dict["externalUrlInfo"] = None

        # set to None if serving_port_info (nullable) is None
        # and model_fields_set contains the field
        if (
            self.serving_port_info is None
            and "serving_port_info" in self.model_fields_set
        ):
            _dict["servingPortInfo"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InternalToolInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "toolType": obj.get("toolType"),
                "connectionType": obj.get("connectionType"),
                "containerPort": obj.get("containerPort"),
                "nodePortInfo": (
                    NodePortInfo.from_dict(obj["nodePortInfo"])
                    if obj.get("nodePortInfo") is not None
                    else None
                ),
                "externalUrlInfo": (
                    ExternalUrlInfo.from_dict(obj["externalUrlInfo"])
                    if obj.get("externalUrlInfo") is not None
                    else None
                ),
                "servingPortInfo": (
                    ServingPortInfo.from_dict(obj["servingPortInfo"])
                    if obj.get("servingPortInfo") is not None
                    else None
                ),
            }
        )
        return _obj
