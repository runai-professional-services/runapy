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
from runai.models.environment_asset_spec import EnvironmentAssetSpec


class TestEnvironmentAssetSpec(unittest.TestCase):
    """EnvironmentAssetSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentAssetSpec:
        """Test EnvironmentAssetSpec
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EnvironmentAssetSpec`

        # model = EnvironmentAssetSpec()
        if include_optional:
            return EnvironmentAssetSpec(
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
                                path="/",
                                port=1,
                                host="example.com",
                                scheme="HTTP",
                            ),
                        ),
                    ),
                ),
                uid_gid_source="fromTheImage",
                capabilities=[CHOWN, KILL],
                seccomp_profile_type="RuntimeDefault",
                run_as_non_root=True,
                read_only_root_filesystem=False,
                tty=True,
                stdin=True,
                allow_privilege_escalation=False,
                host_ipc=False,
                host_network=False,
                connections=[
                    runai.models.connection.Connection(
                        name="0",
                        is_external=True,
                        internal_tool_info=runai.models.internal_tool_info.InternalToolInfo(
                            tool_type="jupyter-notebook",
                            connection_type="LoadBalancer",
                            container_port=1,
                            node_port_info=runai.models.node_port_info.NodePortInfo(
                                is_custom_port=True,
                            ),
                            external_url_info=runai.models.external_url_info.ExternalUrlInfo(
                                is_custom_url=True,
                                external_url="0",
                            ),
                            serving_port_info=runai.models.serving_port_info.ServingPortInfo(
                                protocol="grpc",
                            ),
                        ),
                        external_tool_info=runai.models.external_tool_info.ExternalToolInfo(
                            tool_type="wandb",
                            external_url="https://wandb.com/myteam/${PROJECT_NAME}",
                        ),
                    )
                ],
                override_uid_gid_in_workspace=True,
            )
        else:
            return EnvironmentAssetSpec()

    def testEnvironmentAssetSpec(self):
        """Test EnvironmentAssetSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
