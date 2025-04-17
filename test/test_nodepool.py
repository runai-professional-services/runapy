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
from runai.models.nodepool import Nodepool


class TestNodepool(unittest.TestCase):
    """Nodepool unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Nodepool:
        """Test Nodepool
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Nodepool`

        # model = Nodepool()
        if include_optional:
            return Nodepool(
                name="v100",
                label_key="node-type",
                label_value="type-x",
                cluster_id="d73a738f-fab3-430a-8fa3-5241493d7128",
                over_provisioning_ratio=1,
                placement_strategy=runai.models.nodepool_create_fields_placement_strategy.NodepoolCreateFields_placementStrategy(
                    cpu="spread",
                    gpu="spread",
                ),
                gpu_network_acceleration_label_key="",
                gpu_network_acceleration_detection="Auto",
                phase="Creating",
                phase_message="all nodes are down",
                status=None,
                id="5",
                tenant_id=1,
                cluster_name="prod-cluster",
                created_by="user@lab.com",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                updated_by="user@lab.com",
                updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                deleted_by="user@lab.com",
                deleted_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                is_default=False,
            )
        else:
            return Nodepool(
                name="v100",
                label_key="node-type",
                label_value="type-x",
                cluster_id="d73a738f-fab3-430a-8fa3-5241493d7128",
                id="5",
                tenant_id=1,
                cluster_name="prod-cluster",
                created_by="user@lab.com",
                created_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                updated_by="user@lab.com",
                updated_at=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f"
                ),
                is_default=False,
            )

    def testNodepool(self):
        """Test Nodepool"""
        inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
