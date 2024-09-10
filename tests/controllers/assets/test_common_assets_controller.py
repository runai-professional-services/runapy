from unittest.mock import Mock

import pytest

from runai import errors
from runai.assets import CommonAssetsController


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def common_assets_controller(mock_client):
    controller = CommonAssetsController(mock_client)
    controller.path =  "/api/v1/asset"
    return controller


def test_get(common_assets_controller):
    common_assets_controller.get("123")
    common_assets_controller.client.get.assert_called_once_with("/api/v1/asset/123")


def test_delete(common_assets_controller):
    common_assets_controller.delete("123")
    common_assets_controller.client.delete.assert_called_once_with("/api/v1/asset/123")


def test_update(common_assets_controller):
    with pytest.raises(errors.RunaiNotImplementedError) as exc_info:
        common_assets_controller.update()
    assert "Class method not implemented. Please submit a feature request on GitHub" in str(exc_info)
    common_assets_controller.client.put.assert_not_called()
