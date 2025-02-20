# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.training_policy_overwrite_request_v2 import (
    TrainingPolicyOverwriteRequestV2,
)


class TestTrainingPolicyOverwriteRequestV2(unittest.TestCase):
    """TrainingPolicyOverwriteRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrainingPolicyOverwriteRequestV2:
        """Test TrainingPolicyOverwriteRequestV2
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TrainingPolicyOverwriteRequestV2`

        # model = TrainingPolicyOverwriteRequestV2()
        if include_optional:
            return TrainingPolicyOverwriteRequestV2(
                meta=runai.models.policy_creation_fields.PolicyCreationFields(
                    scope="system",
                    project_id=1,
                    department_id="2",
                    cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                    name="my-policy",
                ),
                policy=runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                    defaults=runai.models.training_policy_defaults_and_rules_v2_defaults.TrainingPolicyDefaultsAndRulesV2_defaults(),
                    rules=runai.models.rules.rules(),
                    imposed_assets=[""],
                ),
            )
        else:
            return TrainingPolicyOverwriteRequestV2()

    def testTrainingPolicyOverwriteRequestV2(self):
        """Test TrainingPolicyOverwriteRequestV2"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
