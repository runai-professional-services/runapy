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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self


class GitAssetSpec(BaseModel):
    """
    Pydantic class model representing GitAssetSpec.

    Parameters:
        ```python
        repository: Optional[str]
        branch: Optional[str]
        revision: Optional[str]
        path: Optional[str]
        password_asset_id: Optional[str]
        ```
        repository: URL to a remote Git repository. The content of this repository will be mapped to the container running the workload. (mandatory)
        branch: Specific branch to synchronize the repository from.
        revision: Specific revision to synchronize the repository from.
        path: Local path within the workspace to which the Git repository will be mapped (mandatory).
        password_asset_id: ID of credentials asset of type password. Needed for non public repository which requires authentication.
    Example:
        ```python
        GitAssetSpec(
            repository='https://github.com/my-git/my-repo',
                        branch='main',
                        revision='0',
                        path='/container/my-repository',
                        password_asset_id='0'
        )
        ```
    """  # noqa: E501

    repository: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="URL to a remote Git repository. The content of this repository will be mapped to the container running the workload. (mandatory)",
    )
    branch: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="Specific branch to synchronize the repository from."
    )
    revision: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Specific revision to synchronize the repository from.",
    )
    path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Local path within the workspace to which the Git repository will be mapped (mandatory).",
    )
    password_asset_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = (
        Field(
            default=None,
            description="ID of credentials asset of type password. Needed for non public repository which requires authentication.",
            alias="passwordAssetId",
        )
    )
    __properties: ClassVar[List[str]] = [
        "repository",
        "branch",
        "revision",
        "path",
        "passwordAssetId",
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
        """Create an instance of GitAssetSpec from a JSON string"""
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
        # set to None if repository (nullable) is None
        # and model_fields_set contains the field
        if self.repository is None and "repository" in self.model_fields_set:
            _dict["repository"] = None

        # set to None if branch (nullable) is None
        # and model_fields_set contains the field
        if self.branch is None and "branch" in self.model_fields_set:
            _dict["branch"] = None

        # set to None if revision (nullable) is None
        # and model_fields_set contains the field
        if self.revision is None and "revision" in self.model_fields_set:
            _dict["revision"] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if password_asset_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.password_asset_id is None
            and "password_asset_id" in self.model_fields_set
        ):
            _dict["passwordAssetId"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GitAssetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "repository": obj.get("repository"),
                "branch": obj.get("branch"),
                "revision": obj.get("revision"),
                "path": obj.get("path"),
                "passwordAssetId": obj.get("passwordAssetId"),
            }
        )
        return _obj
