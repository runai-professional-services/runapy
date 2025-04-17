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
from runai.models.specific_run_auto_scaling_auto_scaling import (
    SpecificRunAutoScalingAutoScaling,
)


class TestSpecificRunAutoScalingAutoScaling(unittest.TestCase):
    """SpecificRunAutoScalingAutoScaling unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpecificRunAutoScalingAutoScaling:
        """Test SpecificRunAutoScalingAutoScaling
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SpecificRunAutoScalingAutoScaling`

        # model = SpecificRunAutoScalingAutoScaling()
        if include_optional:
            return SpecificRunAutoScalingAutoScaling(
                metric_threshold_percentage=1,
                min_replicas=0,
                max_replicas=1,
                initial_replicas=0,
                activation_replicas=1,
                concurrency_hard_limit=0,
                scale_to_zero_retention_seconds=0,
                scale_down_delay_seconds=0,
                initialization_timeout_seconds=1,
                threshold_metric="http_requests_total",
                threshold_value=56,
            )
        else:
            return SpecificRunAutoScalingAutoScaling()

    def testSpecificRunAutoScalingAutoScaling(self):
        """Test SpecificRunAutoScalingAutoScaling"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
