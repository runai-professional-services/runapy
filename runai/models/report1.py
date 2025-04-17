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
from runai.models.label1 import Label1
from runai.models.metric_information_for_report import MetricInformationForReport
from runai.models.range import Range
from runai.models.report_status import ReportStatus
from typing import Optional, Set
from typing_extensions import Self


class Report1(BaseModel):
    """
    Pydantic class model representing Report1.

    Parameters:
        ```python
        name: str
        description: str
        metrics: List[MetricInformationForReport]
        labels: List[Label1]
        range: Optional[Range]
        additional_fields: Dict[str, object]
        id: str
        created_at: datetime
        created_by: str
        tenant_id: int
        status: ReportStatus
        status_updated_at: datetime
        status_message: str
        ```
        name: See model str for more information.
        description: See model str for more information.
        metrics: See model List[MetricInformationForReport] for more information.
        labels: See model List[Label1] for more information.
        range: See model Range for more information.
        additional_fields: See model Dict[str, object] for more information.
        id: See model str for more information.
        created_at: See model datetime for more information.
        created_by: See model str for more information.
        tenant_id: ID of the tenant where the project is located.
        status: See model ReportStatus for more information.
        status_updated_at: See model datetime for more information.
        status_message: See model str for more information.
    Example:
        ```python
        Report1(
            name='2023 GPU report',
                        description='This report shows the GPU usage of all projects in the organization',
                        metrics=[
                    runai.models.metric_information_for_report.MetricInformationForReport(
                        name = 'gpu_allocation_hours',
                        display_name = 'GPU allocation hours',
                        filters = {
                            'key' : [
                                ''
                                ]
                            }, )
                    ],
                        labels=[
                    runai.models.label1.Label1(
                        name = 'nodepoolName',
                        display_name = 'Node pool', )
                    ],
                        range=runai.models.range.Range(
                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                    end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                        additional_fields={ },
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

    name: StrictStr
    description: Optional[StrictStr] = None
    metrics: List[MetricInformationForReport]
    labels: Optional[List[Label1]] = None
    range: Optional[Range]
    additional_fields: Optional[Dict[str, Any]] = Field(
        default=None, alias="additionalFields"
    )
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
        "name",
        "description",
        "metrics",
        "labels",
        "range",
        "additionalFields",
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
        """Create an instance of Report1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict["metrics"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict["labels"] = _items
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict["range"] = self.range.to_dict()
        # set to None if range (nullable) is None
        # and model_fields_set contains the field
        if self.range is None and "range" in self.model_fields_set:
            _dict["range"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Report1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "metrics": (
                    [
                        MetricInformationForReport.from_dict(_item)
                        for _item in obj["metrics"]
                    ]
                    if obj.get("metrics") is not None
                    else None
                ),
                "labels": (
                    [Label1.from_dict(_item) for _item in obj["labels"]]
                    if obj.get("labels") is not None
                    else None
                ),
                "range": (
                    Range.from_dict(obj["range"])
                    if obj.get("range") is not None
                    else None
                ),
                "additionalFields": obj.get("additionalFields"),
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
