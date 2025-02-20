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
from runai.models.distributed_policy_rules_v2_worker import (
    DistributedPolicyRulesV2Worker,
)


class TestDistributedPolicyRulesV2Worker(unittest.TestCase):
    """DistributedPolicyRulesV2Worker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DistributedPolicyRulesV2Worker:
        """Test DistributedPolicyRulesV2Worker
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DistributedPolicyRulesV2Worker`

        # model = DistributedPolicyRulesV2Worker()
        if include_optional:
            return DistributedPolicyRulesV2Worker(
                command=runai.models.string_rules.StringRules(),
                args=runai.models.string_rules.StringRules(),
                image=runai.models.string_rules.StringRules(),
                image_pull_policy=runai.models.image_pull_policy_rules.ImagePullPolicyRules(),
                working_dir=runai.models.string_rules.StringRules(),
                create_home_dir=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                probes=runai.models.probes_rules.ProbesRules(
                    readiness=runai.models.probe_rules.ProbeRules(
                        initial_delay_seconds=runai.models.integer_rules.IntegerRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                            default_from=runai.models.default_from_rule.DefaultFromRule(
                                field="",
                                factor=1.337,
                            ),
                        ),
                        period_seconds=runai.models.integer_rules.IntegerRules(
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                        ),
                        timeout_seconds=None,
                        success_threshold=None,
                        failure_threshold=None,
                        handler=runai.models.probe_handler_rules.ProbeHandlerRules(
                            http_get=runai.models.probe_handler_rules_http_get.ProbeHandlerRules_httpGet(
                                path=runai.models.string_rules.StringRules(),
                                port=None,
                                host=runai.models.string_rules.StringRules(),
                                scheme=runai.models.string_rules.StringRules(),
                            ),
                        ),
                    ),
                ),
                node_type=runai.models.string_rules.StringRules(),
                node_pools=runai.models.array_rules.ArrayRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    options=[
                        {"value": "value", "displayed": "A description of the value."}
                    ],
                    can_edit=True,
                ),
                pod_affinity=runai.models.pod_affinity_rules.PodAffinityRules(
                    type=runai.models.pod_affinity_type_rules.PodAffinityTypeRules(),
                    key=runai.models.string_rules.StringRules(),
                ),
                environment_variables=runai.models.instances_rules.InstancesRules(
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                annotations=runai.models.instances_rules.InstancesRules(
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                labels=runai.models.instances_rules.InstancesRules(
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                tolerations=runai.models.tolerations_rules.TolerationsRules(
                    attributes=runai.models.toleration_rules.TolerationRules(
                        operator=runai.models.toleration_operator_rules.TolerationOperatorRules(),
                        key=runai.models.string_rules.StringRules(),
                        value=runai.models.string_rules.StringRules(),
                        effect=runai.models.toleration_effect_rules.TolerationEffectRules(),
                        seconds=runai.models.integer_rules.IntegerRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                            default_from=runai.models.default_from_rule.DefaultFromRule(
                                field="",
                                factor=1.337,
                            ),
                        ),
                        exclude=runai.models.boolean_rules.BooleanRules(
                            required=True,
                            can_edit=True,
                        ),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                terminate_after_preemption=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                auto_deletion_time_after_completion_seconds=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                termination_grace_period_seconds=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                backoff_limit=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                ports=runai.models.ports_rules.PortsRules(
                    attributes=runai.models.port_rules.PortRules(
                        container=runai.models.integer_rules.IntegerRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                            default_from=runai.models.default_from_rule.DefaultFromRule(
                                field="",
                                factor=1.337,
                            ),
                        ),
                        service_type=runai.models.port_service_type_rules.PortServiceTypeRules(),
                        custom_external_port=runai.models.boolean_rules.BooleanRules(
                            required=True,
                            can_edit=True,
                        ),
                        external=runai.models.integer_rules.IntegerRules(
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                        ),
                        tool_type=runai.models.string_rules.StringRules(),
                        tool_name=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                exposed_urls=runai.models.exposed_urls_rules.ExposedUrlsRules(
                    attributes=runai.models.exposed_url_rules.ExposedUrlRules(
                        container=runai.models.integer_rules.IntegerRules(
                            source_of_rule={"scope": "project", "projectId": 3},
                            required=True,
                            can_edit=True,
                            min=56,
                            max=56,
                            step=56,
                            default_from=runai.models.default_from_rule.DefaultFromRule(
                                field="",
                                factor=1.337,
                            ),
                        ),
                        custom_url=runai.models.boolean_rules.BooleanRules(
                            required=True,
                            can_edit=True,
                        ),
                        url=runai.models.string_rules.StringRules(),
                        authorized_users=runai.models.array_rules.ArrayRules(
                            required=True,
                            options=[
                                {
                                    "value": "value",
                                    "displayed": "A description of the value.",
                                }
                            ],
                            can_edit=True,
                        ),
                        tool_type=runai.models.string_rules.StringRules(),
                        tool_name=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                related_urls=runai.models.related_urls_rules.RelatedUrlsRules(
                    attributes=runai.models.related_url_rules.RelatedUrlRules(
                        url=runai.models.string_rules.StringRules(),
                        type=runai.models.string_rules.StringRules(),
                        name=runai.models.string_rules.StringRules(),
                    ),
                    instances=runai.models.item_rules.ItemRules(
                        source_of_rule={"scope": "project", "projectId": 3},
                        can_add=True,
                        locked=["HOME", "USER"],
                    ),
                ),
                security=runai.models.security_flat_fields_rules.SecurityFlatFieldsRules(),
                compute=runai.models.compute_fields_rules.ComputeFieldsRules(),
                storage=runai.models.storage_fields_rules.StorageFieldsRules(),
                num_workers=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                distributed_framework=runai.models.distributed_framework_rules.DistributedFrameworkRules(),
                slots_per_worker=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                min_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                max_replicas=runai.models.integer_rules.IntegerRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=56,
                    max=56,
                    step=56,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                clean_pod_policy=runai.models.distributed_clean_pod_policy_rules.DistributedCleanPodPolicyRules(),
            )
        else:
            return DistributedPolicyRulesV2Worker()

    def testDistributedPolicyRulesV2Worker(self):
        """Test DistributedPolicyRulesV2Worker"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
