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
from runai.models.superset_spec import SupersetSpec


class TestSupersetSpec(unittest.TestCase):
    """SupersetSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupersetSpec:
        """Test SupersetSpec
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SupersetSpec`

        # model = SupersetSpec()
        if include_optional:
            return SupersetSpec(
                command="python",
                args="-x my-script.py",
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
                node_type="my-node-type",
                node_pools=[my - node - pool - a, my - node - pool - b],
                pod_affinity=runai.models.pod_affinity.PodAffinity(
                    type="Required",
                    key="",
                ),
                tty=True,
                stdin=True,
                environment_variables=[
                    runai.models.environment_variable.EnvironmentVariable(
                        name="HOME",
                        value="/home/my-folder",
                        secret=runai.models.environment_variable_secret.EnvironmentVariableSecret(
                            name="postgress_secret",
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
                annotations=[
                    runai.models.annotation.Annotation(
                        name="billing",
                        value="my-billing-unit",
                        exclude=False,
                    )
                ],
                labels=[
                    runai.models.label.Label(
                        name="stage",
                        value="initial-research",
                        exclude=False,
                    )
                ],
                tolerations=[
                    runai.models.toleration.Toleration(
                        name="0",
                        operator="Equal",
                        key="",
                        value="",
                        effect="NoSchedule",
                        seconds=1,
                        exclude=False,
                    )
                ],
                terminate_after_preemption=False,
                auto_deletion_time_after_completion_seconds=15,
                termination_grace_period_seconds=20,
                backoff_limit=3,
                restart_policy="Always",
                ports=[
                    runai.models.port.Port(
                        container=8080,
                        service_type="LoadBalancer",
                        external=30080,
                        tool_type="pytorch",
                        tool_name="my-pytorch",
                        name="port-instance-a",
                        exclude=False,
                    )
                ],
                exposed_urls=[
                    runai.models.exposed_url.ExposedUrl(
                        container=8080,
                        url="https://my-url.com",
                        authorized_users=["user-a", "user-b"],
                        authorized_groups=["group-a", "group-b"],
                        tool_type="jupyter",
                        tool_name="my-pytorch",
                        name="url-instance-a",
                        exclude=False,
                    )
                ],
                related_urls=[
                    runai.models.related_url.RelatedUrl(
                        url="https://my-url.com",
                        type="wandb",
                        name="url-instance-a",
                        exclude=False,
                    )
                ],
                priority_class="build",
                completions=1,
                parallelism=1,
                num_workers=1,
                distributed_framework="MPI",
                slots_per_worker=1,
                ssh_auth_mount_path="/root/.ssh",
                min_replicas=56,
                max_replicas=56,
                clean_pod_policy="None",
                serving_port=runai.models.serving_port.ServingPort(),
                autoscaling=runai.models.auto_scaling.AutoScaling(),
                security=runai.models.security_flat_fields.SecurityFlatFields(),
                compute=runai.models.compute_fields.ComputeFields(),
                storage=runai.models.storage_fields.StorageFields(),
            )
        else:
            return SupersetSpec()

    def testSupersetSpec(self):
        """Test SupersetSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
