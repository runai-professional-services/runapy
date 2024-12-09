import pytest
import json
from unittest.mock import Mock, patch

from runai import models
from runai import controllers
from runai import errors
from runai.client import RunaiClient


class TestTemplateController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.TemplateController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.TemplateController(mock_client)
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
            controllers.TemplateController(client)
        assert "cluster_id is not configured" in str(exc_info)

    def test_all(self, controller):
        # TODO: understand if anything needs to be passed in the response
        mock_response = [{"id": 1, "name": "pool1"}, {"id": 2, "name": "pool2"}]

        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/workload-template"
        )

    def test_get_by_name(self, controller):
        mock_response = {'entries': [{"meta": {"name": "my-template"}}, {"meta": {"name": "my-template-2"}}]}
        controller.client.get.return_value = mock_response

        result = controller.get_by_name(template_name="my-template")
        # Note remoted "id": 2
        assert result == {"meta": {"name": "my-template"}}
       
        controller.client.get.assert_called_once_with(
            "/api/v1/asset/workload-template"
        )

    def test_create(self, controller):
        cluster_id = controller.client.cluster_id
        name="my-template"
        scope="cluster"
        assets = {
            "environment": "1f21043c-3a8a-4049-bd62-4c3135545178",
            "compute": "bbe5a6d1-1c63-4448-b534-036514f8b756",
            "datasources": None,
            "workloadVolumes": None
        }

        expected_payload = {"meta": {"name": name, "scope": scope, "workloadSupportedTypes": None, 
        "description": None, "clusterId": cluster_id, "departmentId": None,
        "projectId": None,"autoDelete": False}, "spec": {"assets": assets, "specificEnv": None}}
        # Trim spaces to match actual json string payload
        expected_payload = json.dumps(expected_payload).replace(" ", "")

        controller.create(
            name=name,
            scope=scope,
            assets=assets
        )

        controller.client.post.assert_called_once_with(
            "/api/v1/asset/workload-template",
            expected_payload
        )

    def test_create_missing_required_field(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(
                name="my-template",
                scope=None,
                 assets={
                    "environment": "2",
                    "compute": "1"
                },
                specificenv = {
                    "command": "echo 'hello world'"
                }
            )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_update(self, controller):
        mock_response = {"id": 1, "name": "updated_template"}
        controller.client.put.return_value = mock_response

        result = controller.update(
            asset_id=1,
            name="updated_template",
             assets={
                    "environment": "2",
                    "compute": "1"
                },
                specificenv = {
                    "command": "echo 'hello world'"
                }
        )

        assert result == mock_response
        controller.client.put.assert_called_once()

    def test_update_bad_parameters(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update(
                asset_id=1,
                name=None,
                assets={
                    "environment": "2",
                    "compute": "1"
                },
                specificenv = {
                    "command": "echo 'hello world'"
                }
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_update_compute(self, controller):
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.put.return_value = mock_response

        result = controller.update(
                asset_id=1,
                name="update_template",
                assets={
                    "environment": "2",
                    "compute": "1"
                }
        )

        assert result == mock_response
        controller.client.put.assert_called_once()

    def test_update_compute_with_specificenv(self, controller):
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.put.return_value = mock_response

        result = controller.update(
                asset_id=1,
                name="update_template",
                assets={
                    "environment": "2",
                    "compute": "1"
                },
                specificenv={"command": "echo 'hello world'"}
        )

        assert result == mock_response
        controller.client.put.assert_called_once()

    def test_update_compute_bad_parameter(self, controller):

        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update(
                asset_id=1,
                name="update_template",
                assets={"environment": "2",
                "compute": 1}
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_update_compute_bad_parameter_specificenv(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update(
                asset_id=1,
                name="update_template",
                assets={
                    "environment": "2",
                    "compute": "1"
                },
                specificenv={"command": 1}
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_delete(self, controller):
        template_asset_id = 1
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.delete.return_value = mock_response

        result = controller.delete(asset_id=template_asset_id)

        assert result == mock_response
        controller.client.delete.assert_called_once_with(
            f"/api/v1/asset/workload-template/{template_asset_id}"
        )

