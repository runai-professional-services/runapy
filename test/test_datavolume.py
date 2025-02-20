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
from runai.models.datavolume import Datavolume


class TestDatavolume(unittest.TestCase):
    """Datavolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Datavolume:
        """Test Datavolume
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Datavolume`

        # model = Datavolume()
        if include_optional:
            return Datavolume(
                id="71f69d83-ba66-4822-adf5-55ce55efd210",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                created_by="user@run.ai",
                updated_by="user@run.ai",
                name="datavolume-a",
                description="Results of experiment X",
                origin_pvc_name="pvc-a",
                project_id="5",
                should_delete_original_volume=False,
                project_name="project-a",
                department_id="department-a",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                shared_scopes=[null],
                status=runai.models.datavolume_status.DatavolumeStatus(
                    phase="Ready",
                    phase_message="Failed to copy pvc to project 'project-a'",
                    conditions=[
                        runai.models.condition2.Condition2(
                            type="PvcsCreated",
                            status="False",
                            message="Failed to create pvc in namespace 'runai-proj1'",
                            reason="ErrorCreatingPvc",
                            last_transition_time="2022-01-01T03:49:52.531Z",
                        )
                    ],
                    datavolume_pvc_name="datavolume-pvc-1",
                    datavolume_pv_name="datavolume-pv-1",
                ),
            )
        else:
            return Datavolume(
                id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="datavolume-a",
                origin_pvc_name="pvc-a",
                project_id="5",
                project_name="project-a",
                status=runai.models.datavolume_status.DatavolumeStatus(
                    phase="Ready",
                    phase_message="Failed to copy pvc to project 'project-a'",
                    conditions=[
                        runai.models.condition2.Condition2(
                            type="PvcsCreated",
                            status="False",
                            message="Failed to create pvc in namespace 'runai-proj1'",
                            reason="ErrorCreatingPvc",
                            last_transition_time="2022-01-01T03:49:52.531Z",
                        )
                    ],
                    datavolume_pvc_name="datavolume-pvc-1",
                    datavolume_pv_name="datavolume-pv-1",
                ),
            )

    def testDatavolume(self):
        """Test Datavolume"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
