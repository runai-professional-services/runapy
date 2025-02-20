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
from runai.models.tolerations_field_rules import TolerationsFieldRules


class TestTolerationsFieldRules(unittest.TestCase):
    """TolerationsFieldRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TolerationsFieldRules:
        """Test TolerationsFieldRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TolerationsFieldRules`

        # model = TolerationsFieldRules()
        if include_optional:
            return TolerationsFieldRules(
                tolerations=runai.models.tolerations_rules.TolerationsRules(
                    attributes=runai.models.toleration_rules.TolerationRules(
                        operator=runai.models.toleration_operator_rules.TolerationOperatorRules(),
                        key=runai.models.string_rules.StringRules(),
                        value=runai.models.string_rules.StringRules(),
                        effect=runai.models.toleration_effect_rules.TolerationEffectRules(),
                        seconds=runai.models.integer_rules.IntegerRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                        ),
                        exclude=runai.models.boolean_rules.BooleanRules(
                            required=True,
                            can_edit=True,
                        ),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                )
            )
        else:
            return TolerationsFieldRules()

    def testTolerationsFieldRules(self):
        """Test TolerationsFieldRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
