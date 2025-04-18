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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class DepartmentProjectParent(BaseModel):
    """
    Pydantic class model representing Department or project parent.

    Parameters:
        ```python
        id: str
        name: str
        parent: Optional[DepartmentProjectParent]
        ```
        id: See model str for more information.
        name: See model str for more information.
        parent: See model DepartmentProjectParent for more information.
    Example:
        ```python
        DepartmentProjectParent(
            id='9f55253e-11ed-47c7-acef-fc4054768dbc',
                        name='organization1',
                        parent=runai.models.department_project_parent.DepartmentProjectParent(
                    id = '9f55253e-11ed-47c7-acef-fc4054768dbc',
                    name = 'organization1',
                    parent = runai.models.department_project_parent.DepartmentProjectParent(
                        id = '9f55253e-11ed-47c7-acef-fc4054768dbc',
                        name = 'organization1', ), )
        )
        ```
    """  # noqa: E501

    id: StrictStr
    name: StrictStr
    parent: Optional[DepartmentProjectParent] = None
    __properties: ClassVar[List[str]] = ["id", "name", "parent"]

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
        """Create an instance of DepartmentProjectParent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict["parent"] = self.parent.to_dict()
        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict["parent"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DepartmentProjectParent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "parent": (
                    DepartmentProjectParent.from_dict(obj["parent"])
                    if obj.get("parent") is not None
                    else None
                ),
            }
        )
        return _obj


# TODO: Rewrite to not use raise_errors
DepartmentProjectParent.model_rebuild(raise_errors=False)
