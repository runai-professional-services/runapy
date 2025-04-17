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
from runai.models.overridable_spec_fields import OverridableSpecFields


class TestOverridableSpecFields(unittest.TestCase):
    """OverridableSpecFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OverridableSpecFields:
        """Test OverridableSpecFields
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OverridableSpecFields`

        # model = OverridableSpecFields()
        if include_optional:
            return OverridableSpecFields(
                command="python",
                args="-x my-script.py",
                run_as_uid=500,
                run_as_gid=30,
                supplemental_groups="2,3,5,8",
                environment_variables=[
                    runai.models.environment_variable_of_asset.EnvironmentVariableOfAsset(
                        name="HOME",
                        value="/home/my-folder",
                        credential=runai.models.environment_variable_credential.EnvironmentVariableCredential(
                            asset_id="0",
                            key="POSTGRES_PASSWORD",
                        ),
                        config_map=runai.models.environment_variable_config_map.EnvironmentVariableConfigMap(
                            name="my-config-map",
                            key="MY_POSTGRES_SCHEMA",
                        ),
                        pod_field_ref=runai.models.environment_variable_pod_field_reference.EnvironmentVariablePodFieldReference(
                            path="metadata.name",
                        ),
                        exclude=False,
                        description="Home directory of the user.",
                    )
                ],
            )
        else:
            return OverridableSpecFields()

    def testOverridableSpecFields(self):
        """Test OverridableSpecFields"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
