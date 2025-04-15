# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

import runai
from runai.models.get_workload_history200_response import GetWorkloadHistory200Response


class TestGetWorkloadHistory200Response(unittest.TestCase):
    """GetWorkloadHistory200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetWorkloadHistory200Response:
        """Test GetWorkloadHistory200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetWorkloadHistory200Response`

        # model = GetWorkloadHistory200Response()
        if include_optional:
            return GetWorkloadHistory200Response(
                next=1,
                records=[
                    runai.models.history_record.HistoryRecord(
                        meta=runai.models.history_record_meta.HistoryRecordMeta(
                            creation_timestamp="2022-01-01T03:49:52.531Z",
                            type="Event",
                        ),
                        spec=runai.models.history_record_spec.HistoryRecord_spec(
                            event=runai.models.event1.Event1(
                                created_at="2022-01-01T03:49:52.531Z",
                                id="",
                                type="Normal",
                                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                                message="Started container z",
                                reason="Started",
                                source="kubelet",
                                involved_object=runai.models.involved_object.InvolvedObject(
                                    uid="",
                                    kind="Pod",
                                    name="test-0-1",
                                    namespace="runai-test",
                                ),
                            ),
                            phase_update=runai.models.phase_update.PhaseUpdate(
                                phase="Creating",
                                phase_message="Not enough resources in the requested nodepool",
                            ),
                        ),
                    )
                ],
            )
        else:
            return GetWorkloadHistory200Response(
                records=[
                    runai.models.history_record.HistoryRecord(
                        meta=runai.models.history_record_meta.HistoryRecordMeta(
                            creation_timestamp="2022-01-01T03:49:52.531Z",
                            type="Event",
                        ),
                        spec=runai.models.history_record_spec.HistoryRecord_spec(
                            event=runai.models.event1.Event1(
                                created_at="2022-01-01T03:49:52.531Z",
                                id="",
                                type="Normal",
                                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                                message="Started container z",
                                reason="Started",
                                source="kubelet",
                                involved_object=runai.models.involved_object.InvolvedObject(
                                    uid="",
                                    kind="Pod",
                                    name="test-0-1",
                                    namespace="runai-test",
                                ),
                            ),
                            phase_update=runai.models.phase_update.PhaseUpdate(
                                phase="Creating",
                                phase_message="Not enough resources in the requested nodepool",
                            ),
                        ),
                    )
                ],
            )

    def testGetWorkloadHistory200Response(self):
        """Test GetWorkloadHistory200Response"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
