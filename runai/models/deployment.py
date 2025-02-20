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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.deployment_condition import DeploymentCondition
from runai.models.owner import Owner
from runai.models.pod_template import PodTemplate
from typing import Optional, Set
from typing_extensions import Self


class Deployment(BaseModel):
    """
    Pydantic class model representing Deployment.

    Parameters:
        ```python
        cluster_uuid: str
        id: str
        name: str
        namespace: str
        project: str
        owners: List[Owner]
        created_at: datetime
        replicas: int
        template: PodTemplate
        scheduler_name: str
        username: str
        connections: List[str]
        service_id: str
        revision_id: str
        inferenceworkload_name: str
        conditions: List[DeploymentCondition]
        node_pool: str
        ```
        cluster_uuid: See model str for more information.
        id: See model str for more information.
        name: See model str for more information.
        namespace: See model str for more information.
        project: See model str for more information.
        owners: See model List[Owner] for more information.
        created_at: See model datetime for more information.
        replicas: See model int for more information.
        template: See model PodTemplate for more information.
        scheduler_name: See model str for more information.
        username: See model str for more information.
        connections: See model List[str] for more information.
        service_id: See model str for more information.
        revision_id: See model str for more information.
        inferenceworkload_name: See model str for more information.
        conditions: See model List[DeploymentCondition] for more information.
        node_pool: See model str for more information.
    Example:
        ```python
        Deployment(
            cluster_uuid='',
                        id='',
                        name='',
                        namespace='',
                        project='',
                        owners=[
                    {"kind":"kind","name":"name","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
                    ],
                        created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        replicas=56,
                        template=runai.models.pod_template.PodTemplate(
                    containers = [
                        {"image":"image","name":"name"}
                        ],
                    resource_request = {
                        'key' : 1.337
                        }, ),
                        scheduler_name='',
                        username='',
                        connections=[
                    ''
                    ],
                        service_id='',
                        revision_id='',
                        inferenceworkload_name='',
                        conditions=[
                    {"type":"Available","status":true,"reason":"MinimumReplicasAvailable"}
                    ],
                        node_pool=''
        )
        ```
    """  # noqa: E501

    cluster_uuid: StrictStr = Field(alias="clusterUuid")
    id: StrictStr
    name: StrictStr
    namespace: StrictStr
    project: Optional[StrictStr] = None
    owners: List[Owner]
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    replicas: StrictInt
    template: PodTemplate
    scheduler_name: StrictStr = Field(alias="schedulerName")
    username: Optional[StrictStr] = None
    connections: List[StrictStr]
    service_id: Optional[StrictStr] = Field(default=None, alias="serviceId")
    revision_id: Optional[StrictStr] = Field(default=None, alias="revisionId")
    inferenceworkload_name: Optional[StrictStr] = Field(
        default=None, alias="inferenceworkloadName"
    )
    conditions: Optional[List[DeploymentCondition]] = None
    node_pool: Optional[StrictStr] = Field(default=None, alias="nodePool")
    __properties: ClassVar[List[str]] = [
        "clusterUuid",
        "id",
        "name",
        "namespace",
        "project",
        "owners",
        "createdAt",
        "replicas",
        "template",
        "schedulerName",
        "username",
        "connections",
        "serviceId",
        "revisionId",
        "inferenceworkloadName",
        "conditions",
        "nodePool",
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
        """Create an instance of Deployment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in owners (list)
        _items = []
        if self.owners:
            for _item_owners in self.owners:
                if _item_owners:
                    _items.append(_item_owners.to_dict())
            _dict["owners"] = _items
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict["template"] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict["conditions"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Deployment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "clusterUuid": obj.get("clusterUuid"),
                "id": obj.get("id"),
                "name": obj.get("name"),
                "namespace": obj.get("namespace"),
                "project": obj.get("project"),
                "owners": (
                    [Owner.from_dict(_item) for _item in obj["owners"]]
                    if obj.get("owners") is not None
                    else None
                ),
                "createdAt": obj.get("createdAt"),
                "replicas": obj.get("replicas"),
                "template": (
                    PodTemplate.from_dict(obj["template"])
                    if obj.get("template") is not None
                    else None
                ),
                "schedulerName": obj.get("schedulerName"),
                "username": obj.get("username"),
                "connections": obj.get("connections"),
                "serviceId": obj.get("serviceId"),
                "revisionId": obj.get("revisionId"),
                "inferenceworkloadName": obj.get("inferenceworkloadName"),
                "conditions": (
                    [
                        DeploymentCondition.from_dict(_item)
                        for _item in obj["conditions"]
                    ]
                    if obj.get("conditions") is not None
                    else None
                ),
                "nodePool": obj.get("nodePool"),
            }
        )
        return _obj
