# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class PolicyReadOnlyFields(BaseModel):
    """
    Pydantic class model representing PolicyReadOnlyFields.

    Parameters:
        ```python
        id: str
        tenant_id: int
        cluster_id: Optional[str]
        created_by: str
        created_at: datetime
        updated_by: str
        updated_at: datetime
        ```
        id: The unique id of the policy.
        tenant_id: The id of the tenant.
        cluster_id: The id of the cluster.
        created_by: The user who created the policy.
        created_at: The time at which the policy wes created
        updated_by: The user who updated the policy.
        updated_at: The time at which the policy has been updated
    Example:
        ```python
        PolicyReadOnlyFields(
            id='0',
                        tenant_id=1001,
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        created_by='0',
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_by='0',
                        updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
        )
        ```
    """  # noqa: E501

    id: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The unique id of the policy."
    )
    tenant_id: Optional[StrictInt] = Field(
        default=None, description="The id of the tenant.", alias="tenantId"
    )
    cluster_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The id of the cluster.", alias="clusterId"
    )
    created_by: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The user who created the policy.", alias="createdBy"
    )
    created_at: datetime = Field(
        description="The time at which the policy wes created", alias="createdAt"
    )
    updated_by: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The user who updated the policy.", alias="updatedBy"
    )
    updated_at: datetime = Field(
        description="The time at which the policy has been updated", alias="updatedAt"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "tenantId",
        "clusterId",
        "createdBy",
        "createdAt",
        "updatedBy",
        "updatedAt",
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
        """Create an instance of PolicyReadOnlyFields from a JSON string"""
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
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict["clusterId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PolicyReadOnlyFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "tenantId": obj.get("tenantId"),
                "clusterId": obj.get("clusterId"),
                "createdBy": obj.get("createdBy"),
                "createdAt": obj.get("createdAt"),
                "updatedBy": obj.get("updatedBy"),
                "updatedAt": obj.get("updatedAt"),
            }
        )
        return _obj
