from unittest.mock import Mock

import pytest

from runai.assets import AssetsFactory, PVCController, S3Controller, GitController, NFSController


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def assets_factory():
    factory = AssetsFactory(mock_client)
    return factory


def test_assets_factory_controllers_as_properties(assets_factory):
    assert isinstance(assets_factory.pvc, PVCController)
    assert isinstance(assets_factory.nfs, NFSController)
    assert isinstance(assets_factory.git, GitController)
    assert isinstance(assets_factory.s3, S3Controller)