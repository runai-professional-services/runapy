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
from runai.models.project_update_request1 import ProjectUpdateRequest1


class TestProjectUpdateRequest1(unittest.TestCase):
    """ProjectUpdateRequest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectUpdateRequest1:
        """Test ProjectUpdateRequest1
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ProjectUpdateRequest1`

        # model = ProjectUpdateRequest1()
        if include_optional:
            return ProjectUpdateRequest1(
                deserved_gpus=3,
                max_allowed_gpus=5,
                gpu_over_quota_weight=1,
                default_node_pools=[default],
                interactive_job_time_limit_secs=3600,
                interactive_job_max_idle_duration_secs=3000,
                interactive_preemptible_job_max_idle_duration_secs=3000,
                training_job_time_limit_secs=3600,
                training_job_max_idle_duration_secs=3000,
                node_affinity=runai.models.jobs_node_affinity.JobsNodeAffinity(
                    train=None,
                    interactive=None,
                ),
                permissions=runai.models.resource_permissions.ResourcePermissions(
                    users=[""],
                    groups=[""],
                    applications=[""],
                ),
                resources=runai.models.assigned_resources.AssignedResources(
                    id=1.337,
                    gpu=None,
                    cpu=None,
                    memory=None,
                ),
                node_pools_resources=[null],
            )
        else:
            return ProjectUpdateRequest1()

    def testProjectUpdateRequest1(self):
        """Test ProjectUpdateRequest1"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
