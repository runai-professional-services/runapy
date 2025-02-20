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
from runai.models.config_map_instance import ConfigMapInstance
from runai.models.data_volume_instance import DataVolumeInstance
from runai.models.git_instance import GitInstance
from runai.models.host_path_instance import HostPathInstance
from runai.models.nfs_instance import NfsInstance
from runai.models.pvc_instance import PvcInstance
from runai.models.s3_instance import S3Instance
from runai.models.secret_instance1 import SecretInstance1
from typing import Optional, Set
from typing_extensions import Self


class StorageFields(BaseModel):
    """
    Pydantic class model representing StorageFields.

    Parameters:
        ```python
        data_volume: Optional[List[DataVolumeInstance]]
        pvc: Optional[List[PvcInstance]]
        git: Optional[List[GitInstance]]
        config_map_volume: Optional[List[ConfigMapInstance]]
        secret_volume: Optional[List[SecretInstance1]]
        host_path: Optional[List[HostPathInstance]]
        nfs: Optional[List[NfsInstance]]
        s3: Optional[List[S3Instance]]
        ```
        data_volume: Set of data volumes to use in the workload.
        pvc: Set of pvc persistent volume claims to use in the workload.
        git: Set of git repositories to use in the workload.
        config_map_volume: Set of config map volumes to use in the workload
        secret_volume: Set of secret volumes to use in the workload
        host_path: Set of host paths to use in the workload.
        nfs: Set of nfs volumes to use in the workload.
        s3: Set of s3 buckets to use in the workload.
    Example:
        ```python
        StorageFields(
            data_volume=[
                    runai.models.data_volume_instance.DataVolumeInstance()
                    ],
                        pvc=[
                    runai.models.pvc_instance.PvcInstance()
                    ],
                        git=[
                    runai.models.git_instance.GitInstance()
                    ],
                        config_map_volume=[
                    runai.models.config_map_instance.ConfigMapInstance()
                    ],
                        secret_volume=[
                    runai.models.secret_instance1.SecretInstance1()
                    ],
                        host_path=[
                    runai.models.host_path_instance.HostPathInstance()
                    ],
                        nfs=[
                    runai.models.nfs_instance.NfsInstance()
                    ],
                        s3=[
                    runai.models.s3_instance.S3Instance()
                    ]
        )
        ```
    """  # noqa: E501

    data_volume: Optional[List[Optional[DataVolumeInstance]]] = Field(
        default=None,
        description="Set of data volumes to use in the workload.",
        alias="dataVolume",
    )
    pvc: Optional[List[Optional[PvcInstance]]] = Field(
        default=None,
        description="Set of pvc persistent volume claims to use in the workload.",
    )
    git: Optional[List[Optional[GitInstance]]] = Field(
        default=None, description="Set of git repositories to use in the workload."
    )
    config_map_volume: Optional[List[Optional[ConfigMapInstance]]] = Field(
        default=None,
        description="Set of config map volumes to use in the workload",
        alias="configMapVolume",
    )
    secret_volume: Optional[List[Optional[SecretInstance1]]] = Field(
        default=None,
        description="Set of secret volumes to use in the workload",
        alias="secretVolume",
    )
    host_path: Optional[List[Optional[HostPathInstance]]] = Field(
        default=None,
        description="Set of host paths to use in the workload.",
        alias="hostPath",
    )
    nfs: Optional[List[Optional[NfsInstance]]] = Field(
        default=None, description="Set of nfs volumes to use in the workload."
    )
    s3: Optional[List[Optional[S3Instance]]] = Field(
        default=None, description="Set of s3 buckets to use in the workload."
    )
    __properties: ClassVar[List[str]] = [
        "dataVolume",
        "pvc",
        "git",
        "configMapVolume",
        "secretVolume",
        "hostPath",
        "nfs",
        "s3",
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
        """Create an instance of StorageFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_volume (list)
        _items = []
        if self.data_volume:
            for _item_data_volume in self.data_volume:
                if _item_data_volume:
                    _items.append(_item_data_volume.to_dict())
            _dict["dataVolume"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pvc (list)
        _items = []
        if self.pvc:
            for _item_pvc in self.pvc:
                if _item_pvc:
                    _items.append(_item_pvc.to_dict())
            _dict["pvc"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in git (list)
        _items = []
        if self.git:
            for _item_git in self.git:
                if _item_git:
                    _items.append(_item_git.to_dict())
            _dict["git"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in config_map_volume (list)
        _items = []
        if self.config_map_volume:
            for _item_config_map_volume in self.config_map_volume:
                if _item_config_map_volume:
                    _items.append(_item_config_map_volume.to_dict())
            _dict["configMapVolume"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in secret_volume (list)
        _items = []
        if self.secret_volume:
            for _item_secret_volume in self.secret_volume:
                if _item_secret_volume:
                    _items.append(_item_secret_volume.to_dict())
            _dict["secretVolume"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in host_path (list)
        _items = []
        if self.host_path:
            for _item_host_path in self.host_path:
                if _item_host_path:
                    _items.append(_item_host_path.to_dict())
            _dict["hostPath"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nfs (list)
        _items = []
        if self.nfs:
            for _item_nfs in self.nfs:
                if _item_nfs:
                    _items.append(_item_nfs.to_dict())
            _dict["nfs"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in s3 (list)
        _items = []
        if self.s3:
            for _item_s3 in self.s3:
                if _item_s3:
                    _items.append(_item_s3.to_dict())
            _dict["s3"] = _items
        # set to None if data_volume (nullable) is None
        # and model_fields_set contains the field
        if self.data_volume is None and "data_volume" in self.model_fields_set:
            _dict["dataVolume"] = None

        # set to None if pvc (nullable) is None
        # and model_fields_set contains the field
        if self.pvc is None and "pvc" in self.model_fields_set:
            _dict["pvc"] = None

        # set to None if git (nullable) is None
        # and model_fields_set contains the field
        if self.git is None and "git" in self.model_fields_set:
            _dict["git"] = None

        # set to None if config_map_volume (nullable) is None
        # and model_fields_set contains the field
        if (
            self.config_map_volume is None
            and "config_map_volume" in self.model_fields_set
        ):
            _dict["configMapVolume"] = None

        # set to None if secret_volume (nullable) is None
        # and model_fields_set contains the field
        if self.secret_volume is None and "secret_volume" in self.model_fields_set:
            _dict["secretVolume"] = None

        # set to None if host_path (nullable) is None
        # and model_fields_set contains the field
        if self.host_path is None and "host_path" in self.model_fields_set:
            _dict["hostPath"] = None

        # set to None if nfs (nullable) is None
        # and model_fields_set contains the field
        if self.nfs is None and "nfs" in self.model_fields_set:
            _dict["nfs"] = None

        # set to None if s3 (nullable) is None
        # and model_fields_set contains the field
        if self.s3 is None and "s3" in self.model_fields_set:
            _dict["s3"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "dataVolume": (
                    [DataVolumeInstance.from_dict(_item) for _item in obj["dataVolume"]]
                    if obj.get("dataVolume") is not None
                    else None
                ),
                "pvc": (
                    [PvcInstance.from_dict(_item) for _item in obj["pvc"]]
                    if obj.get("pvc") is not None
                    else None
                ),
                "git": (
                    [GitInstance.from_dict(_item) for _item in obj["git"]]
                    if obj.get("git") is not None
                    else None
                ),
                "configMapVolume": (
                    [
                        ConfigMapInstance.from_dict(_item)
                        for _item in obj["configMapVolume"]
                    ]
                    if obj.get("configMapVolume") is not None
                    else None
                ),
                "secretVolume": (
                    [SecretInstance1.from_dict(_item) for _item in obj["secretVolume"]]
                    if obj.get("secretVolume") is not None
                    else None
                ),
                "hostPath": (
                    [HostPathInstance.from_dict(_item) for _item in obj["hostPath"]]
                    if obj.get("hostPath") is not None
                    else None
                ),
                "nfs": (
                    [NfsInstance.from_dict(_item) for _item in obj["nfs"]]
                    if obj.get("nfs") is not None
                    else None
                ),
                "s3": (
                    [S3Instance.from_dict(_item) for _item in obj["s3"]]
                    if obj.get("s3") is not None
                    else None
                ),
            }
        )
        return _obj
