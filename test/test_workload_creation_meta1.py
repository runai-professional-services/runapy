# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.workload_creation_meta1 import WorkloadCreationMeta1


class TestWorkloadCreationMeta1(unittest.TestCase):
    """WorkloadCreationMeta1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadCreationMeta1:
        """Test WorkloadCreationMeta1
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WorkloadCreationMeta1`

        # model = WorkloadCreationMeta1()
        if include_optional:
            return WorkloadCreationMeta1(
                name="my-workload-name",
                use_given_name_as_prefix=True,
                project_id="1",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
            )
        else:
            return WorkloadCreationMeta1(
                name="my-workload-name",
                project_id="1",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
            )

    def testWorkloadCreationMeta1(self):
        """Test WorkloadCreationMeta1"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
