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
from runai.models.probe_rules import ProbeRules


class TestProbeRules(unittest.TestCase):
    """ProbeRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProbeRules:
        """Test ProbeRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProbeRules`

        # model = ProbeRules()
        if include_optional:
            return ProbeRules(
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
                timeout_seconds=runai.models.integer_rules.IntegerRules(
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
                success_threshold=runai.models.integer_rules.IntegerRules(
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
                failure_threshold=runai.models.integer_rules.IntegerRules(
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
                handler=runai.models.probe_handler_rules.ProbeHandlerRules(
                    http_get=runai.models.probe_handler_rules_http_get.ProbeHandlerRules_httpGet(
                        path=runai.models.string_rules.StringRules(),
                        port=runai.models.integer_rules.IntegerRules(
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
                        host=runai.models.string_rules.StringRules(),
                        scheme=runai.models.string_rules.StringRules(),
                    ),
                ),
            )
        else:
            return ProbeRules()

    def testProbeRules(self):
        """Test ProbeRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
