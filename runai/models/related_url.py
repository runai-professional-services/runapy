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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class RelatedUrl(BaseModel):
    """
    Pydantic class model representing A URL that is related to the workload. For example, a URL to an external server providing statistics or logging about the workload..

    Parameters:
        ```python
        url: Optional[str]
        type: Optional[str]
        name: Optional[str]
        exclude: Optional[bool]
        ```
        url: The URL for connecting an external service related to the workload. (mandatory)
        type: The type of service that the url provides. For example, wandb (Weights &amp; Biases). (mandatory)
        name: Unique name to identify the instance. primarily used for policy locked rules.
        exclude: Use &#39;true&#39; in case the item is defined in defaults of the policy, and you wish to exclude it from the workload. - Default: False
    Example:
        ```python
        RelatedUrl(
            url='https://my-url.com',
                        type='wandb',
                        name='url-instance-a',
                        exclude=False
        )
        ```
    """  # noqa: E501

    url: Optional[StrictStr] = Field(
        default=None,
        description="The URL for connecting an external service related to the workload. (mandatory)",
    )
    type: Optional[StrictStr] = Field(
        default=None,
        description="The type of service that the url provides. For example, wandb (Weights & Biases). (mandatory)",
    )
    name: Optional[StrictStr] = Field(
        default=None,
        description="Unique name to identify the instance. primarily used for policy locked rules.",
    )
    exclude: Optional[StrictBool] = Field(
        default=False,
        description="Use 'true' in case the item is defined in defaults of the policy, and you wish to exclude it from the workload.",
    )
    __properties: ClassVar[List[str]] = ["url", "type", "name", "exclude"]

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
        """Create an instance of RelatedUrl from a JSON string"""
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
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict["url"] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict["type"] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if exclude (nullable) is None
        # and model_fields_set contains the field
        if self.exclude is None and "exclude" in self.model_fields_set:
            _dict["exclude"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RelatedUrl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "url": obj.get("url"),
                "type": obj.get("type"),
                "name": obj.get("name"),
                "exclude": (
                    obj.get("exclude") if obj.get("exclude") is not None else False
                ),
            }
        )
        return _obj
