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
from runai.models.cluster_reported_status import ClusterReportedStatus

class TestClusterReportedStatus(unittest.TestCase):
    """ClusterReportedStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterReportedStatus:
        """Test ClusterReportedStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterReportedStatus`

        # model = ClusterReportedStatus()
        if include_optional:
            return ClusterReportedStatus(
                conditions = [
                    runai.models.cluster_reported_status_conditions_inner.ClusterReportedStatus_conditions_inner(
                        last_transition_time = datetime.datetime.strptime("2013-10-20 19:20:30.00\', \'%Y-%m-%d %H:%M:%S.%f"), 
                        message = '', 
                        observed_generation = 0, 
                        reason = 'AbUUGjjNSwg1_bs:ZayIMrKdgNvb7gvxmPb:GcsM72ate2RA9:q4w2l5eH5XxEz06awo0', 
                        status = 'True', 
                        type = '', )
                    ],
                operands = {
                    'key' : runai.models.cluster_reported_status_operands_value.ClusterReportedStatus_operands_value(
                        last_transition_time = datetime.datetime.strptime("2013-10-20 19:20:30.00\', \'%Y-%m-%d %H:%M:%S.%f"), 
                        ready = True, 
                        reasons = [
                            ''
                            ], 
                        unready_threshold_crossed = True, )
                    },
                platform = runai.models.cluster_reported_status_platform.ClusterReportedStatus_platform(
                    type = 'vanilla', 
                    kube_version = '', ),
                config = runai.models.cluster_reported_config.ClusterReportedConfig(
                    workload_ownership_protection = False, 
                    subdomain_enabled = False, ),
                dependencies = runai.models.cluster_dependencies_status.ClusterDependenciesStatus(
                    required = {
                        'key' : runai.models.cluster_dependency_status.ClusterDependencyStatus(
                            available = True, 
                            reason = '', 
                            components = {
                                'key' : runai.models.cluster_dependency_status.ClusterDependencyStatus(
                                    available = True, 
                                    reason = '', )
                                }, )
                        }, 
                    optional = {
                        'key' : 
                        }, )
            )
        else:
            return ClusterReportedStatus(
        )

    def testClusterReportedStatus(self):
        """Test ClusterReportedStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        #inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()