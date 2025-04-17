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
from runai.models.workspace_policy_v2 import WorkspacePolicyV2


class TestWorkspacePolicyV2(unittest.TestCase):
    """WorkspacePolicyV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspacePolicyV2:
        """Test WorkspacePolicyV2
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WorkspacePolicyV2`

        # model = WorkspacePolicyV2()
        if include_optional:
            return WorkspacePolicyV2(
                meta=None,
                policy=runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                    defaults=runai.models.workspace_policy_defaults_and_rules_v2_defaults.WorkspacePolicyDefaultsAndRulesV2_defaults(),
                    rules=runai.models.rules.rules(),
                    imposed_assets=[""],
                    status=runai.models.policy_validation_status.PolicyValidationStatus(
                        validation=runai.models.policy_validation_status_validation.PolicyValidationStatus_validation(
                            error_message="",
                        ),
                    ),
                ),
                effective=runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                    defaults=runai.models.workspace_policy_defaults_and_rules_v2_defaults.WorkspacePolicyDefaultsAndRulesV2_defaults(),
                    rules=runai.models.rules.rules(),
                    imposed_assets=[""],
                    status=runai.models.policy_validation_status.PolicyValidationStatus(
                        validation=runai.models.policy_validation_status_validation.PolicyValidationStatus_validation(
                            error_message="",
                        ),
                    ),
                ),
                effective_updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
            )
        else:
            return WorkspacePolicyV2()

    def testWorkspacePolicyV2(self):
        """Test WorkspacePolicyV2"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
