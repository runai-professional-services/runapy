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
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class Pod(BaseModel):
    """
    Pydantic class model representing Pod.

    Parameters:
        ```python
        pod_id: str
        job_id: str
        pod_group_id: str
        cluster_uuid: str
        pod_name: str
        image_name: str
        node_id: str
        phase: str
        status: str
        created: int
        completed: int
        started: int
        last_updated: int
        dynamic_data: object
        exists_in_cluster: bool
        resource_request: Dict[str, float]
        resource_allocation: Dict[str, float]
        node_pool: str
        namespace: str
        ```
        pod_id: Identifier of the pod running the job.
        job_id: Unique identifier of the job.
        pod_group_id: This had been used as jobId. Remained here for backward compatibility
        cluster_uuid: Unique identifier of the cluster.
        pod_name: The name of the pod running the job.
        image_name: The name of the image executed by the pod.
        node_id: Unique identifier of the node.
        phase: See model str for more information.
        status: See model str for more information.
        created: Creation time of the pod.
        completed: Completion time of the pod.
        started: The time when the pod started executing.
        last_updated: Last time the pod details were updated.
        dynamic_data: See model object for more information.
        exists_in_cluster: See model bool for more information.
        resource_request: See model Dict[str, float] for more information.
        resource_allocation: See model Dict[str, float] for more information.
        node_pool: The node pool of the pod.
        namespace: The namespace of the pod.
    Example:
        ```python
        Pod(
            pod_id='',
                        job_id='',
                        pod_group_id='',
                        cluster_uuid='',
                        pod_name='',
                        image_name='',
                        node_id='',
                        phase='',
                        status='',
                        created=56,
                        completed=56,
                        started=56,
                        last_updated=56,
                        dynamic_data=None,
                        exists_in_cluster=True,
                        resource_request={
                    'key' : 1.337
                    },
                        resource_allocation={
                    'key' : 1.337
                    },
                        node_pool='',
                        namespace=''
        )
        ```
    """  # noqa: E501

    pod_id: StrictStr = Field(
        description="Identifier of the pod running the job.", alias="podId"
    )
    job_id: StrictStr = Field(
        description="Unique identifier of the job.", alias="jobId"
    )
    pod_group_id: Optional[StrictStr] = Field(
        default=None,
        description="This had been used as jobId. Remained here for backward compatibility",
        alias="podGroupId",
    )
    cluster_uuid: StrictStr = Field(
        description="Unique identifier of the cluster.", alias="clusterUuid"
    )
    pod_name: StrictStr = Field(
        description="The name of the pod running the job.", alias="podName"
    )
    image_name: StrictStr = Field(
        description="The name of the image executed by the pod.", alias="imageName"
    )
    node_id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the node.", alias="nodeId"
    )
    phase: StrictStr
    status: Optional[StrictStr] = None
    created: StrictInt = Field(description="Creation time of the pod.")
    completed: StrictInt = Field(description="Completion time of the pod.")
    started: Optional[StrictInt] = Field(
        default=None, description="The time when the pod started executing."
    )
    last_updated: StrictInt = Field(
        description="Last time the pod details were updated.", alias="lastUpdated"
    )
    dynamic_data: Optional[Dict[str, Any]] = Field(default=None, alias="dynamicData")
    exists_in_cluster: Optional[StrictBool] = Field(
        default=None, alias="existsInCluster"
    )
    resource_request: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(
        default=None, alias="resourceRequest"
    )
    resource_allocation: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(
        default=None, alias="resourceAllocation"
    )
    node_pool: Optional[StrictStr] = Field(
        default=None, description="The node pool of the pod.", alias="nodePool"
    )
    namespace: Optional[StrictStr] = Field(
        default=None, description="The namespace of the pod."
    )
    __properties: ClassVar[List[str]] = [
        "podId",
        "jobId",
        "podGroupId",
        "clusterUuid",
        "podName",
        "imageName",
        "nodeId",
        "phase",
        "status",
        "created",
        "completed",
        "started",
        "lastUpdated",
        "dynamicData",
        "existsInCluster",
        "resourceRequest",
        "resourceAllocation",
        "nodePool",
        "namespace",
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
        """Create an instance of Pod from a JSON string"""
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
        """Create an instance of Pod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "podId": obj.get("podId"),
                "jobId": obj.get("jobId"),
                "podGroupId": obj.get("podGroupId"),
                "clusterUuid": obj.get("clusterUuid"),
                "podName": obj.get("podName"),
                "imageName": obj.get("imageName"),
                "nodeId": obj.get("nodeId"),
                "phase": obj.get("phase"),
                "status": obj.get("status"),
                "created": obj.get("created"),
                "completed": obj.get("completed"),
                "started": obj.get("started"),
                "lastUpdated": obj.get("lastUpdated"),
                "dynamicData": obj.get("dynamicData"),
                "existsInCluster": obj.get("existsInCluster"),
                "resourceRequest": obj.get("resourceRequest"),
                "resourceAllocation": obj.get("resourceAllocation"),
                "nodePool": obj.get("nodePool"),
                "namespace": obj.get("namespace"),
            }
        )
        return _obj
