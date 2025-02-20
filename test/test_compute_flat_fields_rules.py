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
from runai.models.compute_flat_fields_rules import ComputeFlatFieldsRules


class TestComputeFlatFieldsRules(unittest.TestCase):
    """ComputeFlatFieldsRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComputeFlatFieldsRules:
        """Test ComputeFlatFieldsRules
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ComputeFlatFieldsRules`

        # model = ComputeFlatFieldsRules()
        if include_optional:
            return ComputeFlatFieldsRules(
                cpu_core_request=runai.models.number_rules.NumberRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=1.337,
                    max=1.337,
                    step=1.337,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                cpu_core_limit=runai.models.number_rules.NumberRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=1.337,
                    max=1.337,
                    step=1.337,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                cpu_memory_request=runai.models.quantity_rules.QuantityRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    max="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                cpu_memory_limit=runai.models.quantity_rules.QuantityRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    max="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                large_shm_request=runai.models.boolean_rules.BooleanRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                ),
                gpu_request_type=runai.models.gpu_request_rules.GpuRequestRules(),
                mig_profile=runai.models.mig_profile_rules.MigProfileRules(),
                gpu_devices_request=runai.models.integer_rules.IntegerRules(
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
                gpu_portion_request=runai.models.number_rules.NumberRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=1.337,
                    max=1.337,
                    step=1.337,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                gpu_portion_limit=runai.models.number_rules.NumberRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min=1.337,
                    max=1.337,
                    step=1.337,
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                gpu_memory_request=runai.models.quantity_rules.QuantityRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    max="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
                gpu_memory_limit=runai.models.quantity_rules.QuantityRules(
                    source_of_rule={"scope": "project", "projectId": 3},
                    required=True,
                    can_edit=True,
                    min="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    max="-0..1.73182.66.03300982804.9021169267472mmMGGmuikTPEPmTGiGkePiGemGmmnmeiniPPkTPnEePKmnuuEinuiGEEuiGuMETMPTPmeeKPenkETmEkMikEe-521919116647837856387556598",
                    default_from=runai.models.default_from_rule.DefaultFromRule(
                        field="",
                        factor=1.337,
                    ),
                ),
            )
        else:
            return ComputeFlatFieldsRules()

    def testComputeFlatFieldsRules(self):
        """Test ComputeFlatFieldsRules"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
