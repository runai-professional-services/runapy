# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ReportGroupByOptions(str, Enum):
    """
    ReportGroupByOptions

    Allowed enum values:

    NODEPOOL = 'Nodepool'

    PROJECT = 'Project'

    DEPARTMENT = 'Department'

    CLUSTER = 'Cluster'


    Example:
        ```python
        ReportGroupByOptions.NODEPOOL
        ReportGroupByOptions.PROJECT
        ReportGroupByOptions.DEPARTMENT
        ReportGroupByOptions.CLUSTER
        ```
    """

    NODEPOOL = "Nodepool"
    PROJECT = "Project"
    DEPARTMENT = "Department"
    CLUSTER = "Cluster"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReportGroupByOptions from a JSON string"""
        return cls(json.loads(json_str))
