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
from runai.models.data_department_fields import DataDepartmentFields


class TestDataDepartmentFields(unittest.TestCase):
    """DataDepartmentFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataDepartmentFields:
        """Test DataDepartmentFields
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DataDepartmentFields`

        # model = DataDepartmentFields()
        if include_optional:
            return DataDepartmentFields(
                description="",
                resources=[
                    runai.models.resources.Resources(
                        node_pool=runai.models.resources_node_pool.Resources_nodePool(
                            id="22",
                            name="default",
                        ),
                        gpu=None,
                        cpu=runai.models.resources_cpu.Resources_cpu(),
                        memory=runai.models.resources_memory.Resources_memory(),
                    )
                ],
                scheduling_rules=runai.models.scheduling_rules.SchedulingRules(
                    interactive_job_time_limit_seconds=100,
                    interactive_job_max_idle_duration_seconds=100,
                    interactive_job_preempt_idle_duration_seconds=100,
                    training_job_max_idle_duration_seconds=100,
                    training_job_time_limit_seconds=100,
                ),
                default_node_pools=[""],
                node_types=runai.models.node_types_per_workload.NodeTypesPerWorkload(
                    training=[""],
                    workspace=[""],
                    names={"key' : '"},
                ),
                name="organization1",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                overtime_data=runai.models.overtime_data.OvertimeData(
                    range24h_data=runai.models.range24h_data.range24hData(),
                    range7d_data=runai.models.range7d_data.range7dData(),
                    range30d_data=runai.models.range30d_data.range30dData(),
                ),
            )
        else:
            return DataDepartmentFields(
                resources=[
                    runai.models.resources.Resources(
                        node_pool=runai.models.resources_node_pool.Resources_nodePool(
                            id="22",
                            name="default",
                        ),
                        gpu=None,
                        cpu=runai.models.resources_cpu.Resources_cpu(),
                        memory=runai.models.resources_memory.Resources_memory(),
                    )
                ],
                name="organization1",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
            )

    def testDataDepartmentFields(self):
        """Test DataDepartmentFields"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
