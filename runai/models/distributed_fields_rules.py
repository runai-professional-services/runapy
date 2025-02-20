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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.distributed_framework_rules import DistributedFrameworkRules
from runai.models.integer_rules import IntegerRules
from typing import Optional, Set
from typing_extensions import Self


class DistributedFieldsRules(BaseModel):
    """
    Pydantic class model representing DistributedFieldsRules.

    Parameters:
        ```python
        num_workers: Optional[IntegerRules]
        distributed_framework: Optional[DistributedFrameworkRules]
        slots_per_worker: Optional[IntegerRules]
        min_replicas: Optional[IntegerRules]
        max_replicas: Optional[IntegerRules]
        ```
        num_workers: See model IntegerRules for more information.
        distributed_framework: See model DistributedFrameworkRules for more information.
        slots_per_worker: See model IntegerRules for more information.
        min_replicas: See model IntegerRules for more information.
        max_replicas: See model IntegerRules for more information.
    Example:
        ```python
        DistributedFieldsRules(
            num_workers=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        distributed_framework=runai.models.distributed_framework_rules.DistributedFrameworkRules(),
                        slots_per_worker=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        min_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, ),
                        max_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule = {"scope":"project","projectId":3},
                    required = True,
                    can_edit = True,
                    min = 56,
                    max = 56,
                    step = 56, )
        )
        ```
    """  # noqa: E501

    num_workers: Optional[IntegerRules] = Field(default=None, alias="numWorkers")
    distributed_framework: Optional[DistributedFrameworkRules] = Field(
        default=None, alias="distributedFramework"
    )
    slots_per_worker: Optional[IntegerRules] = Field(
        default=None, alias="slotsPerWorker"
    )
    min_replicas: Optional[IntegerRules] = Field(default=None, alias="minReplicas")
    max_replicas: Optional[IntegerRules] = Field(default=None, alias="maxReplicas")
    __properties: ClassVar[List[str]] = [
        "numWorkers",
        "distributedFramework",
        "slotsPerWorker",
        "minReplicas",
        "maxReplicas",
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
        """Create an instance of DistributedFieldsRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of num_workers
        if self.num_workers:
            _dict["numWorkers"] = self.num_workers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of distributed_framework
        if self.distributed_framework:
            _dict["distributedFramework"] = self.distributed_framework.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slots_per_worker
        if self.slots_per_worker:
            _dict["slotsPerWorker"] = self.slots_per_worker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min_replicas
        if self.min_replicas:
            _dict["minReplicas"] = self.min_replicas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_replicas
        if self.max_replicas:
            _dict["maxReplicas"] = self.max_replicas.to_dict()
        # set to None if num_workers (nullable) is None
        # and model_fields_set contains the field
        if self.num_workers is None and "num_workers" in self.model_fields_set:
            _dict["numWorkers"] = None

        # set to None if distributed_framework (nullable) is None
        # and model_fields_set contains the field
        if (
            self.distributed_framework is None
            and "distributed_framework" in self.model_fields_set
        ):
            _dict["distributedFramework"] = None

        # set to None if slots_per_worker (nullable) is None
        # and model_fields_set contains the field
        if (
            self.slots_per_worker is None
            and "slots_per_worker" in self.model_fields_set
        ):
            _dict["slotsPerWorker"] = None

        # set to None if min_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.min_replicas is None and "min_replicas" in self.model_fields_set:
            _dict["minReplicas"] = None

        # set to None if max_replicas (nullable) is None
        # and model_fields_set contains the field
        if self.max_replicas is None and "max_replicas" in self.model_fields_set:
            _dict["maxReplicas"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistributedFieldsRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "numWorkers": (
                    IntegerRules.from_dict(obj["numWorkers"])
                    if obj.get("numWorkers") is not None
                    else None
                ),
                "distributedFramework": (
                    DistributedFrameworkRules.from_dict(obj["distributedFramework"])
                    if obj.get("distributedFramework") is not None
                    else None
                ),
                "slotsPerWorker": (
                    IntegerRules.from_dict(obj["slotsPerWorker"])
                    if obj.get("slotsPerWorker") is not None
                    else None
                ),
                "minReplicas": (
                    IntegerRules.from_dict(obj["minReplicas"])
                    if obj.get("minReplicas") is not None
                    else None
                ),
                "maxReplicas": (
                    IntegerRules.from_dict(obj["maxReplicas"])
                    if obj.get("maxReplicas") is not None
                    else None
                ),
            }
        )
        return _obj
