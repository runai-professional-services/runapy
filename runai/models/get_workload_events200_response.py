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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.event1 import Event1
from typing import Optional, Set
from typing_extensions import Self


class GetWorkloadEvents200Response(BaseModel):
    """
    Pydantic class model representing GetWorkloadEvents200Response.

    Parameters:
        ```python
        next: int
        events: List[Event1]
        ```
        next: See model int for more information.
        events: See model List[Event1] for more information.
    Example:
        ```python
        GetWorkloadEvents200Response(
            next=1,
                        events=[
                    runai.models.event1.Event1(
                        created_at = '2022-01-01T03:49:52.531Z',
                        id = '',
                        type = 'Normal',
                        cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
                        message = 'Started container z',
                        reason = 'Started',
                        source = 'kubelet',
                        involved_object = runai.models.involved_object.InvolvedObject(
                            uid = '',
                            kind = 'Pod',
                            name = 'test-0-1',
                            namespace = 'runai-test', ), )
                    ]
        )
        ```
    """  # noqa: E501

    next: Optional[StrictInt] = None
    events: List[Optional[Event1]]
    __properties: ClassVar[List[str]] = ["next", "events"]

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
        """Create an instance of GetWorkloadEvents200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict["events"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetWorkloadEvents200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "next": obj.get("next"),
                "events": (
                    [Event1.from_dict(_item) for _item in obj["events"]]
                    if obj.get("events") is not None
                    else None
                ),
            }
        )
        return _obj
