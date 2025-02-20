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
from runai.models.common_security_non_overridable_rules import (
    CommonSecurityNonOverridableRules,
)


class TestCommonSecurityNonOverridableRules(unittest.TestCase):
    """CommonSecurityNonOverridableRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSecurityNonOverridableRules:
        """Test CommonSecurityNonOverridableRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CommonSecurityNonOverridableRules`

        # model = CommonSecurityNonOverridableRules()
        if include_optional:
            return CommonSecurityNonOverridableRules(
                uid_gid_source=runai.models.uid_gid_source_rules.UidGidSourceRules(),
                capabilities=runai.models.array_rules.ArrayRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    options=[
                        {"value": "value", "displayed": "A description of the value."}
                    ],
                    can_edit=True,
                ),
                seccomp_profile_type=runai.models.seccomp_profile_type_rules.SeccompProfileTypeRules(),
                run_as_non_root=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                read_only_root_filesystem=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
            )
        else:
            return CommonSecurityNonOverridableRules()

    def testCommonSecurityNonOverridableRules(self):
        """Test CommonSecurityNonOverridableRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
