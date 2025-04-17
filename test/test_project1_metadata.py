# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.project1_metadata import Project1Metadata


class TestProject1Metadata(unittest.TestCase):
    """Project1Metadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project1Metadata:
        """Test Project1Metadata
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Project1Metadata`

        # model = Project1Metadata()
        if include_optional:
            return Project1Metadata(
                project_id=1,
                project_name="project-a",
                department_id=8,
                department_name="default",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                cluster_name="cluster-a",
            )
        else:
            return Project1Metadata(
                project_id=1,
                project_name="project-a",
                department_id=8,
                department_name="default",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                cluster_name="cluster-a",
            )

    def testProject1Metadata(self):
        """Test Project1Metadata"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
