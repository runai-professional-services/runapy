from unittest.mock import Mock

import pytest

from runai import errors
from runai.assets import AccessKeyController, PasswordController, DockerRegistryController


@pytest.fixture
def mock_client():
    return Mock()


def test_access_key_create(mock_client):
    controller = AccessKeyController(mock_client)
    controller.create(
        name="test-access-key",
        scope="system",
        access_key_id="ACIVJXLQQTGRRXKNPAI3",
        access_key_secret="tBb7gR3zQcgZ184eTNETxXFyytEPXu3ewWTXTdSb"
    )
    mock_client.post.assert_called_once_with(
        "/api/v1/asset/credentials/access-key",
        '{"meta":{"name":"test-access-key","scope":"system","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"existingSecretName":null,"accessKeyId":"ACIVJXLQQTGRRXKNPAI3","secretAccessKey":"tBb7gR3zQcgZ184eTNETxXFyytEPXu3ewWTXTdSb"}}'
    )


def test_access_key_create_fail_existing_access_key_with_user(mock_client):
    controller = AccessKeyController(mock_client)
    with pytest.raises(errors.RunaiBuildModelError) as exc_info:
        controller.create(
            name="test-access-key",
            scope="system",
            existing_secret_name="some-access-key",
            access_key_id="ACIVJXLQQTGRRXKNPAI3",
        )
    assert "Failed to build body scheme" in str(exc_info)
    controller.client.post.assert_not_called()


def test_password_create(mock_client):
    controller = PasswordController(mock_client)
    controller.create(
        name="test-password",
        scope="system",
        user="test",
        password="pass"
    )
    mock_client.post.assert_called_once_with(
        "/api/v1/asset/credentials/password",
        '{"meta":{"name":"test-password","scope":"system","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"existingSecretName":null,"user":"test","password":"pass"}}'
    )


def test_password_create_fail_existing_password_with_user(mock_client):
    controller = PasswordController(mock_client)
    with pytest.raises(errors.RunaiBuildModelError) as exc_info:
        controller.create(
            name="test-password",
            scope="system",
            existing_secret_name="some-password",
            user="test",
        )
    assert "Failed to build body scheme" in str(exc_info)
    controller.client.post.assert_not_called()


def test_docker_registry_create(mock_client):
    controller = DockerRegistryController(mock_client)
    controller.create(
        name="test-docker-registry",
        url="private.org.docker.io",
        scope="system",
        user="test",
        password="pass"
    )
    mock_client.post.assert_called_once_with(
        "/api/v1/asset/credentials/docker-registry",
        '{"meta":{"name":"test-docker-registry","scope":"system","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"url":"private.org.docker.io","existingSecretName":null,"user":"test","password":"pass"}}'
    )


def test_docker_registry_create_fail_existing_secret_with_user(mock_client):
    controller = DockerRegistryController(mock_client)
    with pytest.raises(errors.RunaiBuildModelError) as exc_info:
        controller.create(
            name="test-docker-registry",
            url="private.org.docker.io",
            scope="system",
            existing_secret_name="some-secret",
            user="test",
        )
    assert "Failed to build body scheme" in str(exc_info)
    controller.client.post.assert_not_called()
