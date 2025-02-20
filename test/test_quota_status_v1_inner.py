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
from runai.models.quota_status_v1_inner import QuotaStatusV1Inner


class TestQuotaStatusV1Inner(unittest.TestCase):
    """QuotaStatusV1Inner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaStatusV1Inner:
        """Test QuotaStatusV1Inner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `QuotaStatusV1Inner`

        # model = QuotaStatusV1Inner()
        if include_optional:
            return QuotaStatusV1Inner(
                node_pool_name="",
                allocated=runai.models.quota_status_resource_list_v1.QuotaStatusResourceListV1(
                    gpu=0,
                    cpu=1000,
                    memory=1000,
                ),
                allocated_non_preemptible=runai.models.quota_status_resource_list_v1.QuotaStatusResourceListV1(
                    gpu=0,
                    cpu=1000,
                    memory=1000,
                ),
                requested=runai.models.quota_status_resource_list_v1.QuotaStatusResourceListV1(
                    gpu=0,
                    cpu=1000,
                    memory=1000,
                ),
            )
        else:
            return QuotaStatusV1Inner()

    def testQuotaStatusV1Inner(self):
        """Test QuotaStatusV1Inner"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
