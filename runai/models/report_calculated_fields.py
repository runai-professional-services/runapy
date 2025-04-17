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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.report_status import ReportStatus
from typing import Optional, Set
from typing_extensions import Self


class ReportCalculatedFields(BaseModel):
    """
    Pydantic class model representing ReportCalculatedFields.

    Parameters:
        ```python
        id: str
        created_at: datetime
        created_by: str
        tenant_id: int
        status: ReportStatus
        status_updated_at: datetime
        status_message: str
        ```
        id: See model str for more information.
        created_at: See model datetime for more information.
        created_by: See model str for more information.
        tenant_id: ID of the tenant where the project is located.
        status: See model ReportStatus for more information.
        status_updated_at: See model datetime for more information.
        status_message: See model str for more information.
    Example:
        ```python
        ReportCalculatedFields(
            id='',
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        created_by='user@run.ai',
                        tenant_id=2,
                        status='Pending',
                        status_updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        status_message='Report in queue'
        )
        ```
    """  # noqa: E501

    id: StrictStr
    created_at: datetime = Field(alias="createdAt")
    created_by: StrictStr = Field(alias="createdBy")
    tenant_id: StrictInt = Field(
        description="ID of the tenant where the project is located.", alias="tenantId"
    )
    status: ReportStatus
    status_updated_at: datetime = Field(alias="statusUpdatedAt")
    status_message: Optional[StrictStr] = Field(default=None, alias="statusMessage")
    __properties: ClassVar[List[str]] = [
        "id",
        "createdAt",
        "createdBy",
        "tenantId",
        "status",
        "statusUpdatedAt",
        "statusMessage",
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
        """Create an instance of ReportCalculatedFields from a JSON string"""
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
        """Create an instance of ReportCalculatedFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "createdAt": obj.get("createdAt"),
                "createdBy": obj.get("createdBy"),
                "tenantId": obj.get("tenantId"),
                "status": obj.get("status"),
                "statusUpdatedAt": obj.get("statusUpdatedAt"),
                "statusMessage": obj.get("statusMessage"),
            }
        )
        return _obj
