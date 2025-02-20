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
from runai.models.environment_variables_field_defaults import (
    EnvironmentVariablesFieldDefaults,
)


class TestEnvironmentVariablesFieldDefaults(unittest.TestCase):
    """EnvironmentVariablesFieldDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentVariablesFieldDefaults:
        """Test EnvironmentVariablesFieldDefaults
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EnvironmentVariablesFieldDefaults`

        # model = EnvironmentVariablesFieldDefaults()
        if include_optional:
            return EnvironmentVariablesFieldDefaults(
                environment_variables=runai.models.environment_variables_defaults.EnvironmentVariablesDefaults(
                    instances=[
                        runai.models.environment_variable.EnvironmentVariable(
                            name="HOME",
                            value="/home/my-folder",
                            secret=runai.models.environment_variable_secret.EnvironmentVariableSecret(
                                name="postgress_secret",
                                key="POSTGRES_PASSWORD",
                            ),
                            exclude=False,
                        )
                    ],
                )
            )
        else:
            return EnvironmentVariablesFieldDefaults()

    def testEnvironmentVariablesFieldDefaults(self):
        """Test EnvironmentVariablesFieldDefaults"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
