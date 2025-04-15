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
from runai.models.common_storage_rules import CommonStorageRules


class TestCommonStorageRules(unittest.TestCase):
    """CommonStorageRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonStorageRules:
        """Test CommonStorageRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CommonStorageRules`

        # model = CommonStorageRules()
        if include_optional:
            return CommonStorageRules(
                storage=runai.models.common_storage_fields_rules.CommonStorageFieldsRules(
                    data_volume=runai.models.data_volumes_rules.DataVolumesRules(
                        attributes=runai.models.data_volume_rules.DataVolumeRules(
                            id=runai.models.string_rules.StringRules(),
                            mount_path=runai.models.string_rules.StringRules(),
                        ),
                        instances=runai.models.item_rules.ItemRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            can_add=True,
                            locked=["HOME", "USER"],
                        ),
                    ),
                    pvc=runai.models.pvcs_rules.PvcsRules(),
                    host_path=runai.models.host_paths_rules.HostPathsRules(),
                    nfs=runai.models.nfss_rules.NfssRules(),
                    git=runai.models.gits_rules.GitsRules(),
                    config_map_volume=runai.models.config_maps_rules.ConfigMapsRules(),
                    secret_volume=runai.models.secrets_rules.SecretsRules(),
                )
            )
        else:
            return CommonStorageRules()

    def testCommonStorageRules(self):
        """Test CommonStorageRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
