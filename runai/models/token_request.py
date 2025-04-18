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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class TokenRequest(BaseModel):
    """
    Pydantic class model representing TokenRequest.

    Parameters:
        ```python
        grant_type: str
        app_id: str
        app_secret: str
        code: str
        redirect_uri: str
        refresh_token: str
        username: str
        password: str
        client_id: str
        client_secret: str
        ```
        grant_type: See model str for more information.
        app_id: See model str for more information.
        app_secret: See model str for more information.
        code: See model str for more information.
        redirect_uri: See model str for more information.
        refresh_token: See model str for more information.
        username: See model str for more information.
        password: See model str for more information.
        client_id: See model str for more information.
        client_secret: See model str for more information.
    Example:
        ```python
        TokenRequest(
            grant_type='app_token',
                        app_id='',
                        app_secret='',
                        code='',
                        redirect_uri='',
                        refresh_token='',
                        username='',
                        password='',
                        client_id='',
                        client_secret=''
        )
        ```
    """  # noqa: E501

    grant_type: Optional[StrictStr] = Field(default=None, alias="grantType")
    app_id: Optional[StrictStr] = Field(default=None, alias="appID")
    app_secret: Optional[StrictStr] = Field(default=None, alias="appSecret")
    code: Optional[StrictStr] = None
    redirect_uri: Optional[StrictStr] = Field(default=None, alias="redirectUri")
    refresh_token: Optional[StrictStr] = Field(default=None, alias="refreshToken")
    username: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = Field(default=None, alias="clientID")
    client_secret: Optional[StrictStr] = Field(default=None, alias="clientSecret")
    __properties: ClassVar[List[str]] = [
        "grantType",
        "appID",
        "appSecret",
        "code",
        "redirectUri",
        "refreshToken",
        "username",
        "password",
        "clientID",
        "clientSecret",
    ]

    @field_validator("grant_type")
    def grant_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "app_token",
                "client_credentials",
                "refresh_token",
                "exchange_token",
                "password",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('app_token', 'client_credentials', 'refresh_token', 'exchange_token', 'password')"
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
        """Create an instance of TokenRequest from a JSON string"""
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
        """Create an instance of TokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "grantType": obj.get("grantType"),
                "appID": obj.get("appID"),
                "appSecret": obj.get("appSecret"),
                "code": obj.get("code"),
                "redirectUri": obj.get("redirectUri"),
                "refreshToken": obj.get("refreshToken"),
                "username": obj.get("username"),
                "password": obj.get("password"),
                "clientID": obj.get("clientID"),
                "clientSecret": obj.get("clientSecret"),
            }
        )
        return _obj
