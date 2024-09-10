from unittest.mock import Mock

import pytest

from runai.assets import CredentialsFactory, AccessKeyController, PasswordController, DockerRegistryController


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def credentials_factory():
    factory = CredentialsFactory(mock_client)
    return factory


def test_assets_factory_controllers_as_properties(credentials_factory):
    assert isinstance(credentials_factory.access_key, AccessKeyController)
    assert isinstance(credentials_factory.password, PasswordController)
    assert isinstance(credentials_factory.docker_registry_secret, DockerRegistryController)
