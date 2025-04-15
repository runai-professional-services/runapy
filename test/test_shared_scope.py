# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.shared_scope import SharedScope


class TestSharedScope(unittest.TestCase):
    """SharedScope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SharedScope:
        """Test SharedScope
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SharedScope`

        # model = SharedScope()
        if include_optional:
            return SharedScope(
                scope_type="cluster",
                scope_id="a418ed33-9399-48c0-a890-122cadd13bfd",
                scope_name="project-a",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                created_by="user@run.ai",
            )
        else:
            return SharedScope(
                scope_type="cluster",
                scope_id="a418ed33-9399-48c0-a890-122cadd13bfd",
                scope_name="project-a",
            )

    def testSharedScope(self):
        """Test SharedScope"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
