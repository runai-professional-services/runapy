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


class S3Instance(BaseModel):
    """
    Pydantic class model representing S3Instance.

    Parameters:
        ```python
        name: Optional[str]
        bucket: Optional[str]
        path: Optional[str]
        url: Optional[str]
        access_key_secret: Optional[str]
        secret_key_of_access_key_id: Optional[str]
        secret_key_of_secret_key: Optional[str]
        exclude: Optional[bool]
        ```
        name: unique name to identify the instance. primarily used for policy locked rules.
        bucket: The name of the bucket. (mandatory)
        path: Local path within the workspace to which the S3 bucket will be mapped. (mandatory)
        url: The url of the S3 service provider. The default is the URL of the Amazon AWS S3 service.
        access_key_secret: Name of the secret containing credentials of the S3 bucket. Used for private S3 buckets.
        secret_key_of_access_key_id: The key to use for loading the access key id from the secret. The default is &#x60;AccessKeyId&#x60;. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).
        secret_key_of_secret_key: The key to use for loading the secret key from the secret. The default is &#x60;SecretKey&#x60;. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).
        exclude: Use &#39;true&#39; in case the item is defined in defaults of the policy, and you wish to exclude it from the workload. - Default: False
    Example:
        ```python
        S3Instance(
            name='storage-instance-a',
                        bucket='my-bucket',
                        path='/container/my-bucket',
                        url='https://s3.amazonaws.com',
                        access_key_secret='my-access-key-secret',
                        secret_key_of_access_key_id='AccessKeyId',
                        secret_key_of_secret_key='SecretKey',
                        exclude=False
        )
        ```
    """  # noqa: E501

    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="unique name to identify the instance. primarily used for policy locked rules.",
    )
    bucket: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None, description="The name of the bucket. (mandatory)"
    )
    path: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="Local path within the workspace to which the S3 bucket will be mapped. (mandatory)",
    )
    url: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(
        default=None,
        description="The url of the S3 service provider. The default is the URL of the Amazon AWS S3 service.",
    )
    access_key_secret: Optional[Annotated[str, Field(min_length=1, strict=True)]] = (
        Field(
            default=None,
            description="Name of the secret containing credentials of the S3 bucket. Used for private S3 buckets.",
            alias="accessKeySecret",
        )
    )
    secret_key_of_access_key_id: Optional[
        Annotated[str, Field(min_length=1, strict=True)]
    ] = Field(
        default=None,
        description="The key to use for loading the access key id from the secret. The default is `AccessKeyId`. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).",
        alias="secretKeyOfAccessKeyId",
    )
    secret_key_of_secret_key: Optional[
        Annotated[str, Field(min_length=1, strict=True)]
    ] = Field(
        default=None,
        description="The key to use for loading the secret key from the secret. The default is `SecretKey`. For more information, see [Credentials access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).",
        alias="secretKeyOfSecretKey",
    )
    exclude: Optional[StrictBool] = Field(
        default=False,
        description="Use 'true' in case the item is defined in defaults of the policy, and you wish to exclude it from the workload.",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "bucket",
        "path",
        "url",
        "accessKeySecret",
        "secretKeyOfAccessKeyId",
        "secretKeyOfSecretKey",
        "exclude",
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
        """Create an instance of S3Instance from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict["name"] = None

        # set to None if bucket (nullable) is None
        # and model_fields_set contains the field
        if self.bucket is None and "bucket" in self.model_fields_set:
            _dict["bucket"] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict["url"] = None

        # set to None if access_key_secret (nullable) is None
        # and model_fields_set contains the field
        if (
            self.access_key_secret is None
            and "access_key_secret" in self.model_fields_set
        ):
            _dict["accessKeySecret"] = None

        # set to None if secret_key_of_access_key_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.secret_key_of_access_key_id is None
            and "secret_key_of_access_key_id" in self.model_fields_set
        ):
            _dict["secretKeyOfAccessKeyId"] = None

        # set to None if secret_key_of_secret_key (nullable) is None
        # and model_fields_set contains the field
        if (
            self.secret_key_of_secret_key is None
            and "secret_key_of_secret_key" in self.model_fields_set
        ):
            _dict["secretKeyOfSecretKey"] = None

        # set to None if exclude (nullable) is None
        # and model_fields_set contains the field
        if self.exclude is None and "exclude" in self.model_fields_set:
            _dict["exclude"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of S3Instance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "bucket": obj.get("bucket"),
                "path": obj.get("path"),
                "url": obj.get("url"),
                "accessKeySecret": obj.get("accessKeySecret"),
                "secretKeyOfAccessKeyId": obj.get("secretKeyOfAccessKeyId"),
                "secretKeyOfSecretKey": obj.get("secretKeyOfSecretKey"),
                "exclude": (
                    obj.get("exclude") if obj.get("exclude") is not None else False
                ),
            }
        )
        return _obj
