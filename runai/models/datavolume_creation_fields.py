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

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class DatavolumeCreationFields(BaseModel):
    """
    Pydantic class model representing DatavolumeCreationFields.

    Parameters:
        ```python
        name: str
        description: str
        origin_pvc_name: str
        project_id: str
        should_delete_original_volume: bool
        ```
        name: See model str for more information.
        description: See model str for more information.
        origin_pvc_name: The name of the PVC that the datavolume is based on
        project_id: The ID of the project that in its namespace the origin pvc is located
        should_delete_original_volume: If true, the original storage volume will be deleted together with the datavolume - Default: False
    Example:
        ```python
        DatavolumeCreationFields(
            name='datavolume-a',
                        description='Results of experiment X',
                        origin_pvc_name='pvc-a',
                        project_id='5',
                        should_delete_original_volume=False
        )
        ```
    """  # noqa: E501

    name: Annotated[str, Field(strict=True, max_length=63)]
    description: Optional[Annotated[str, Field(strict=True, max_length=127)]] = None
    origin_pvc_name: StrictStr = Field(
        description="The name of the PVC that the datavolume is based on",
        alias="originPvcName",
    )
    project_id: StrictStr = Field(
        description="The ID of the project that in its namespace the origin pvc is located",
        alias="projectId",
    )
    should_delete_original_volume: Optional[StrictBool] = Field(
        default=False,
        description="If true, the original storage volume will be deleted together with the datavolume",
        alias="shouldDeleteOriginalVolume",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "description",
        "originPvcName",
        "projectId",
        "shouldDeleteOriginalVolume",
    ]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z][-a-z0-9]{0,62}$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-z][-a-z0-9]{0,62}$/"
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
        """Create an instance of DatavolumeCreationFields from a JSON string"""
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
        """Create an instance of DatavolumeCreationFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "originPvcName": obj.get("originPvcName"),
                "projectId": obj.get("projectId"),
                "shouldDeleteOriginalVolume": (
                    obj.get("shouldDeleteOriginalVolume")
                    if obj.get("shouldDeleteOriginalVolume") is not None
                    else False
                ),
            }
        )
        return _obj
