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
from runai.models.container_non_overridable_rules import ContainerNonOverridableRules


class TestContainerNonOverridableRules(unittest.TestCase):
    """ContainerNonOverridableRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContainerNonOverridableRules:
        """Test ContainerNonOverridableRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContainerNonOverridableRules`

        # model = ContainerNonOverridableRules()
        if include_optional:
            return ContainerNonOverridableRules(
                image=runai.models.string_rules.StringRules(),
                image_pull_policy=runai.models.image_pull_policy_rules.ImagePullPolicyRules(),
                working_dir=runai.models.string_rules.StringRules(),
                create_home_dir=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                probes=runai.models.probes_rules.ProbesRules(
                    readiness=runai.models.probe_rules.ProbeRules(
                        initial_delay_seconds=runai.models.integer_rules.IntegerRules(
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
                        period_seconds=runai.models.integer_rules.IntegerRules(
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                        ),
                        timeout_seconds=None,
                        success_threshold=None,
                        failure_threshold=None,
                        handler=runai.models.probe_handler_rules.ProbeHandlerRules(
                            http_get=runai.models.probe_handler_rules_http_get.ProbeHandlerRules_httpGet(
                                path=runai.models.string_rules.StringRules(),
                                port=None,
                                host=runai.models.string_rules.StringRules(),
                                scheme=runai.models.string_rules.StringRules(),
                            ),
                        ),
                    ),
                ),
            )
        else:
            return ContainerNonOverridableRules()

    def testContainerNonOverridableRules(self):
        """Test ContainerNonOverridableRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
