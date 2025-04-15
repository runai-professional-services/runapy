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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class ConfigMapInstance(BaseModel):
    """
    Pydantic class model representing ConfigMapInstance.

    Parameters:
        ```python
        name: Optional[str]
        config_map: Optional[str]
        mount_path: Optional[str]
        exclude: Optional[bool]
        ```
        name: unique name to identify the instance. primarily used for policy locked rules.
        config_map: The name of the ConfigMap resource. (mandatory)
        mount_path: Local path within the workspace to which the ConfigMap will be mapped to. (mandatory)
        exclude: Use &#39;true&#39; in case the item is defined in defaults of the policy, and you wish to exclude it from the workload. - Default: False
    Example:
        ```python
        ConfigMapInstance(
            name='storage-instance-a',
                        config_map='0',
                        mount_path='0',
                        exclude=False
        )
        ```
    """  # noqa: E501

    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="unique name to identify the instance. primarily used for policy locked rules.",
    )
    config_map: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="The name of the ConfigMap resource. (mandatory)",
        alias="configMap",
    )
    mount_path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Local path within the workspace to which the ConfigMap will be mapped to. (mandatory)",
        alias="mountPath",
    )
    exclude: Optional[StrictBool] = Field(
        default=False,
        description="Use 'true' in case the item is defined in defaults of the policy, and you wish to exclude it from the workload.",
    )
    __properties: ClassVar[List[str]] = ["name", "configMap", "mountPath", "exclude"]

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
        """Create an instance of ConfigMapInstance from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if config_map (nullable) is None
        # and model_fields_set contains the field
        if self.config_map is None and "config_map" in self.model_fields_set:
            _dict["configMap"] = None

        # set to None if mount_path (nullable) is None
        # and model_fields_set contains the field
        if self.mount_path is None and "mount_path" in self.model_fields_set:
            _dict["mountPath"] = None

        # set to None if exclude (nullable) is None
        # and model_fields_set contains the field
        if self.exclude is None and "exclude" in self.model_fields_set:
            _dict["exclude"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigMapInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "configMap": obj.get("configMap"),
                "mountPath": obj.get("mountPath"),
                "exclude": (
                    obj.get("exclude") if obj.get("exclude") is not None else False
                ),
            }
        )
        return _obj
