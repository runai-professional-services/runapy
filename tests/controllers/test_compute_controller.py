import pytest
import json
from unittest.mock import Mock, patch

from runai import models
from runai import controllers
from runai import errors
from runai.client import RunaiClient


class TestComputeController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.ComputeController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.ComputeController(mock_client)
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
            controllers.ComputeController(client)
        assert "cluster_id is not configured" in str(exc_info)

    def test_all(self, controller):
        mock_response = [{"meta": {"id": 1, "name": "cpu-only"}}]

        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/compute"
        )

    def test_get_by_name(self, controller):
        mock_response = {'entries': [{"meta": {"name": "cpu-only"}}, {"meta": {"name": "gpu-only"}}]}
        controller.client.get.return_value = mock_response

        result = controller.get_by_name(compute_name="cpu-only")
        # Note remoted "id": 2
        assert result == {"meta": {"name": "cpu-only"}}
       
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/compute"
        )



