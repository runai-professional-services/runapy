# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictStr,
    ValidationError,
    field_validator,
)
from typing import Optional
from runai.models.auto_redirect_sso_setting import AutoRedirectSsoSetting
from runai.models.exclude_groups_from_token_setting import ExcludeGroupsFromTokenSetting
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

UPDATEIDMSETTINGBYKEYREQUEST_ANY_OF_SCHEMAS = [
    "AutoRedirectSsoSetting",
    "ExcludeGroupsFromTokenSetting",
]


class UpdateIdmSettingByKeyRequest(BaseModel):
    """
    UpdateIdmSettingByKeyRequest
    """

    # data type: AutoRedirectSsoSetting
    anyof_schema_1_validator: Optional[AutoRedirectSsoSetting] = None
    # data type: ExcludeGroupsFromTokenSetting
    anyof_schema_2_validator: Optional[ExcludeGroupsFromTokenSetting] = None
    if TYPE_CHECKING:
        actual_instance: Optional[
            Union[AutoRedirectSsoSetting, ExcludeGroupsFromTokenSetting]
        ] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = {
        "AutoRedirectSsoSetting",
        "ExcludeGroupsFromTokenSetting",
    }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        instance = UpdateIdmSettingByKeyRequest.model_construct()
        error_messages = []
        # validate data type: AutoRedirectSsoSetting
        if not isinstance(v, AutoRedirectSsoSetting):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `AutoRedirectSsoSetting`"
            )
        else:
            return v

        # validate data type: ExcludeGroupsFromTokenSetting
        if not isinstance(v, ExcludeGroupsFromTokenSetting):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `ExcludeGroupsFromTokenSetting`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in UpdateIdmSettingByKeyRequest with anyOf schemas: AutoRedirectSsoSetting, ExcludeGroupsFromTokenSetting. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[AutoRedirectSsoSetting] = None
        try:
            instance.actual_instance = AutoRedirectSsoSetting.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ExcludeGroupsFromTokenSetting] = None
        try:
            instance.actual_instance = ExcludeGroupsFromTokenSetting.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into UpdateIdmSettingByKeyRequest with anyOf schemas: AutoRedirectSsoSetting, ExcludeGroupsFromTokenSetting. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(
        self,
    ) -> Optional[
        Union[Dict[str, Any], AutoRedirectSsoSetting, ExcludeGroupsFromTokenSetting]
    ]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
