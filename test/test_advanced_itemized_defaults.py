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
from runai.models.advanced_itemized_defaults import AdvancedItemizedDefaults


class TestAdvancedItemizedDefaults(unittest.TestCase):
    """AdvancedItemizedDefaults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedItemizedDefaults:
        """Test AdvancedItemizedDefaults
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AdvancedItemizedDefaults`

        # model = AdvancedItemizedDefaults()
        if include_optional:
            return AdvancedItemizedDefaults(
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
                        exclude=False,
                    ),
                    instances=[
                        runai.models.toleration.Toleration(
                            name="0",
                            key="",
                            value="",
                            seconds=1,
                            exclude=False,
                        )
                    ],
                ),
            )
        else:
            return AdvancedItemizedDefaults()

    def testAdvancedItemizedDefaults(self):
        """Test AdvancedItemizedDefaults"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
