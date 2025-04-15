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
from runai.models.workload_template_list_response import WorkloadTemplateListResponse


class TestWorkloadTemplateListResponse(unittest.TestCase):
    """WorkloadTemplateListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadTemplateListResponse:
        """Test WorkloadTemplateListResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `WorkloadTemplateListResponse`

        # model = WorkloadTemplateListResponse()
        if include_optional:
            return WorkloadTemplateListResponse(
                entries=[
                    runai.models.workload_template.WorkloadTemplate(
                        meta={
                            "name": "my-asset",
                            "scope": "tenant",
                            "id": "a418ed33-9399-48c0-a890-122cadd13bfd",
                            "kind": "s3",
                            "createdBy": "test@run.ai",
                            "createdAt": "2023-02-23T14:25:36.707685Z",
                            "updatedBy": "test@run.ai",
                            "updatedAt": "2023-02-23T14:25:36.707685Z",
                            "workloadSupportedTypes": {
                                "workspace": False,
                                "training": False,
                                "distributed": True,
                                "distFramework": "TF",
                            },
                        },
                        spec=runai.models.specific_run_info_fields.SpecificRunInfoFields(
                            assets=runai.models.assets_ref.AssetsRef(
                                environment=None,
                                compute=runai.models.assets_ref_compute.AssetsRefCompute(),
                                datasources=[
                                    runai.models.datasource_ref.DatasourceRef(
                                        id="0",
                                        name="my-asset",
                                        kind="compute",
                                        overrides=runai.models.data_source_overrides.DataSourceOverrides(
                                            container_path="/container/directory",
                                        ),
                                    )
                                ],
                                workload_volumes=[""],
                            ),
                            specific_env=runai.models.specific_run_params.SpecificRunParams(),
                            distributed=runai.models.info_distributed.InfoDistributed(),
                        ),
                    )
                ]
            )
        else:
            return WorkloadTemplateListResponse(
                entries=[
                    runai.models.workload_template.WorkloadTemplate(
                        meta={
                            "name": "my-asset",
                            "scope": "tenant",
                            "id": "a418ed33-9399-48c0-a890-122cadd13bfd",
                            "kind": "s3",
                            "createdBy": "test@run.ai",
                            "createdAt": "2023-02-23T14:25:36.707685Z",
                            "updatedBy": "test@run.ai",
                            "updatedAt": "2023-02-23T14:25:36.707685Z",
                            "workloadSupportedTypes": {
                                "workspace": False,
                                "training": False,
                                "distributed": True,
                                "distFramework": "TF",
                            },
                        },
                        spec=runai.models.specific_run_info_fields.SpecificRunInfoFields(
                            assets=runai.models.assets_ref.AssetsRef(
                                environment=None,
                                compute=runai.models.assets_ref_compute.AssetsRefCompute(),
                                datasources=[
                                    runai.models.datasource_ref.DatasourceRef(
                                        id="0",
                                        name="my-asset",
                                        kind="compute",
                                        overrides=runai.models.data_source_overrides.DataSourceOverrides(
                                            container_path="/container/directory",
                                        ),
                                    )
                                ],
                                workload_volumes=[""],
                            ),
                            specific_env=runai.models.specific_run_params.SpecificRunParams(),
                            distributed=runai.models.info_distributed.InfoDistributed(),
                        ),
                    )
                ],
            )

    def testWorkloadTemplateListResponse(self):
        """Test WorkloadTemplateListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
