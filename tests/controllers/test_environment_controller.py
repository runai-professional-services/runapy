import pytest
import json
from unittest.mock import Mock, patch

from runai import models
from runai import controllers
from runai import errors
from runai.client import RunaiClient


class TestEnvironmentController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.EnvironmentController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.EnvironmentController(mock_client)
        assert controller.client == mock_client

    def test_all(self, controller):
        mock_response = [{"meta": {"id": 1, "name": "jupyter-lab"}}]

        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/environment"
        )

    def test_get_by_name(self, controller):
        mock_response = {'entries': [{"meta": {"name": "jupyter-lab"}}, {"meta": {"name": "jupyter-tensorboard"}}]}
        controller.client.get.return_value = mock_response

        result = controller.get_by_name(environment_name="jupyter-lab")
        # Note remoted "id": 2
        assert result == {"meta": {"name": "jupyter-lab"}}
       
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/environment"
        )



