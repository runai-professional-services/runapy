# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AssetKind(str, Enum):
    """
    The kind of the asset.

    Allowed enum values:

    COMPUTE = 'compute'

    ENVIRONMENT = 'environment'

    ACCESSKEY = 'accessKey'

    DOCKERREGISTRY = 'dockerRegistry'

    PASSWORD = 'password'

    GENERICSECRET = 'genericSecret'

    REGISTRY = 'registry'

    S3 = 's3'

    GIT = 'git'

    NFS = 'nfs'

    PVC = 'pvc'

    HOSTPATH = 'hostPath'

    WORKLOAD_MINUS_TEMPLATE = 'workload-template'

    MODEL = 'model'

    CONFIG_MINUS_MAP = 'config-map'

    SECRET_MINUS_VOLUME = 'secret-volume'

    DATA_MINUS_VOLUME = 'data-volume'


    Example:
        ```python
        AssetKind.COMPUTE
        AssetKind.ENVIRONMENT
        AssetKind.ACCESSKEY
        AssetKind.DOCKERREGISTRY
        AssetKind.PASSWORD
        AssetKind.GENERICSECRET
        AssetKind.REGISTRY
        AssetKind.S3
        AssetKind.GIT
        AssetKind.NFS
        AssetKind.PVC
        AssetKind.HOSTPATH
        AssetKind.WORKLOAD_MINUS_TEMPLATE
        AssetKind.MODEL
        AssetKind.CONFIG_MINUS_MAP
        AssetKind.SECRET_MINUS_VOLUME
        AssetKind.DATA_MINUS_VOLUME
        ```
    """

    COMPUTE = "compute"
    ENVIRONMENT = "environment"
    ACCESSKEY = "accessKey"
    DOCKERREGISTRY = "dockerRegistry"
    PASSWORD = "password"
    GENERICSECRET = "genericSecret"
    REGISTRY = "registry"
    S3 = "s3"
    GIT = "git"
    NFS = "nfs"
    PVC = "pvc"
    HOSTPATH = "hostPath"
    WORKLOAD_MINUS_TEMPLATE = "workload-template"
    MODEL = "model"
    CONFIG_MINUS_MAP = "config-map"
    SECRET_MINUS_VOLUME = "secret-volume"
    DATA_MINUS_VOLUME = "data-volume"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AssetKind from a JSON string"""
        return cls(json.loads(json_str))
