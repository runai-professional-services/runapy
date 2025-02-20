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
from runai.models.datasource_list_response_entry import DatasourceListResponseEntry


class TestDatasourceListResponseEntry(unittest.TestCase):
    """DatasourceListResponseEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatasourceListResponseEntry:
        """Test DatasourceListResponseEntry
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DatasourceListResponseEntry`

        # model = DatasourceListResponseEntry()
        if include_optional:
            return DatasourceListResponseEntry(
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
                spec=runai.models.datasource_list_response_asset_spec.DatasourceListResponseAssetSpec(
                    host_path=runai.models.host_path.hostPath(),
                    nfs=runai.models.nfs.nfs(),
                    pvc=runai.models.pvc.pvc(),
                    git=runai.models.git.git(),
                    s3=runai.models.s3.s3(),
                    config_map=runai.models.config_map.config_map(),
                    secret=runai.models.secret.secret(),
                ),
                used_by=runai.models.asset_usage_info.AssetUsageInfo(
                    workspaces=[
                        runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                            id="",
                            name="my-workload-name",
                            status="0",
                        )
                    ],
                    trainings=[
                        runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                            id="",
                            name="my-workload-name",
                            status="0",
                        )
                    ],
                    distributed=[],
                    inferences=[],
                    templates=[
                        runai.models.asset_ref.AssetRef(
                            id="0",
                            name="my-asset",
                        )
                    ],
                    assets=runai.models.assets_usage_ref.AssetsUsageRef(
                        environment=runai.models.environment.environment(),
                        environments=[
                            runai.models.asset_ref.AssetRef(
                                id="0",
                                name="my-asset",
                            )
                        ],
                        compute=runai.models.assets_usage_ref_compute.AssetsUsageRefCompute(),
                        computes=[],
                        datasources=[
                            runai.models.asset_datasource_ref.AssetDatasourceRef(
                                id="0",
                                name="my-asset",
                                kind="compute",
                                overrides=runai.models.data_source_overrides.DataSourceOverrides(
                                    container_path="/container/directory",
                                ),
                            )
                        ],
                    ),
                ),
                usage_times=runai.models.usage_times_info.UsageTimesInfo(
                    last_used_by_workload=datetime.datetime.strptime(
                        "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                    ),
                ),
                compliance=runai.models.compliance_info.ComplianceInfo(
                    imposed=True,
                    compliance=True,
                    reason=[
                        runai.models.compliance_info_reason.ComplianceInfoReason(
                            field="",
                            details="",
                        )
                    ],
                ),
                status=runai.models.asset_cluster_status_info.AssetClusterStatusInfo(
                    status="Issues found",
                    issues=[
                        runai.models.asset_cluster_status_issue.AssetClusterStatusIssue(
                            scope_id="",
                            scope_type="system",
                            issue="ReplicationError",
                        )
                    ],
                    message="",
                    url="",
                ),
                cluster_info=runai.models.cluster_info1.ClusterInfo1(
                    resources=[
                        runai.models.cluster_resource_info.ClusterResourceInfo(
                            name="password-credential-1",
                        )
                    ],
                ),
            )
        else:
            return DatasourceListResponseEntry(
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
                spec=runai.models.datasource_list_response_asset_spec.DatasourceListResponseAssetSpec(
                    host_path=runai.models.host_path.hostPath(),
                    nfs=runai.models.nfs.nfs(),
                    pvc=runai.models.pvc.pvc(),
                    git=runai.models.git.git(),
                    s3=runai.models.s3.s3(),
                    config_map=runai.models.config_map.config_map(),
                    secret=runai.models.secret.secret(),
                ),
            )

    def testDatasourceListResponseEntry(self):
        """Test DatasourceListResponseEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
