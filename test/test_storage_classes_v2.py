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
from runai.models.storage_classes_v2 import StorageClassesV2


class TestStorageClassesV2(unittest.TestCase):
    """StorageClassesV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StorageClassesV2:
        """Test StorageClassesV2
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `StorageClassesV2`

        # model = StorageClassesV2()
        if include_optional:
            return StorageClassesV2(
                items=[
                    runai.models.storage_class_v2.StorageClassV2(
                        cluster_id="550e8400-e29b-41d4-a716-446655440000",
                        storage_class_name="my-storage-class",
                        spec=runai.models.storage_class_spec.StorageClassSpec(
                            provisioner="kubernetes.io/aws-ebs",
                            allow_volume_expansion=True,
                            is_default=False,
                        ),
                        permissions=runai.models.storage_class_permissions.StorageClassPermissions(
                            allowed_for_assets=True,
                            allowed_for_workloads=True,
                            allowed_for_ephemeral_volumes=True,
                            allowed_for_persistent_volumes=True,
                        ),
                        customization=runai.models.storage_class_customization.StorageClassCustomization(
                            access_mode=runai.models.access_mode_customization.AccessModeCustomization(
                                required=True,
                                default=runai.models.pvc_access_modes.PvcAccessModes(
                                    read_write_once=True,
                                    read_only_many=True,
                                    read_write_many=True,
                                ),
                                supported_values=runai.models.pvc_supported_access_modes.PvcSupportedAccessModes(
                                    read_write_once=True,
                                    read_only_many=True,
                                    read_write_many=True,
                                ),
                            ),
                            volume_mode=runai.models.volume_mode_customization.VolumeModeCustomization(
                                required=True,
                            ),
                            claim_size=runai.models.claim_size_customization.ClaimSizeCustomization(
                                supported_units=["MB"],
                                min="1G",
                                max="1G",
                                step="1G",
                            ),
                        ),
                    )
                ]
            )
        else:
            return StorageClassesV2(
                items=[
                    runai.models.storage_class_v2.StorageClassV2(
                        cluster_id="550e8400-e29b-41d4-a716-446655440000",
                        storage_class_name="my-storage-class",
                        spec=runai.models.storage_class_spec.StorageClassSpec(
                            provisioner="kubernetes.io/aws-ebs",
                            allow_volume_expansion=True,
                            is_default=False,
                        ),
                        permissions=runai.models.storage_class_permissions.StorageClassPermissions(
                            allowed_for_assets=True,
                            allowed_for_workloads=True,
                            allowed_for_ephemeral_volumes=True,
                            allowed_for_persistent_volumes=True,
                        ),
                        customization=runai.models.storage_class_customization.StorageClassCustomization(
                            access_mode=runai.models.access_mode_customization.AccessModeCustomization(
                                required=True,
                                default=runai.models.pvc_access_modes.PvcAccessModes(
                                    read_write_once=True,
                                    read_only_many=True,
                                    read_write_many=True,
                                ),
                                supported_values=runai.models.pvc_supported_access_modes.PvcSupportedAccessModes(
                                    read_write_once=True,
                                    read_only_many=True,
                                    read_write_many=True,
                                ),
                            ),
                            volume_mode=runai.models.volume_mode_customization.VolumeModeCustomization(
                                required=True,
                            ),
                            claim_size=runai.models.claim_size_customization.ClaimSizeCustomization(
                                supported_units=["MB"],
                                min="1G",
                                max="1G",
                                step="1G",
                            ),
                        ),
                    )
                ],
            )

    def testStorageClassesV2(self):
        """Test StorageClassesV2"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
