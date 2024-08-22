import logging

from unittest.mock import Mock, patch, ANY

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from pydantic import HttpUrl

from runai import controllers
from runai.client import RunaiClient, RunaiClientConfig
from runai.errors import RunaiHTTPError, RunaiClientError, RunaiBuildModelError


@pytest.fixture
def mock_client():
    with patch("runai.client.requests.post") as mock_post, patch(
        "runai.client.requests.Session"
    ) as mock_session:

        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = {"access_token": "mocked-api-token"}

        mock_session_instance = Mock()
        mock_session.return_value = mock_session_instance

        client = RunaiClient(
            realm="test-realm",
            client_id="api-client",
            client_secret="test-client-secret",
            runai_base_url="https://test.runai.ai",
            cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        )

        client._session = mock_session_instance

        yield client


@pytest.fixture
def mock_response():
    response = Mock()
    response.ok = True
    return response


def test_runai_client_config():
    config = RunaiClientConfig(
        realm="test-realm",
        client_id="api-client",
        client_secret="test-client-secret",
        runai_base_url="https://test.runai.ai",
        cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        retries=3,
        debug=True,
    )
    assert config.realm == "test-realm"
    assert config.client_id == "api-client"
    assert config.client_secret == "test-client-secret"
    assert config.runai_base_url == HttpUrl("https://test.runai.ai")
    assert config.cluster_id == "7d82b243-9ef4-4819-83c2-b15733b652d3"
    assert config.retries == 3
    assert config.debug == True


def test_runai_client_wrong_field_type():
    with patch("runai.client.requests.post") as mock_post, patch(
        "runai.client.requests.Session"
    ) as mock_session:
        with pytest.raises(RunaiBuildModelError) as exc_info:
            RunaiClient(
                realm="realm",
                client_id=5,
                client_secret="test",
                cluster_id="api-client",
                runai_base_url=HttpUrl("https://test.runai.ai"),
            )

            assert "Failed to build body scheme" in str(exc_info)
            mock_post.assert_not_called()
            mock_session.assert_not_called()


def test_create_session():
    with patch("runai.client.requests.post") as mock_post, patch(
        "runai.client.requests.Session"
    ) as mock_session:

        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = {"access_token": "test-token"}

        mock_session_instance = Mock()
        mock_session.return_value = mock_session_instance

        client = RunaiClient(
            realm="test-realm",
            client_id="test-client-id",
            client_secret="test-client-secret",
            runai_base_url="https://test.runai.ai",
            cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        )

        assert client._session == mock_session_instance
        mock_session_instance.headers.update.assert_called_once_with(
            {"authorization": "Bearer test-token", "content-type": "application/json"}
        )
        mock_session_instance.mount.assert_called_once_with("https://", ANY)


@pytest.mark.parametrize("retries, expected_retries", [(3, 3), (None, 1)])
@patch("runai.client.requests.Session")
@patch("runai.client.requests.post")
def test_client_retry_mechanism(mock_post, mock_session, retries, expected_retries):
    mock_post.return_value.ok = True
    mock_post.return_value.json.return_value = {"access_token": "test-token"}

    mock_session.return_value = mock_session

    RunaiClient(
        realm="test-realm",
        client_id="api-client",
        client_secret="test-client-secret",
        runai_base_url="https://test.runai.ai",
        cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        retries=retries,
    )

    mock_session.mount.assert_called_once_with("https://", ANY)

    # Get the HTTPAdapter and Retry objects
    http_adapter = mock_session.mount.call_args[0][1]
    retry_obj = http_adapter.max_retries

    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter.max_retries == retry_obj

    assert isinstance(retry_obj, Retry)
    assert retry_obj.total == expected_retries
    assert retry_obj.backoff_factor == 2
    assert retry_obj.status_forcelist == [500, 502, 503, 504]
    assert retry_obj.allowed_methods == ["GET", "POST", "PUT", "DELETE"]


def test_generate_api_token_success():
    with patch("runai.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"access_token": "test-token"}
        mock_post.return_value = mock_response

        client_id = "some-client"
        client_secret = "test-client-secret"
        client = RunaiClient(
            realm="test-realm",
            client_id=client_id,
            client_secret=client_secret,
            runai_base_url="https://test.runai.ai",
            cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        )

        assert client._api_token == "test-token"
        mock_post.assert_called_once_with(
            "https://test.runai.ai/auth/realms/test-realm/protocol/openid-connect/token",
            data=f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}",
            headers={"content-type": "application/x-www-form-urlencoded"},
        )


def test_generate_api_token_unauthorized_http_error():
    with patch("runai.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_post.return_value = mock_response

        with pytest.raises(RunaiHTTPError) as exc_info:
            RunaiClient(
                realm="test-realm",
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
        mock_response.text = "Invalid JSON"
        mock_post.return_value = mock_response

        with pytest.raises(RunaiClientError) as exc_info:
            RunaiClient(
                realm="test-realm",
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            )
        assert "Failed to decode response to json" in str(exc_info)


def test_generate_api_token_missing_access_token():
    with patch("runai.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"token": "not-access-token"}
        mock_post.return_value = mock_response

        with pytest.raises(RunaiClientError) as exc_info:
            RunaiClient(
                realm="test-realm",
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai",
                cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            )
        assert "Failed to get access token from response" in str(exc_info)


@patch("logging.basicConfig")
def test_client_logging_configuration(mock_logging_config):
    with patch.object(RunaiClient, "_generate_api_token"):
        RunaiClient(
            realm="test-realm",
            client_id="api-client",
            client_secret="test-client-secret",
            runai_base_url="https://test.runai.ai",
            cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
            debug=True,
        )
        mock_logging_config.assert_called_once_with(level=logging.DEBUG)


@patch("logging.basicConfig")
def test_client_default_logging_configuration(mock_logging_config):
    with patch.object(RunaiClient, "_generate_api_token"):
        RunaiClient(
            realm="test-realm",
            client_id="api-client",
            client_secret="test-client-secret",
            runai_base_url="https://test.runai.ai",
            cluster_id="7d82b243-9ef4-4819-83c2-b15733b652d3",
        )
        mock_logging_config.assert_not_called()


def test_client_controller_properties(mock_client):
    assert isinstance(mock_client.clusters, controllers.ClusterController)
    assert isinstance(mock_client.access_rules, controllers.AccessRulesController)
    assert isinstance(mock_client.roles, controllers.RolesController)
    assert isinstance(mock_client.departments, controllers.DepartmentController)
    assert isinstance(mock_client.projects, controllers.ProjectController)
    assert isinstance(mock_client.node_pools, controllers.NodePoolController)
    assert isinstance(mock_client.users, controllers.UsersController)
    assert isinstance(mock_client.workloads, controllers.WorkloadsController)
    assert isinstance(mock_client.workspace, controllers.WorkspaceController)
    assert isinstance(mock_client.training, controllers.TrainingController)
    assert isinstance(mock_client.inference, controllers.InferenceController)
    assert isinstance(mock_client.distributed, controllers.DistributedController)


def test_succesfull_cluster_init_no_cluster_id():
    with patch.object(RunaiClient, "_generate_api_token"):
        client = RunaiClient(
            realm="test-realm",
            client_id="api-client",
            client_secret="test-client-secret",
            runai_base_url="https://test.runai.ai"
        )
    assert isinstance(client, RunaiClient)


def test_cluster_config_cluster_id(mock_client):
    cluster_id = "7d82b243-9ef4-4819-83c2-b15733b652d3"

    mock_client.config_cluster_id(cluster_id)

    assert mock_client.cluster_id == cluster_id


def test_cluster_config_cluster_id_wrong_uuid_type(mock_client):
    wrong_type_uuid1_cluster_id = "de531c90-608e-11ef-b864-0242ac120002"

    with pytest.raises(RunaiBuildModelError) as exc_info:
        mock_client.config_cluster_id(wrong_type_uuid1_cluster_id)

    assert "Failed to build body scheme" in str(exc_info)
