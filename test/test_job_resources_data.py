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
from runai.models.job_resources_data import JobResourcesData


class TestJobResourcesData(unittest.TestCase):
    """JobResourcesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResourcesData:
        """Test JobResourcesData
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JobResourcesData`

        # model = JobResourcesData()
        if include_optional:
            return JobResourcesData(
                gpu=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                gpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                cpu=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                cpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                advanced=runai.models.job_advanced_data.JobAdvancedData(
                    idle_seconds=50,
                    gr_engine_active=1.337,
                    dram_active=1.337,
                    sm_active=1.337,
                    sm_occupancy=1.337,
                    pipe_tensor_active=1.337,
                    pipe_fp64_active=1.337,
                    pipe_fp32_active=1.337,
                    pipe_fp16_active=1.337,
                    nvlink_tx_bytes=1.337,
                    nvlink_rx_bytes=1.337,
                    pcie_tx_bytes=1.337,
                    pcie_rx_bytes=1.337,
                ),
            )
        else:
            return JobResourcesData(
                gpu=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                gpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                cpu=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
                cpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated=2.5,
                    utilization=0.8,
                ),
            )

    def testJobResourcesData(self):
        """Test JobResourcesData"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
