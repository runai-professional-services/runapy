import pytest

from unittest.mock import Mock, patch

from runai import controllers
from tests.utilities import load_test_data


class TestRolesController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.RolesController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.RolesController(mock_client)
        assert controller.client == mock_client

    def test_all(self, controller):
        mock_response = (
            {
                "name": "System administrator",
                "description": "A system administrator can:\nControl all aspects of the system: users, organizations, compute resources, general settings, etc.\nThis role has global system control and should be limited to a small group of skilled IT administrators.",
                "permissions": [],
                "id": 1,
                "createdAt": "2023-09-18T11:20:05.188383Z",
                "updatedAt": "2024-08-07T12:08:32.61371Z",
                "createdBy": "Run:ai",
            },
        )
        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with("/api/v1/authorization/roles")

    def test_get(self, controller):
        role_id = 1
        mock_response = (
            {
                "name": "System administrator",
                "description": "A system administrator can:\nControl all aspects of the system: users, organizations, compute resources, general settings, etc.\nThis role has global system control and should be limited to a small group of skilled IT administrators.",
                "permissions": [],
                "id": role_id,
                "createdAt": "2023-09-18T11:20:05.188383Z",
                "updatedAt": "2024-08-07T12:08:32.61371Z",
                "createdBy": "Run:ai",
            },
        )
        controller.client.get.return_value = mock_response

        result = controller.get(role_id=role_id)

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            f"/api/v1/authorization/roles/{role_id}"
        )

    def test_get_roles_name_to_id_map(self, controller):
        expected = {
            "System administrator": 1,
            "Data volume administrator": 2256,
            "L1 researcher": 5,
            "ML engineer": 6,
            "Viewer": 7,
            "L2 researcher": 8,
            "Environment administrator": 9,
            "Credentials administrator": 373,
            "Data source administrator": 10,
            "Cloud support": 1709,
            "Editor": 3,
            "Research manager": 4,
            "Department viewer": 13,
            "Application administrator": 1708,
            "Department administrator": 1710,
            "Cloud operator": 1711,
            "Compute resource administrator": 11,
            "Template administrator": 12,
        }

        mock_response_data = load_test_data("roles_list.json")
        with patch.object(
            controller.client, "get", return_value=mock_response_data
        ) as mock_get:
            result = controller.get_roles_name_to_id_map()

        assert result == expected
        mock_get.assert_called_once_with("/api/v1/authorization/roles")
