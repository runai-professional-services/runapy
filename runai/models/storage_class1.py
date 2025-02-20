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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.storage_class1_spec import StorageClass1Spec
from typing import Optional, Set
from typing_extensions import Self


class StorageClass1(BaseModel):
    """
    Pydantic class model representing StorageClass1.

    Parameters:
        ```python
        cluster_id: str
        storage_class_name: str
        spec: StorageClass1Spec
        ```
        cluster_id: Cluster ID which has sent the resource info
        storage_class_name: Storage class name
        spec: See model StorageClass1Spec for more information.
    Example:
        ```python
        StorageClass1(
            cluster_id='',
                        storage_class_name='my storage class',
                        spec=runai.models.storage_class1_spec.StorageClass1_Spec(
                    provisioner = 'kubernetes.io/aws-ebs',
                    allow_volume_expansion = True,
                    is_default = False, )
        )
        ```
    """  # noqa: E501

    cluster_id: Optional[StrictStr] = Field(
        default=None, description="Cluster ID which has sent the resource info"
    )
    storage_class_name: StrictStr = Field(description="Storage class name")
    spec: Optional[StorageClass1Spec] = Field(default=None, alias="Spec")
    __properties: ClassVar[List[str]] = ["cluster_id", "storage_class_name", "Spec"]

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
        """Create an instance of StorageClass1 from a JSON string"""
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
            _dict["Spec"] = self.spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageClass1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cluster_id": obj.get("cluster_id"),
                "storage_class_name": obj.get("storage_class_name"),
                "Spec": (
                    StorageClass1Spec.from_dict(obj["Spec"])
                    if obj.get("Spec") is not None
                    else None
                ),
            }
        )
        return _obj
