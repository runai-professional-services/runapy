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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.key_value_pair import KeyValuePair
from typing import Optional, Set
from typing_extensions import Self


class GenericSecretSpec(BaseModel):
    """
    Pydantic class model representing GenericSecretSpec.

    Parameters:
        ```python
        existing_secret_name: Optional[str]
        key_value_pairs: Optional[List[KeyValuePair]]
        key_id: int
        ```
        existing_secret_name: name of existing secret in the cluster from which the general key-value values should be taken.
        key_value_pairs: Set of key-value pairs to store in the new credential.
        key_id: id of the encryption key which has been used to encrypt an asset&#39;s data.
    Example:
        ```python
        GenericSecretSpec(
            existing_secret_name='0',
                        key_value_pairs=[
                    runai.models.key_value_pair.KeyValuePair(
                        key = 'secret-key',
                        value = 'my-secret', )
                    ],
                        key_id=56
        )
        ```
    """  # noqa: E501

    existing_secret_name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = (
        Field(
            default=None,
            description="name of existing secret in the cluster from which the general key-value values should be taken.",
            alias="existingSecretName",
        )
    )
    key_value_pairs: Optional[List[Optional[KeyValuePair]]] = Field(
        default=None,
        description="Set of key-value pairs to store in the new credential.",
        alias="keyValuePairs",
    )
    key_id: StrictInt = Field(
        description="id of the encryption key which has been used to encrypt an asset's data.",
        alias="keyId",
    )
    __properties: ClassVar[List[str]] = ["existingSecretName", "keyValuePairs", "keyId"]

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
        """Create an instance of GenericSecretSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in key_value_pairs (list)
        _items = []
        if self.key_value_pairs:
            for _item_key_value_pairs in self.key_value_pairs:
                if _item_key_value_pairs:
                    _items.append(_item_key_value_pairs.to_dict())
            _dict["keyValuePairs"] = _items
        # set to None if existing_secret_name (nullable) is None
        # and model_fields_set contains the field
        if (
            self.existing_secret_name is None
            and "existing_secret_name" in self.model_fields_set
        ):
            _dict["existingSecretName"] = None

        # set to None if key_value_pairs (nullable) is None
        # and model_fields_set contains the field
        if self.key_value_pairs is None and "key_value_pairs" in self.model_fields_set:
            _dict["keyValuePairs"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenericSecretSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "existingSecretName": obj.get("existingSecretName"),
                "keyValuePairs": (
                    [KeyValuePair.from_dict(_item) for _item in obj["keyValuePairs"]]
                    if obj.get("keyValuePairs") is not None
                    else None
                ),
                "keyId": obj.get("keyId"),
            }
        )
        return _obj
