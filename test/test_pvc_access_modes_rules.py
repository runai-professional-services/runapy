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
from runai.models.pvc_access_modes_rules import PvcAccessModesRules


class TestPvcAccessModesRules(unittest.TestCase):
    """PvcAccessModesRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PvcAccessModesRules:
        """Test PvcAccessModesRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PvcAccessModesRules`

        # model = PvcAccessModesRules()
        if include_optional:
            return PvcAccessModesRules(
                read_write_once=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                read_only_many=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                read_write_many=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
            )
        else:
            return PvcAccessModesRules()

    def testPvcAccessModesRules(self):
        """Test PvcAccessModesRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
