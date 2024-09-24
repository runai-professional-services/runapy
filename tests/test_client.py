import logging

from unittest.mock import Mock, patch, ANY

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from pydantic import HttpUrl

from runai import controllers
from runai import assets
from runai.client import RunaiClient, RunaiClientConfig
from runai.errors import RunaiHTTPError, RunaiClientError, RunaiBuildModelError


@pytest.fixture
def runai_client():
    with patch("runai.client.requests.post"):
        with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
            with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
                mock_token = "token.token"
                mock_token_epiary = 1727185600

                client = RunaiClient(
                    client_id="api-client",
                    client_secret="test-client-secret",
                    runai_base_url="https://test.runai.ai",
                    cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
                )
                client._api_token = mock_token
                client._api_token_expiary = mock_token_epiary

                yield client


def test_runai_client_config():
    config = RunaiClientConfig(
        client_id="api-client",
        client_secret="test-client-secret",
        runai_base_url="https://test.runai.ai",
        cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        retries=3,
        debug=True,
    )
    assert config.client_id == "api-client"
    assert config.client_secret == "test-client-secret"
    assert config.runai_base_url == HttpUrl("https://test.runai.ai")
    assert config.cluster_id == "7d82b243-9ef4-4819-83c2-b15733b652d3"
    assert config.retries == 3
    assert config.debug


def test_runai_client_wrong_field_type():
    with patch("runai.client.requests.post") as mock_post, patch(
        "runai.client.requests.Session"
    ) as mock_session:
        with pytest.raises(RunaiBuildModelError) as exc_info:
            RunaiClient(
                client_id=5,
                client_secret="test",
                cluster_id="api-client",
                runai_base_url=HttpUrl("https://test.runai.ai"),
            )

            assert "Failed to build body scheme" in str(exc_info)
            mock_post.assert_not_called()
            mock_session.assert_not_called()


@patch("runai.client.requests.Session")
@patch("runai.client.HTTPAdapter")
@patch("runai.client.Retry")
def test_create_session(mock_retry, mock_adapter, mock_session):
    with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
        with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
            mock_session_instance = Mock()
            mock_session.return_value = mock_session_instance  # Mock the Session object
            mock_adapter_instance = Mock()
            mock_adapter.return_value = mock_adapter_instance  # Mock the HTTPAdapter

            retries_value = 3
            
            client = RunaiClient(
                client_id="test-client-id",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
                retries=retries_value
            )

            mock_session.assert_called_once()
            mock_retry.assert_called_once_with(
                total=retries_value,
                backoff_factor=2,
                status_forcelist=[500, 502, 503, 504],
                allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
                raise_on_status=False,
            )
            mock_adapter.assert_called_once_with(max_retries=mock_retry.return_value)
            mock_session_instance.mount.assert_called_once_with("https://", mock_adapter_instance)
            assert client._session == mock_session_instance


def test_generate_api_token_unauthorized_http_error():
    with patch("runai.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_post.return_value = mock_response

        with pytest.raises(RunaiHTTPError) as exc_info:
            RunaiClient(
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            )
        assert "[401] - Unauthorized" in str(exc_info.value)


def test_generate_api_token_json_decode_error():
    with patch("runai.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError("", "", 0)
        mock_post.return_value = mock_response

        with pytest.raises(RunaiClientError) as exc_info:
            RunaiClient(
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            )
        assert "Failed to decode response to json" in str(exc_info)


def test_generate_api_token_missing_access_token():
    with patch("runai.client.requests.post"):
        with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
            mock_response = Mock()
            mock_response.json.return_value = {"not-access-token": "not-access-token"}

            with pytest.raises(RunaiClientError) as exc_info:
                RunaiClient(
                    client_id="api-client",
                    client_secret="test-client-secret",
                    runai_base_url="https://test.runai.ai",
                    cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
                )
            assert "Failed to get access token from response" in str(exc_info)


@patch("logging.basicConfig")
def test_client_logging_configuration(mock_logging_config):
    with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
        with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
            RunaiClient(
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
                debug=True,
            )
            mock_logging_config.assert_called_once_with(level=logging.DEBUG)


@patch("logging.basicConfig")
def test_client_default_logging_configuration(mock_logging_config):
    with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
        with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
            RunaiClient(
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            )
            mock_logging_config.assert_not_called()


def test_client_controller_properties(runai_client):
    controllers_dict = {
        "clusters": controllers.ClusterController,
        "access_rules": controllers.AccessRulesController,
        "roles": controllers.RolesController,
        "departments": controllers.DepartmentController,
        "projects": controllers.ProjectController,
        "node_pools": controllers.NodePoolController,
        "users": controllers.UsersController,
        "workloads": controllers.WorkloadsController,
        "workspace": controllers.WorkspaceController,
        "training": controllers.TrainingController,
        "inference": controllers.InferenceController,
        "distributed": controllers.DistributedController,
        "assets": assets.AssetsFactory}

    client_properties = runai_client.__class__.__dict__

    for controller_name, controller_cls in controllers_dict.items():
        assert controller_name in client_properties
        controller_attr = getattr(runai_client, controller_name)
        assert isinstance(controller_attr, controller_cls)


def test_succesfull_cluster_init_no_cluster_id():
    with patch("runai.client.RunaiClient._generate_api_token", return_value="token"):
        with patch("runai.client.RunaiClient._set_token_expiary", return_value="1727185600"):
            client = RunaiClient(
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai"
            )

            assert isinstance(client, RunaiClient)


def test_cluster_config_cluster_id(runai_client):
    cluster_id = "7d82b243-9ef4-4819-83c2-b15733b652d3"

    runai_client.config_cluster_id(cluster_id)

    assert runai_client.cluster_id == cluster_id


def test_cluster_config_cluster_id_wrong_uuid_type(runai_client):
    wrong_type_uuid1_cluster_id = "de531c90-608e-11ef-b864-0242ac120002"

    with pytest.raises(RunaiBuildModelError) as exc_info:
        runai_client.config_cluster_id(wrong_type_uuid1_cluster_id)

    assert "Failed to build body scheme" in str(exc_info)
