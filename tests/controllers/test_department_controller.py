import pytest
import json
from unittest.mock import Mock, patch

from runai import controllers
from runai import models
from runai import errors
from runai.client import RunaiClient


class TestDepartmentController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.DepartmentController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.DepartmentController(mock_client)
        assert controller.client == mock_client
    
    def test_init_missing_cluster_id(self):
        with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
            with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
                client = RunaiClient(
                    client_id="api-client",
                    client_secret="test-client-secret",
                    runai_base_url="https://test.runai.ai"
                )
        with pytest.raises(errors.RunaiClusterIDNotConfigured) as exc_info:
            controllers.DepartmentController(client)
        assert "cluster_id is not configured" in str(exc_info)

    def test_all(self, controller):
        mock_response = {
            "departments": [
                {
                    "id": 1,
                    "name": "department1",
                    "createdAt": "2022-12-13T12:49:21.49Z",
                    "updatedAt": "2024-07-21T19:30:18.497444Z",
                    "resources": [
                        {
                            "nodePool": {"id": "530", "name": "default"},
                            "gpu": {"deserved": 1, "limit": 2, "overQuotaWeight": 0},
                        }
                    ],
                },
                {
                    "id": 2,
                    "name": "department2",
                    "createdAt": "2022-12-13T12:49:21.49Z",
                    "updatedAt": "2024-07-21T19:30:18.497444Z",
                    "resources": [
                        {
                            "nodePool": {"id": "530", "name": "default"},
                            "gpu": {"deserved": 0, "limit": -1, "overQuotaWeight": 0},
                        }
                    ],
                },
            ]
        }
        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/org-unit/departments", models.DepartmentQueryParams()
        )

    def test_all_with_filters(self, controller):
        mock_response = {
            "departments": [
                {
                    "resources": [
                        {
                            "nodePool": {"id": "3078", "name": "default"},
                            "gpu": {"deserved": 2, "limit": -1, "overQuotaWeight": 2},
                        }
                    ],
                    "name": "default",
                    "clusterId": "0ee12059-9047-4a7e-a2ff-3b16d3a0dd99",
                    "id": "4501823",
                    "createdAt": "2024-08-07T08:55:12.971511Z",
                    "updatedAt": "2024-08-07T09:37:26.559938Z",
                    "updatedBy": "ofir@run.ai",
                }
            ]
        }
        controller.client.get.return_value = mock_response

        result = controller.all(
            filterBy="clusterId==0ee12059-9047-4a7e-a2ff-3b16d3a0dd99", limit=1
        )

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/org-unit/departments",
            models.DepartmentQueryParams(
                filterBy="clusterId==0ee12059-9047-4a7e-a2ff-3b16d3a0dd99", limit=1
            ),
        )

    def test_all_wrong_filter_convention(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.all(
                filterBy={"clusterId": "0ee12059-9047-4a7e-a2ff-3b16d3a0dd99"}, limit=1
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_create(self, controller):
        department_name = "some_department"
        mock_response = {"id": 3, "name": department_name}
        controller.client.post.return_value = mock_response

        cluster_id = controller.client.cluster_id
        resources = [
            {
                "nodePool": {"id": "22", "name": "default"},
                "gpu": {"deserved": 0, "limit": 0, "overQuotaWeight": 2},
                "cpu": None,
                "memory": None,
            }
        ]

        expected_body = {
            "name": department_name,
            "clusterId": cluster_id,
            "resources": resources,
        }

        expected_body = json.dumps(expected_body).replace(" ", "")

        result = controller.create(name=department_name, resources=resources)

        assert result == mock_response
        controller.client.post.assert_called_once_with(
            "/api/v1/org-unit/departments", expected_body
        )

    def test_create_missing_gpu_resources(self, controller):
        department_name = "some_department"
        resources = [
            {
                "nodePool": {"id": "22", "name": "default"},
                "cpu": None,
                "memory": None,
            }
        ]
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(name=department_name, resources=resources)
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_get(self, controller):
        department_id = 1
        mock_response = {"id": department_id, "name": "department1"}
        controller.client.get.return_value = mock_response

        result = controller.get(department_id=department_id)

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            f"/api/v1/org-unit/departments/{department_id}"
        )

    def test_update_resources(self, controller):
        department_id = "3"
        resources = [
            {
                "nodePool": {"id": "22", "name": "default"},
                "gpu": {"deserved": 0, "limit": 0, "overQuotaWeight": 2},
                "cpu": None,
                "memory": None,
            }
        ]

        controller.update_resources(
            department_id=department_id, resources=resources
        )

        expected_body = resources

        controller.client.put.assert_called_once_with(
            f"/api/v1/org-unit/departments/{department_id}/resources",
            expected_body
        )

    def test_update_resources_missing_gpu_resource(self, controller):
        department_id = "3"
        resources = [
            {
                "nodePool": {"id": "22", "name": "default"},
                "cpu": None,
                "memory": None,
            }
        ]
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update_resources(
                department_id=department_id, resources=resources
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.put.assert_not_called()

    def test_delete(self, controller):
        department_id = 1
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.delete.return_value = mock_response

        result = controller.delete(department_id=department_id)

        assert result == mock_response
        controller.client.delete.assert_called_once_with(
            f"/api/v1/org-unit/departments/{department_id}"
        )
    
    def test_patch_resources_missing_required_gpu(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.patch(
                department_id=1,
                resources={
                    "nodePool": {
                        "id": "1",
                        "name": "default",
                    },
                })
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.patch.assert_not_called()
