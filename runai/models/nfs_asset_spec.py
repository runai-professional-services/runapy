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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class NFSAssetSpec(BaseModel):
    """
    Pydantic class model representing NFSAssetSpec.

    Parameters:
        ```python
        path: Optional[str]
        read_only: Optional[bool]
        server: Optional[str]
        mount_path: Optional[str]
        ```
        path: Path that is exported by the NFS server (mandatory). For more information, see [NFS](https://kubernetes.io/docs/concepts/storage/volumes#nfs).
        read_only: Force the NFS export to be mounted with read-only permissions. - Default: True
        server: The hostname or IP address of the NFS server. (mandatory)
        mount_path: The path that the NFS volume will be mounted to when in use. (mandatory)
    Example:
        ```python
        NFSAssetSpec(
            path='/container/nfs',
                        read_only=True,
                        server='my.nfs.com',
                        mount_path='/local/nfs'
        )
        ```
    """  # noqa: E501

    path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Path that is exported by the NFS server (mandatory). For more information, see [NFS](https://kubernetes.io/docs/concepts/storage/volumes#nfs).",
    )
    read_only: Optional[StrictBool] = Field(
        default=True,
        description="Force the NFS export to be mounted with read-only permissions.",
        alias="readOnly",
    )
    server: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="The hostname or IP address of the NFS server. (mandatory)",
    )
    mount_path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="The path that the NFS volume will be mounted to when in use. (mandatory)",
        alias="mountPath",
    )
    __properties: ClassVar[List[str]] = ["path", "readOnly", "server", "mountPath"]

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
        """Create an instance of NFSAssetSpec from a JSON string"""
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
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if read_only (nullable) is None
        # and model_fields_set contains the field
        if self.read_only is None and "read_only" in self.model_fields_set:
            _dict["readOnly"] = None

        # set to None if server (nullable) is None
        # and model_fields_set contains the field
        if self.server is None and "server" in self.model_fields_set:
            _dict["server"] = None

        # set to None if mount_path (nullable) is None
        # and model_fields_set contains the field
        if self.mount_path is None and "mount_path" in self.model_fields_set:
            _dict["mountPath"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NFSAssetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "path": obj.get("path"),
                "readOnly": (
                    obj.get("readOnly") if obj.get("readOnly") is not None else True
                ),
                "server": obj.get("server"),
                "mountPath": obj.get("mountPath"),
            }
        )
        return _obj
