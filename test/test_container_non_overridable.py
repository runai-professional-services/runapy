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
from runai.models.container_non_overridable import ContainerNonOverridable


class TestContainerNonOverridable(unittest.TestCase):
    """ContainerNonOverridable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContainerNonOverridable:
        """Test ContainerNonOverridable
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContainerNonOverridable`

        # model = ContainerNonOverridable()
        if include_optional:
            return ContainerNonOverridable(
                image="python:3.8",
                image_pull_policy="Always",
                working_dir="/home/myfolder",
                create_home_dir=True,
                probes=runai.models.probes.Probes(
                    readiness=runai.models.probe.Probe(
                        initial_delay_seconds=0,
                        period_seconds=1,
                        timeout_seconds=1,
                        success_threshold=1,
                        failure_threshold=1,
                        handler=runai.models.probe_handler.ProbeHandler(
                            http_get=runai.models.probe_handler_http_get.ProbeHandler_httpGet(
                                path="",
                                port=1,
                                host="",
                                scheme="HTTP",
                            ),
                        ),
                    ),
                ),
            )
        else:
            return ContainerNonOverridable()

    def testContainerNonOverridable(self):
        """Test ContainerNonOverridable"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
