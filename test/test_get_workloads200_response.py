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
from runai.models.get_workloads200_response import GetWorkloads200Response


class TestGetWorkloads200Response(unittest.TestCase):
    """GetWorkloads200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetWorkloads200Response:
        """Test GetWorkloads200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetWorkloads200Response`

        # model = GetWorkloads200Response()
        if include_optional:
            return GetWorkloads200Response(
                next=1,
                workloads=[
                    runai.models.workload.Workload(
                        tenant_id=1001,
                        running_pods=1,
                        phase_updated_at="2022-06-08T11:28:24.131Z",
                        k8s_phase_updated_at="2022-06-08T11:28:24.131Z",
                        updated_at="2022-06-08T11:28:24.131Z",
                        source="CLI",
                        deleted_at="2022-08-12T19:28:24.131Z",
                        type="runai-job",
                        name="very-important-job",
                        id="",
                        priority=50,
                        priority_class_name="high-priority",
                        submitted_by="researcher@run.ai",
                        cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                        project_name="proj-1",
                        project_id="1",
                        department_name="department-1",
                        department_id="1",
                        namespace="runai-proj-1",
                        created_at="2022-01-01T03:49:52.531Z",
                        workload_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(
                            gpu_request_type="portion",
                            gpu=runai.models.request_resource_cores.RequestResourceCores(
                                limit=1.5,
                                request=1,
                            ),
                            gpu_memory=runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit="2G",
                                request="200M",
                            ),
                            cpu=runai.models.request_resource_cores.RequestResourceCores(
                                limit=1.5,
                                request=1,
                            ),
                            cpu_memory=runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit="2G",
                                request="200M",
                            ),
                            mig_profile=["1g.5gb"],
                            extended_resources=[
                                runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                                    resource="hardware-vendor.example/foo",
                                    quantity="2",
                                    exclude=False,
                                )
                            ],
                        ),
                        pods_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(),
                        allocated_resources=runai.models.workload_allocated_resources.WorkloadAllocatedResources(),
                        actions_support=runai.models.actions_support.ActionsSupport(
                            delete=True,
                            suspend=True,
                        ),
                        phase="Creating",
                        conditions=[
                            runai.models.condition1.Condition1(
                                type="Ready",
                                status="False",
                                message="Resource validation failed: ...",
                                reason="ErrorConfig",
                                last_transition_time="2022-01-01T03:49:52.531Z",
                            )
                        ],
                        phase_message="Not enough resources in the requested nodepool",
                        k8s_phase="Pending",
                        requested_pods=runai.models.requested_pods.RequestedPods(
                            number=1,
                            min=2,
                            max=5,
                            parallelism=3,
                            completions=5,
                        ),
                        requested_node_pools=["default"],
                        current_node_pools=["default"],
                        completed_at="2022-01-01T03:49:52.531Z",
                        images=["alpine:latest"],
                        children_ids=[
                            runai.models.workload_children_ids_inner.Workload_childrenIds_inner(
                                id="",
                                type="",
                            )
                        ],
                        urls=[""],
                        datasources=[
                            runai.models.datasource.Datasource(
                                type="pvc",
                                name="my-pvc-datasource-1",
                                id="",
                            )
                        ],
                        environments=[
                            runai.models.environment.Environment(
                                connections=[
                                    runai.models.connection1.Connection1(
                                        name="my-pytorch-env",
                                        tool_type="pytorch",
                                        connection_type="ExternalUrl",
                                        url="http://wandb.com/yourproject",
                                        authorization_type="public",
                                        authorized_users=[
                                            "user@company.ai",
                                            "another@company.ai",
                                        ],
                                        authorized_groups=["group-a", "group-b"],
                                        container_port=8080,
                                    )
                                ],
                                name="pytorch",
                                id="",
                                replica_type="Master",
                            )
                        ],
                        external_connections=[
                            runai.models.connection1.Connection1(
                                name="my-pytorch-env",
                                tool_type="pytorch",
                                connection_type="ExternalUrl",
                                url="http://wandb.com/yourproject",
                                authorization_type="public",
                                authorized_users=[
                                    "user@company.ai",
                                    "another@company.ai",
                                ],
                                authorized_groups=["group-a", "group-b"],
                                container_port=8080,
                            )
                        ],
                        distributed_framework="Pytorch",
                        additional_fields={},
                        preemptible=True,
                        environment_variables={"key' : '"},
                        command="sleep",
                        arguments="1000",
                        phase_reason=runai.models.phase_reason.phaseReason(),
                        idle_gpus=3,
                        idle_allocated_gpus=1,
                    )
                ],
            )
        else:
            return GetWorkloads200Response(
                workloads=[
                    runai.models.workload.Workload(
                        tenant_id=1001,
                        running_pods=1,
                        phase_updated_at="2022-06-08T11:28:24.131Z",
                        k8s_phase_updated_at="2022-06-08T11:28:24.131Z",
                        updated_at="2022-06-08T11:28:24.131Z",
                        source="CLI",
                        deleted_at="2022-08-12T19:28:24.131Z",
                        type="runai-job",
                        name="very-important-job",
                        id="",
                        priority=50,
                        priority_class_name="high-priority",
                        submitted_by="researcher@run.ai",
                        cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                        project_name="proj-1",
                        project_id="1",
                        department_name="department-1",
                        department_id="1",
                        namespace="runai-proj-1",
                        created_at="2022-01-01T03:49:52.531Z",
                        workload_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(
                            gpu_request_type="portion",
                            gpu=runai.models.request_resource_cores.RequestResourceCores(
                                limit=1.5,
                                request=1,
                            ),
                            gpu_memory=runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit="2G",
                                request="200M",
                            ),
                            cpu=runai.models.request_resource_cores.RequestResourceCores(
                                limit=1.5,
                                request=1,
                            ),
                            cpu_memory=runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit="2G",
                                request="200M",
                            ),
                            mig_profile=["1g.5gb"],
                            extended_resources=[
                                runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                                    resource="hardware-vendor.example/foo",
                                    quantity="2",
                                    exclude=False,
                                )
                            ],
                        ),
                        pods_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(),
                        allocated_resources=runai.models.workload_allocated_resources.WorkloadAllocatedResources(),
                        actions_support=runai.models.actions_support.ActionsSupport(
                            delete=True,
                            suspend=True,
                        ),
                        phase="Creating",
                        conditions=[
                            runai.models.condition1.Condition1(
                                type="Ready",
                                status="False",
                                message="Resource validation failed: ...",
                                reason="ErrorConfig",
                                last_transition_time="2022-01-01T03:49:52.531Z",
                            )
                        ],
                        phase_message="Not enough resources in the requested nodepool",
                        k8s_phase="Pending",
                        requested_pods=runai.models.requested_pods.RequestedPods(
                            number=1,
                            min=2,
                            max=5,
                            parallelism=3,
                            completions=5,
                        ),
                        requested_node_pools=["default"],
                        current_node_pools=["default"],
                        completed_at="2022-01-01T03:49:52.531Z",
                        images=["alpine:latest"],
                        children_ids=[
                            runai.models.workload_children_ids_inner.Workload_childrenIds_inner(
                                id="",
                                type="",
                            )
                        ],
                        urls=[""],
                        datasources=[
                            runai.models.datasource.Datasource(
                                type="pvc",
                                name="my-pvc-datasource-1",
                                id="",
                            )
                        ],
                        environments=[
                            runai.models.environment.Environment(
                                connections=[
                                    runai.models.connection1.Connection1(
                                        name="my-pytorch-env",
                                        tool_type="pytorch",
                                        connection_type="ExternalUrl",
                                        url="http://wandb.com/yourproject",
                                        authorization_type="public",
                                        authorized_users=[
                                            "user@company.ai",
                                            "another@company.ai",
                                        ],
                                        authorized_groups=["group-a", "group-b"],
                                        container_port=8080,
                                    )
                                ],
                                name="pytorch",
                                id="",
                                replica_type="Master",
                            )
                        ],
                        external_connections=[
                            runai.models.connection1.Connection1(
                                name="my-pytorch-env",
                                tool_type="pytorch",
                                connection_type="ExternalUrl",
                                url="http://wandb.com/yourproject",
                                authorization_type="public",
                                authorized_users=[
                                    "user@company.ai",
                                    "another@company.ai",
                                ],
                                authorized_groups=["group-a", "group-b"],
                                container_port=8080,
                            )
                        ],
                        distributed_framework="Pytorch",
                        additional_fields={},
                        preemptible=True,
                        environment_variables={"key' : '"},
                        command="sleep",
                        arguments="1000",
                        phase_reason=runai.models.phase_reason.phaseReason(),
                        idle_gpus=3,
                        idle_allocated_gpus=1,
                    )
                ],
            )

    def testGetWorkloads200Response(self):
        """Test GetWorkloads200Response"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
