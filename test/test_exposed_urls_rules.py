# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.exposed_urls_rules import ExposedUrlsRules


class TestExposedUrlsRules(unittest.TestCase):
    """ExposedUrlsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExposedUrlsRules:
        """Test ExposedUrlsRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ExposedUrlsRules`

        # model = ExposedUrlsRules()
        if include_optional:
            return ExposedUrlsRules(
                attributes=runai.models.exposed_url_rules.ExposedUrlRules(
                    container=runai.models.integer_rules.IntegerRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        required=True,
                        can_edit=True,
                        min=56,
                        max=56,
                        step=56,
                        default_from=runai.models.default_from_rule.DefaultFromRule(
                            field="",
                            factor=1.337,
                        ),
                    ),
                    custom_url=runai.models.boolean_rules.BooleanRules(
                        required=True,
                        can_edit=True,
                    ),
                    url=runai.models.string_rules.StringRules(),
                    authorized_users=runai.models.array_rules.ArrayRules(
                        required=True,
                        options=[
                            {
                                "value": "value",
                                "displayed": "A description of the value.",
                            }
                        ],
                        can_edit=True,
                    ),
                    tool_type=runai.models.string_rules.StringRules(),
                    tool_name=runai.models.string_rules.StringRules(),
                ),
                instances=runai.models.item_rules.ItemRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    can_add=True,
                    locked=["HOME", "USER"],
                ),
            )
        else:
            return ExposedUrlsRules()

    def testExposedUrlsRules(self):
        """Test ExposedUrlsRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
