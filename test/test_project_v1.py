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
from runai.models.project_v1 import ProjectV1


class TestProjectV1(unittest.TestCase):
    """ProjectV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectV1:
        """Test ProjectV1
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProjectV1`

        # model = ProjectV1()
        if include_optional:
            return ProjectV1(
                node_pools_resources=[
                    runai.models.node_pool_assigned_resources_v1_response.NodePoolAssignedResourcesV1Response(
                        id=1.337,
                        node_pool=runai.models.node_pool_assigned_resources_v1_response_node_pool.NodePoolAssignedResourcesV1Response_nodePool(
                            id=3,
                            name="default",
                        ),
                        gpu=None,
                        cpu=None,
                        memory=None,
                    )
                ],
                deserved_gpus=3,
                max_allowed_gpus=5,
                gpu_over_quota_weight=1,
                default_node_pools=[default],
                interactive_job_time_limit_secs=3600,
                interactive_job_max_idle_duration_secs=3000,
                interactive_preemptible_job_max_idle_duration_secs=3000,
                training_job_time_limit_secs=3600,
                training_job_max_idle_duration_secs=3000,
                node_affinity=runai.models.project_v1_node_affinity_response.ProjectV1NodeAffinityResponse(
                    train=runai.models.project_v1_node_affinity_response_train.ProjectV1NodeAffinityResponse_train(
                        affinity_type="no_limit",
                        selected_types=[
                            runai.models.project_v1_node_affinity_response_train_selected_types_inner.ProjectV1NodeAffinityResponse_train_selectedTypes_inner(
                                id=1.337,
                                name="",
                            )
                        ],
                    ),
                    interactive=runai.models.project_v1_node_affinity_response_interactive.ProjectV1NodeAffinityResponse_interactive(
                        affinity_type="no_limit",
                        selected_types=[
                            runai.models.project_v1_node_affinity_response_train_selected_types_inner.ProjectV1NodeAffinityResponse_train_selectedTypes_inner(
                                id=1.337,
                                name="",
                            )
                        ],
                    ),
                ),
                permissions=runai.models.project_v1_response_common_fields_permissions.ProjectV1ResponseCommonFields_permissions(
                    users=[""],
                    groups=[""],
                    applications=[""],
                ),
                resources=runai.models.assigned_resources_v1_response.AssignedResourcesV1Response(
                    id=1.337,
                    gpu=None,
                    cpu=None,
                    memory=None,
                ),
                name="team-a",
                namespace="ns-proj1",
                id=5,
                department_id=2,
                tenant_id=2,
                cluster_uuid="71f69d83-ba66-4822-adf5-55ce55efd210",
                department_name="department-a",
                interactive_node_affinity="none",
                train_node_affinity="none",
                created_at="2021-12-14T16:04:15.099Z",
                status=runai.models.project_v1_all_of_status.ProjectV1_allOf_status(
                    namespace="runai-team-a",
                    message="NamespaceHandlerFailed",
                    phase="Ready",
                    conditions=[{"key' : '"}],
                    quota_statuses=[
                        runai.models.quota_status_v1_inner.QuotaStatusV1_inner(
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
                            requested=None,
                        )
                    ],
                ),
                phase="Ready",
                quota_statuses="",
            )
        else:
            return ProjectV1(
                node_pools_resources=[
                    runai.models.node_pool_assigned_resources_v1_response.NodePoolAssignedResourcesV1Response(
                        id=1.337,
                        node_pool=runai.models.node_pool_assigned_resources_v1_response_node_pool.NodePoolAssignedResourcesV1Response_nodePool(
                            id=3,
                            name="default",
                        ),
                        gpu=None,
                        cpu=None,
                        memory=None,
                    )
                ],
                deserved_gpus=3,
                max_allowed_gpus=5,
                gpu_over_quota_weight=1,
                resources=runai.models.assigned_resources_v1_response.AssignedResourcesV1Response(
                    id=1.337,
                    gpu=None,
                    cpu=None,
                    memory=None,
                ),
                namespace="ns-proj1",
            )

    def testProjectV1(self):
        """Test ProjectV1"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
