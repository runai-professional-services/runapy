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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.common_storage_fields_defaults import CommonStorageFieldsDefaults
from typing import Optional, Set
from typing_extensions import Self


class CommonStorageDefaults(BaseModel):
    """
    Pydantic class model representing CommonStorageDefaults.

    Parameters:
        ```python
        storage: Optional[CommonStorageFieldsDefaults]
        ```
        storage: See model CommonStorageFieldsDefaults for more information.
    Example:
        ```python
        CommonStorageDefaults(
            storage=runai.models.common_storage_fields_defaults.CommonStorageFieldsDefaults(
                    data_volume = runai.models.data_volumes_defaults.DataVolumesDefaults(
                        attributes = runai.models.data_volume_instance.DataVolumeInstance(),
                        instances = [
                            runai.models.data_volume_instance.DataVolumeInstance()
                            ], ),
                    pvc = runai.models.pvcs_defaults.PvcsDefaults(
                        instances = [
                            runai.models.pvc_instance.PvcInstance()
                            ], ),
                    host_path = runai.models.host_paths_defaults.HostPathsDefaults(
                        instances = [
                            runai.models.host_path_instance.HostPathInstance()
                            ], ),
                    nfs = runai.models.nfss_defaults.NfssDefaults(
                        instances = [
                            runai.models.nfs_instance.NfsInstance()
                            ], ),
                    git = runai.models.gits_defaults.GitsDefaults(
                        instances = [
                            runai.models.git_instance.GitInstance()
                            ], ),
                    config_map_volume = runai.models.config_maps_defaults.ConfigMapsDefaults(
                        instances = [
                            runai.models.config_map_instance.ConfigMapInstance()
                            ], ),
                    secret_volume = runai.models.secrets_defaults.SecretsDefaults(
                        instances = [
                            runai.models.secret_instance2.SecretInstance2()
                            ], ), )
        )
        ```
    """  # noqa: E501

    storage: Optional[CommonStorageFieldsDefaults] = None
    __properties: ClassVar[List[str]] = ["storage"]

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
        """Create an instance of CommonStorageDefaults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict["storage"] = self.storage.to_dict()
        # set to None if storage (nullable) is None
        # and model_fields_set contains the field
        if self.storage is None and "storage" in self.model_fields_set:
            _dict["storage"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonStorageDefaults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "storage": (
                    CommonStorageFieldsDefaults.from_dict(obj["storage"])
                    if obj.get("storage") is not None
                    else None
                )
            }
        )
        return _obj
