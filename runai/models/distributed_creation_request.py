# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.distributed_spec_master_spec import DistributedSpecMasterSpec
from runai.models.distributed_spec_spec import DistributedSpecSpec
from typing import Optional, Set
from typing_extensions import Self


class DistributedCreationRequest(BaseModel):
    """
    Pydantic class model representing DistributedCreationRequest.

    Parameters:
        ```python
        name: str
        use_given_name_as_prefix: bool
        project_id: str
        cluster_id: str
        spec: DistributedSpecSpec
        master_spec_same_as_worker: Optional[bool]
        master_spec: Optional[DistributedSpecMasterSpec]
        ```
        name: The name of the workload.
        use_given_name_as_prefix: When true, the requested name will be treated as a prefix. The final name of the workload will be composed of the name followed by a random set of characters. - Default: False
        project_id: The id of the project.
        cluster_id: The id of the cluster.
        spec: See model DistributedSpecSpec for more information.
        master_spec_same_as_worker: used for distributed workloads to indicate that the master spec should be the same as the worker spec. in this case, masterSpec should not be specified.
        master_spec: See model DistributedSpecMasterSpec for more information.
    Example:
        ```python
        DistributedCreationRequest(
            name='my-workload-name',
                        use_given_name_as_prefix=True,
                        project_id='1',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        spec="example",
                        master_spec_same_as_worker=True,
                        master_spec=runai.models.distributed_spec_master_spec.DistributedSpec_masterSpec()
        )
        ```
    """  # noqa: E501

    name: Annotated[str, Field(min_length=1, strict=True)] = Field(
        description="The name of the workload."
    )
    use_given_name_as_prefix: Optional[StrictBool] = Field(
        default=False,
        description="When true, the requested name will be treated as a prefix. The final name of the workload will be composed of the name followed by a random set of characters.",
        alias="useGivenNameAsPrefix",
    )
    project_id: StrictStr = Field(
        description="The id of the project.", alias="projectId"
    )
    cluster_id: StrictStr = Field(
        description="The id of the cluster.", alias="clusterId"
    )
    spec: Optional[DistributedSpecSpec] = None
    master_spec_same_as_worker: Optional[StrictBool] = Field(
        default=None,
        description="used for distributed workloads to indicate that the master spec should be the same as the worker spec. in this case, masterSpec should not be specified.",
        alias="masterSpecSameAsWorker",
    )
    master_spec: Optional[DistributedSpecMasterSpec] = Field(
        default=None, alias="masterSpec"
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "useGivenNameAsPrefix",
        "projectId",
        "clusterId",
        "spec",
        "masterSpecSameAsWorker",
        "masterSpec",
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
        """Create an instance of DistributedCreationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict["spec"] = self.spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of master_spec
        if self.master_spec:
            _dict["masterSpec"] = self.master_spec.to_dict()
        # set to None if master_spec_same_as_worker (nullable) is None
        # and model_fields_set contains the field
        if (
            self.master_spec_same_as_worker is None
            and "master_spec_same_as_worker" in self.model_fields_set
        ):
            _dict["masterSpecSameAsWorker"] = None

        # set to None if master_spec (nullable) is None
        # and model_fields_set contains the field
        if self.master_spec is None and "master_spec" in self.model_fields_set:
            _dict["masterSpec"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistributedCreationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "useGivenNameAsPrefix": (
                    obj.get("useGivenNameAsPrefix")
                    if obj.get("useGivenNameAsPrefix") is not None
                    else False
                ),
                "projectId": obj.get("projectId"),
                "clusterId": obj.get("clusterId"),
                "spec": (
                    DistributedSpecSpec.from_dict(obj["spec"])
                    if obj.get("spec") is not None
                    else None
                ),
                "masterSpecSameAsWorker": obj.get("masterSpecSameAsWorker"),
                "masterSpec": (
                    DistributedSpecMasterSpec.from_dict(obj["masterSpec"])
                    if obj.get("masterSpec") is not None
                    else None
                ),
            }
        )
        return _obj
