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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class PolicySyncStatusOfCluster(BaseModel):
    """
    Pydantic class model representing PolicySyncStatusOfCluster.

    Parameters:
        ```python
        cluster_id: str
        status: str
        error_message: Optional[str]
        ```
        cluster_id: The id of the cluster.
        status: Policy sync status of the cluster
        error_message: In case sync failed, holds the error message received from the cluster
    Example:
        ```python
        PolicySyncStatusOfCluster(
            cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        status='Not ready',
                        error_message=''
        )
        ```
    """  # noqa: E501

    cluster_id: StrictStr = Field(
        description="The id of the cluster.", alias="clusterId"
    )
    status: StrictStr = Field(description="Policy sync status of the cluster")
    error_message: Optional[StrictStr] = Field(
        default=None,
        description="In case sync failed, holds the error message received from the cluster",
        alias="errorMessage",
    )
    __properties: ClassVar[List[str]] = ["clusterId", "status", "errorMessage"]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            [
                "Not ready",
                "Applying",
                "Failed",
                "Ready",
                "Pending deletion",
                "Deleting",
                "Deleted",
                "Deletion failed",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('Not ready', 'Applying', 'Failed', 'Ready', 'Pending deletion', 'Deleting', 'Deleted', 'Deletion failed')"
            )
        return value

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
        """Create an instance of PolicySyncStatusOfCluster from a JSON string"""
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
        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict["errorMessage"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PolicySyncStatusOfCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "clusterId": obj.get("clusterId"),
                "status": obj.get("status"),
                "errorMessage": obj.get("errorMessage"),
            }
        )
        return _obj
