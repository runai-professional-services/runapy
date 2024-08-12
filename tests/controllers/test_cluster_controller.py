import pytest
from unittest.mock import Mock

from runai import models
from runai import errors
from runai import controllers


class TestClusterController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.ClusterController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.ClusterController(mock_client)
        assert controller.client == mock_client

    def test_all(self, controller):
        mock_response = [{"name": "cluster1", "uuid":"71f69d83-ba66-4822-adf8-55ce55efd219"},
                         {"name": "cluster2", "uuid":"52f13d82-ba66-4822-adf8-55ce55efd332"}]
        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            '/api/v1/clusters?verbosity=full',
            params=models.ClusterQueryParams(verbosity='full')
        )
    
    def test_all_metadata_verbosity(self, controller):
        mock_response = [{"name": "cluster1", "uuid":"71f69d83-ba66-4822-adf8-55ce55efd219"},
                         {"name": "cluster2", "uuid":"52f13d82-ba66-4822-adf8-55ce55efd332"}]
        controller.client.get.return_value = mock_response

        result = controller.all(verbosity='metadata')

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            '/api/v1/clusters?verbosity=metadata',
            params=models.ClusterQueryParams(verbosity='metadata')
        )

    def test_all_wrong_verbosity_value(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.all(verbosity='noexist')

        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_get(self, controller):
        cluster_id = controller.client.cluster_id
        mock_response = {"uuid": cluster_id, "name": "cluster1"}
        controller.client.get.return_value = mock_response

        result = controller.get(cluster_id=cluster_id)

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            f'/api/v1/clusters/{cluster_id}',
            params=models.ClusterQueryParams(verbosity='full')
        )

    def test_get_metadata_verbosity(self, controller):
        cluster_id = controller.client.cluster_id
        mock_response = {"uuid": cluster_id, "name": "cluster1"}
        controller.client.get.return_value = mock_response

        result = controller.get(cluster_id=cluster_id,
                                verbosity='metadata')

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            f"/api/v1/clusters/{cluster_id}",
            params=models.ClusterQueryParams(verbosity='metadata'))

    def test_get_wrong_verbosity_value(self, controller):
        cluster_id = controller.client.cluster_id

        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.get(cluster_id=cluster_id,
                           verbosity='noexist')

        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()
