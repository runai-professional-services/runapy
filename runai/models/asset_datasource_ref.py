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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.asset_kind import AssetKind
from runai.models.data_source_overrides import DataSourceOverrides
from typing import Optional, Set
from typing_extensions import Self


class AssetDatasourceRef(BaseModel):
    """
    Pydantic class model representing Reference information about a datasource asset..

    Parameters:
        ```python
        id: str
        name: str
        kind: AssetKind
        overrides: Optional[DataSourceOverrides]
        ```
        id: Unique identifier of the asset.
        name: The name of the asset.
        kind: See model AssetKind for more information.
        overrides: See model DataSourceOverrides for more information.
    Example:
        ```python
        AssetDatasourceRef(
            id='0',
                        name='my-asset',
                        kind='compute',
                        overrides=runai.models.data_source_overrides.DataSourceOverrides(
                    container_path = '/container/directory', )
        )
        ```
    """  # noqa: E501

    id: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="Unique identifier of the asset."
    )
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The name of the asset."
    )
    kind: AssetKind
    overrides: Optional[DataSourceOverrides] = None
    __properties: ClassVar[List[str]] = ["id", "name", "kind", "overrides"]

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
        """Create an instance of AssetDatasourceRef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of overrides
        if self.overrides:
            _dict["overrides"] = self.overrides.to_dict()
        # set to None if overrides (nullable) is None
        # and model_fields_set contains the field
        if self.overrides is None and "overrides" in self.model_fields_set:
            _dict["overrides"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetDatasourceRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "kind": obj.get("kind"),
                "overrides": (
                    DataSourceOverrides.from_dict(obj["overrides"])
                    if obj.get("overrides") is not None
                    else None
                ),
            }
        )
        return _obj
