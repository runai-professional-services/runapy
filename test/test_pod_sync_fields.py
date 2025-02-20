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
from runai.models.pod_sync_fields import PodSyncFields


class TestPodSyncFields(unittest.TestCase):
    """PodSyncFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PodSyncFields:
        """Test PodSyncFields
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PodSyncFields`

        # model = PodSyncFields()
        if include_optional:
            return PodSyncFields(
                name="pod-of-a-very-important-job",
                priority_class_name="high-priority",
                id="",
                workload_id="",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                project_id="1",
                node_name="gpu-node-1",
                created_at="2022-01-01T03:49:52.531Z",
                completed_at="2022-01-01T03:49:52.531Z",
                containers=[
                    runai.models.container1.Container1(
                        name="busybox",
                        image="busybox:latest",
                        started_at="2022-01-01T03:49:52.531Z",
                    )
                ],
                current_node_pool="default",
                requested_node_pools=["default"],
                requested_resources=runai.models.pod_request_resources.PodRequestResources(
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
                    mig_profile="1g.5gb",
                    extended_resources=[
                        runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                            resource="hardware-vendor.example/foo",
                            quantity="2",
                            exclude=False,
                        )
                    ],
                ),
                allocated_resources=runai.models.allocated_resources.AllocatedResources(
                    gpu=1.5,
                    mig_profile="1g.5gb",
                    gpu_memory="200Mi",
                    cpu=0.5,
                    cpu_memory="0B",
                    extended_resources=[
                        runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                            resource="hardware-vendor.example/foo",
                            quantity="2",
                            exclude=False,
                        )
                    ],
                ),
                tolerations=[
                    runai.models.pod_toleration.PodToleration(
                        key="",
                        operator="Exists",
                        value="",
                        effect="NoExecute",
                        toleration_seconds=10,
                    )
                ],
                k8s_phase="Pending",
            )
        else:
            return PodSyncFields(
                name="pod-of-a-very-important-job",
                priority_class_name="high-priority",
                id="",
                workload_id="",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                created_at="2022-01-01T03:49:52.531Z",
                containers=[
                    runai.models.container1.Container1(
                        name="busybox",
                        image="busybox:latest",
                        started_at="2022-01-01T03:49:52.531Z",
                    )
                ],
                k8s_phase="Pending",
            )

    def testPodSyncFields(self):
        """Test PodSyncFields"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
