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
from runai.models.common_storage_fields_rules import CommonStorageFieldsRules


class TestCommonStorageFieldsRules(unittest.TestCase):
    """CommonStorageFieldsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonStorageFieldsRules:
        """Test CommonStorageFieldsRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CommonStorageFieldsRules`

        # model = CommonStorageFieldsRules()
        if include_optional:
            return CommonStorageFieldsRules(
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
                pvc=runai.models.pvcs_rules.PvcsRules(
                    attributes=runai.models.pvc_rules.PvcRules(
                        claim_name=runai.models.string_rules.StringRules(),
                        path=runai.models.string_rules.StringRules(),
                        read_only=runai.models.boolean_rules.BooleanRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                        ),
                        claim_info=runai.models.claim_info_rules.ClaimInfoRules(
                            size=runai.models.string_rules.StringRules(),
                            storage_class=runai.models.string_rules.StringRules(),
                            access_modes=runai.models.pvc_access_modes_rules.PvcAccessModesRules(
                                read_write_once=runai.models.boolean_rules.BooleanRules(
                                    required=True,
                                    can_edit=True,
                                ),
                                read_only_many=None,
                                read_write_many=None,
                            ),
                        ),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                host_path=runai.models.host_paths_rules.HostPathsRules(
                    attributes=runai.models.host_path_rules.HostPathRules(
                        path=runai.models.string_rules.StringRules(),
                        read_only=runai.models.boolean_rules.BooleanRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                        ),
                        mount_path=runai.models.string_rules.StringRules(),
                        mount_propagation=runai.models.host_path_mount_propagation_rules.HostPathMountPropagationRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                nfs=runai.models.nfss_rules.NfssRules(
                    attributes=runai.models.nfs_rules.NfsRules(
                        path=runai.models.string_rules.StringRules(),
                        read_only=runai.models.boolean_rules.BooleanRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                        ),
                        server=runai.models.string_rules.StringRules(),
                        mount_path=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                git=runai.models.gits_rules.GitsRules(
                    attributes=runai.models.git_rules.GitRules(
                        repository=runai.models.string_rules.StringRules(),
                        branch=runai.models.string_rules.StringRules(),
                        revision=runai.models.string_rules.StringRules(),
                        path=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                config_map_volume=runai.models.config_maps_rules.ConfigMapsRules(
                    attributes=runai.models.config_map_rules.ConfigMapRules(
                        config_map=runai.models.string_rules.StringRules(),
                        mount_path=runai.models.string_rules.StringRules(),
                        sub_path=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                secret_volume=runai.models.secrets_rules.SecretsRules(
                    attributes=runai.models.secret_rules.SecretRules(
                        secret=runai.models.string_rules.StringRules(),
                        mount_path=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
            )
        else:
            return CommonStorageFieldsRules()

    def testCommonStorageFieldsRules(self):
        """Test CommonStorageFieldsRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
