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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.role import Role
from typing import Optional, Set
from typing_extensions import Self


class GroupCreationRequest(BaseModel):
    """
    Pydantic class model representing GroupCreationRequest.

    Parameters:
        ```python
        username: str
        email: str
        roles: List[Role]
        entity_type: str
        tenant_id: int
        permit_all_clusters: bool
        user_id: str
        permitted_clusters: List[str]
        created_by: str
        ```
        username: Group&#39;s name
        email: Empty email address
        roles: See model List[Role] for more information.
        entity_type: See model str for more information.
        tenant_id: The id of the tenant.
        permit_all_clusters: See model bool for more information.
        user_id: Group&#39;s name
        permitted_clusters: See model List[str] for more information.
        created_by: uid of the user
    Example:
        ```python
        GroupCreationRequest(
            username='group1',
                        email='',
                        roles=[
                    'viewer'
                    ],
                        entity_type='sso-user',
                        tenant_id=1001,
                        permit_all_clusters=False,
                        user_id='group1',
                        permitted_clusters=[
                    '71f69d83-ba66-4822-adf5-55ce55efd210'
                    ],
                        created_by='aaaaa-3333-4444-bbbbbb-111'
        )
        ```
    """  # noqa: E501

    username: StrictStr = Field(description="Group's name")
    email: StrictStr = Field(description="Empty email address")
    roles: List[Role]
    entity_type: Optional[StrictStr] = Field(default=None, alias="entityType")
    tenant_id: Optional[StrictInt] = Field(
        default=None, description="The id of the tenant.", alias="tenantId"
    )
    permit_all_clusters: Optional[StrictBool] = Field(
        default=None, alias="permitAllClusters"
    )
    user_id: Optional[StrictStr] = Field(
        default=None, description="Group's name", alias="userId"
    )
    permitted_clusters: Optional[List[StrictStr]] = Field(
        default=None, alias="permittedClusters"
    )
    created_by: Optional[StrictStr] = Field(
        default=None, description="uid of the user", alias="createdBy"
    )
    __properties: ClassVar[List[str]] = [
        "username",
        "email",
        "roles",
        "entityType",
        "tenantId",
        "permitAllClusters",
        "userId",
        "permittedClusters",
        "createdBy",
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
        """Create an instance of GroupCreationRequest from a JSON string"""
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
        """Create an instance of GroupCreationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "username": obj.get("username"),
                "email": obj.get("email"),
                "roles": obj.get("roles"),
                "entityType": obj.get("entityType"),
                "tenantId": obj.get("tenantId"),
                "permitAllClusters": obj.get("permitAllClusters"),
                "userId": obj.get("userId"),
                "permittedClusters": obj.get("permittedClusters"),
                "createdBy": obj.get("createdBy"),
            }
        )
        return _obj
