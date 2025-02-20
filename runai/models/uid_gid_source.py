# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UidGidSource(str, Enum):
    """
    Indicate the way to determine the user and group ids of the container. The options are a. `fromTheImage` - user and group ids are determined by the docker image that the container runs. this is the default option. b. `custom` - user and group ids can be specified in the environment asset and/or the workspace creation request. c. `idpToken` - user and group ids are determined according to the identity provider (idp) access token. This option is intended for internal use of the environment UI form. For more information, see [User Identity](https://docs.run.ai/latest/admin/runai-setup/config/non-root-containers/).

    Allowed enum values:

    FROMTHEIMAGE = 'fromTheImage'

    FROMIDPTOKEN = 'fromIdpToken'

    CUSTOM = 'custom'


    Example:
        ```python
        UidGidSource.FROMTHEIMAGE
        UidGidSource.FROMIDPTOKEN
        UidGidSource.CUSTOM
        ```
    """

    FROMTHEIMAGE = "fromTheImage"
    FROMIDPTOKEN = "fromIdpToken"
    CUSTOM = "custom"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UidGidSource from a JSON string"""
        return cls(json.loads(json_str))
