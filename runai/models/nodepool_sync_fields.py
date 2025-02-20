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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.nodepool_phase import NodepoolPhase
from runai.models.nodepool_sync_fields_status import NodepoolSyncFieldsStatus
from typing import Optional, Set
from typing_extensions import Self


class NodepoolSyncFields(BaseModel):
    """
    Pydantic class model representing NodepoolSyncFields.

    Parameters:
        ```python
        name: str
        phase: NodepoolPhase
        phase_message: str
        status: NodepoolSyncFieldsStatus
        ```
        name: See model str for more information.
        phase: See model NodepoolPhase for more information.
        phase_message: Message for status of Node Pool
        status: See model NodepoolSyncFieldsStatus for more information.
    Example:
        ```python
        NodepoolSyncFields(
            name='v100',
                        phase='Creating',
                        phase_message='all nodes are down',
                        status="example"
        )
        ```
    """  # noqa: E501

    name: StrictStr
    phase: Optional[NodepoolPhase] = None
    phase_message: Optional[StrictStr] = Field(
        default=None,
        description="Message for status of Node Pool",
        alias="phaseMessage",
    )
    status: Optional[NodepoolSyncFieldsStatus] = None
    __properties: ClassVar[List[str]] = ["name", "phase", "phaseMessage", "status"]

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
        """Create an instance of NodepoolSyncFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodepoolSyncFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "phase": obj.get("phase"),
                "phaseMessage": obj.get("phaseMessage"),
                "status": (
                    NodepoolSyncFieldsStatus.from_dict(obj["status"])
                    if obj.get("status") is not None
                    else None
                ),
            }
        )
        return _obj
