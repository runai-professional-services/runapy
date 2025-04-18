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
from runai.models.compute_itemized_fields_rules import ComputeItemizedFieldsRules


class TestComputeItemizedFieldsRules(unittest.TestCase):
    """ComputeItemizedFieldsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComputeItemizedFieldsRules:
        """Test ComputeItemizedFieldsRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ComputeItemizedFieldsRules`

        # model = ComputeItemizedFieldsRules()
        if include_optional:
            return ComputeItemizedFieldsRules(
                extended_resources=runai.models.extended_resources_rules.ExtendedResourcesRules(
                    attributes=runai.models.extended_resource_rules.ExtendedResourceRules(
                        quantity=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                )
            )
        else:
            return ComputeItemizedFieldsRules()

    def testComputeItemizedFieldsRules(self):
        """Test ComputeItemizedFieldsRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
