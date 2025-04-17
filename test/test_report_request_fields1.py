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
from runai.models.report_request_fields1 import ReportRequestFields1


class TestReportRequestFields1(unittest.TestCase):
    """ReportRequestFields1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportRequestFields1:
        """Test ReportRequestFields1
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ReportRequestFields1`

        # model = ReportRequestFields1()
        if include_optional:
            return ReportRequestFields1(
                name="2023 GPU report",
                description="This report shows the GPU usage of all projects in the organization",
                metrics=[
                    runai.models.metric_information_for_report.MetricInformationForReport(
                        name="gpu_allocation_hours",
                        display_name="GPU allocation hours",
                        filters={"key": [""]},
                    )
                ],
                labels=[
                    runai.models.label1.Label1(
                        name="nodepoolName",
                        display_name="Node pool",
                    )
                ],
                range=runai.models.range.Range(
                    start=datetime.datetime.strptime(
                        "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                    ),
                    end=datetime.datetime.strptime(
                        "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                    ),
                ),
                additional_fields={},
            )
        else:
            return ReportRequestFields1(
                name="2023 GPU report",
                metrics=[
                    runai.models.metric_information_for_report.MetricInformationForReport(
                        name="gpu_allocation_hours",
                        display_name="GPU allocation hours",
                        filters={"key": [""]},
                    )
                ],
                range=runai.models.range.Range(
                    start=datetime.datetime.strptime(
                        "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                    ),
                    end=datetime.datetime.strptime(
                        "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                    ),
                ),
            )

    def testReportRequestFields1(self):
        """Test ReportRequestFields1"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
