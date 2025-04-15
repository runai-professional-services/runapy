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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.auth_entity_type import AuthEntityType
from runai.models.role import Role
from typing import Optional, Set
from typing_extensions import Self


class App(BaseModel):
    """
    Pydantic class model representing App.

    Parameters:
        ```python
        entity_type: AuthEntityType
        tenant_id: int
        user_id: str
        permit_all_clusters: bool
        permitted_clusters: List[str]
        roles: List[Role]
        created_at: datetime
        client_id: str
        name: str
        revoked: bool
        ```
        entity_type: See model AuthEntityType for more information.
        tenant_id: The id of the tenant.
        user_id: Unique identifier of the user
        permit_all_clusters: See model bool for more information.
        permitted_clusters: A list of clusters that the user or application can access.
        roles: See model List[Role] for more information.
        created_at: The creation date of the application.
        client_id: The client ID of the application.
        name: The name of the application.
        revoked: Whether the application has been revoked.
    Example:
        ```python
        App(
            entity_type='regular-user',
                        tenant_id=1001,
                        user_id='4008188b-ab50-4aa5-a3f2-b78091ccf92d',
                        permit_all_clusters=False,
                        permitted_clusters=[
                    '71f69d83-ba66-4822-adf5-55ce55efd210'
                    ],
                        roles=[
                    'viewer'
                    ],
                        created_at='2021-12-14T16:04:15.099Z',
                        client_id='6d2894ba-f998-4039-bba1-caba57caf681',
                        name='MyApplication',
                        revoked=False
        )
        ```
    """  # noqa: E501

    entity_type: Optional[AuthEntityType] = Field(default=None, alias="entityType")
    tenant_id: Optional[StrictInt] = Field(
        default=None, description="The id of the tenant.", alias="tenantId"
    )
    user_id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the user", alias="userId"
    )
    permit_all_clusters: Optional[StrictBool] = Field(
        default=None, alias="permitAllClusters"
    )
    permitted_clusters: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of clusters that the user or application can access.",
        alias="permittedClusters",
    )
    roles: Optional[List[Role]] = None
    created_at: Optional[datetime] = Field(
        default=None,
        description="The creation date of the application.",
        alias="createdAt",
    )
    client_id: Optional[StrictStr] = Field(
        default=None, description="The client ID of the application.", alias="clientId"
    )
    name: StrictStr = Field(description="The name of the application.")
    revoked: Optional[StrictBool] = Field(
        default=None, description="Whether the application has been revoked."
    )
    __properties: ClassVar[List[str]] = [
        "entityType",
        "tenantId",
        "userId",
        "permitAllClusters",
        "permittedClusters",
        "roles",
        "createdAt",
        "clientId",
        "name",
        "revoked",
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
        """Create an instance of App from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of App from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "entityType": obj.get("entityType"),
                "tenantId": obj.get("tenantId"),
                "userId": obj.get("userId"),
                "permitAllClusters": obj.get("permitAllClusters"),
                "permittedClusters": obj.get("permittedClusters"),
                "roles": obj.get("roles"),
                "createdAt": obj.get("createdAt"),
                "clientId": obj.get("clientId"),
                "name": obj.get("name"),
                "revoked": obj.get("revoked"),
            }
        )
        return _obj
