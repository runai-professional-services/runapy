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
from runai.models.replica_defaults_v2 import ReplicaDefaultsV2


class TestReplicaDefaultsV2(unittest.TestCase):
    """ReplicaDefaultsV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReplicaDefaultsV2:
        """Test ReplicaDefaultsV2
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ReplicaDefaultsV2`

        # model = ReplicaDefaultsV2()
        if include_optional:
            return ReplicaDefaultsV2(
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
                                path="",
                                port=1,
                                host="",
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
                ),
                annotations=runai.models.annotations_defaults.AnnotationsDefaults(
                    instances=[
                        runai.models.annotation.Annotation(
                            name="billing",
                            value="my-billing-unit",
                            exclude=False,
                        )
                    ],
                ),
                labels=runai.models.labels_defaults.LabelsDefaults(
                    instances=[
                        runai.models.label.Label(
                            name="stage",
                            value="initial-research",
                            exclude=False,
                        )
                    ],
                ),
                tolerations=runai.models.tolerations_defaults.TolerationsDefaults(
                    attributes=runai.models.toleration.Toleration(
                        name="0",
                        operator="Equal",
                        key="",
                        value="",
                        effect="NoSchedule",
                        seconds=1,
                    ),
                    instances=[
                        runai.models.toleration.Toleration(
                            name="0",
                            key="",
                            value="",
                            seconds=1,
                        )
                    ],
                ),
                terminate_after_preemption=False,
                auto_deletion_time_after_completion_seconds=15,
                backoff_limit=3,
                ports=runai.models.ports_defaults.PortsDefaults(
                    attributes=runai.models.port.Port(
                        container=8080,
                        service_type="LoadBalancer",
                        external=30080,
                        tool_type="pytorch",
                        tool_name="my-pytorch",
                        name="port-instance-a",
                    ),
                    instances=[
                        runai.models.port.Port(
                            container=8080,
                            external=30080,
                            tool_type="pytorch",
                            tool_name="my-pytorch",
                            name="port-instance-a",
                        )
                    ],
                ),
                exposed_urls=runai.models.exposed_urls_defaults.ExposedUrlsDefaults(
                    attributes=runai.models.exposed_url.ExposedUrl(
                        container=8080,
                        url="https://my-url.com",
                        authorized_users=["user-a", "user-b"],
                        authorized_groups=["group-a", "group-b"],
                        tool_type="jupyter",
                        tool_name="my-pytorch",
                        name="url-instance-a",
                    ),
                    instances=[
                        runai.models.exposed_url.ExposedUrl(
                            container=8080,
                            url="https://my-url.com",
                            authorized_users=["user-a", "user-b"],
                            authorized_groups=["group-a", "group-b"],
                            tool_type="jupyter",
                            tool_name="my-pytorch",
                            name="url-instance-a",
                        )
                    ],
                ),
                related_urls=runai.models.related_urls_defaults.RelatedUrlsDefaults(
                    attributes=runai.models.related_url.RelatedUrl(
                        url="https://my-url.com",
                        type="wandb",
                        name="url-instance-a",
                    ),
                    instances=[
                        runai.models.related_url.RelatedUrl(
                            url="https://my-url.com",
                            type="wandb",
                            name="url-instance-a",
                        )
                    ],
                ),
                security=runai.models.security_flat_fields.SecurityFlatFields(),
                compute=runai.models.compute_fields_defaults.ComputeFieldsDefaults(),
                storage=runai.models.storage_fields_defaults.StorageFieldsDefaults(),
            )
        else:
            return ReplicaDefaultsV2()

    def testReplicaDefaultsV2(self):
        """Test ReplicaDefaultsV2"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
