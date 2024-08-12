import pytest
import json
from unittest.mock import Mock

from runai import controllers


class TestUsersController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.UsersController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.UsersController(mock_client)
        assert controller.client == mock_client

    def test_create(self, controller):
        email = "test@run.ai"
        to_reset_password = True

        expected_body = {"email": email, "resetPassword": to_reset_password}
        expected_body = json.dumps(expected_body).replace(" ", "")

        controller.create(email=email, to_reset_password=to_reset_password)

        controller.client.post.assert_called_once_with(
            "/api/v1/users", expected_body
        )
