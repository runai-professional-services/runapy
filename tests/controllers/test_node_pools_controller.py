import pytest
import json
from unittest.mock import Mock, patch

from runai import models
from runai import controllers
from runai import errors
from runai.client import RunaiClient


class TestNodePoolController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.NodePoolController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.NodePoolController(mock_client)
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
            controllers.NodePoolController(client)
        assert "cluster_id is not configured" in str(exc_info)

    def test_all(self, controller):
        mock_response = [{"id": 1, "name": "pool1"}, {"id": 2, "name": "pool2"}]

        controller.client.get.return_value = mock_response

        result = controller.all()

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            f"/v1/k8s/clusters/{controller.client.cluster_id}/node-pools"
        )

    def test_get_by_name(self, controller):
        mock_response = [{"id": 1, "name": "pool1"}, {"id": 2, "name": "pool2"}]
        controller.client.get.return_value = mock_response

        result = controller.get_by_name("pool2")

        assert result == {"id": 2, "name": "pool2"}
        controller.client.get.assert_called_once_with(
            f"/v1/k8s/clusters/{controller.client.cluster_id}/node-pools"
        )

    def test_node_pool_metrics(self, controller):
        cluster_id = controller.client.cluster_id
        node_pool_name = "pool1"
        query_params = {
            "nodepool_name": node_pool_name,
            "start": "2023-01-01",
            "end": "2023-01-02",
            "metric_type": "GPU_UTILIZATION",
        }

        controller.node_pool_metrics(**query_params)

        expected_query_model = models.NodePoolsQueryParams(
            **query_params, metricType=query_params["metric_type"]
        )

        controller.client.get.assert_called_once_with(
            f"/api/v1/clusters/{cluster_id}/nodepools/{node_pool_name}/metrics",
            expected_query_model,
        )

    def test_node_pool_metrics_bad_parameter(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.node_pool_metrics("pool1", 5, "2023-01-02", "GPU_UTILIZATION")
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()
    
    def test_node_pool_metrics_bad_metric_type(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.node_pool_metrics("pool1", "2023-01-01", "2023-01-02", "POD_UTILIZATION")
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_create(self, controller):
        cluster_id = controller.client.cluster_id
        nodepool_name = "new_pool"
        label_key = "key"
        label_value = "value"
        placement_strategy = {"cpu": "spread", "gpu": "spread"}
        over_provisioning_ratio = 1

        expected_payload = {"name": nodepool_name, "labelKey": label_key, "labelValue": label_value, "placementStrategy": placement_strategy, "overProvisioningRatio": over_provisioning_ratio}
        # Trim spaces to match actual json string payload
        expected_payload = json.dumps(expected_payload).replace(" ", "")

        controller.create(
            name=nodepool_name,
            label_key=label_key,
            label_value=label_value,
            placement_strategy=placement_strategy,
            over_provisioning_ratio=over_provisioning_ratio,
        )

        controller.client.post.assert_called_once_with(
            f"/v1/k8s/clusters/{cluster_id}/node-pools",
            expected_payload
        )

    def test_create_missing_required_field(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(
                name="new_pool",
                label_key=None,
                label_value="value",
                placement_strategy={"cpu": "spread", "gpu": "NONE"},
                over_provisioning_ratio=1,
            )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_update(self, controller):
        mock_response = {"id": 1, "name": "updated_pool"}
        controller.client.put.return_value = mock_response

        result = controller.update(
            nodepool_id=1,
            labelKey="new_key",
            labelValue="new_value",
            placementStrategy={"cpu": "binpack", "gpu": "spread"},
            overProvisioningRatio=2,
        )

        assert result == mock_response
        controller.client.put.assert_called_once()

    def test_update_bad_parameters(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update(
                nodepool_id=1,
                labelKey="new_key",
                labelValue="new_value",
                placementStrategy={"cpu": "binpack", "gpu": "NONE"},
                overProvisioningRatio=2,
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_update_labels(self, controller):
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.put.return_value = mock_response

        result = controller.update_labels(
            nodepool_id=1, label_key="new_key", label_value="new_value"
        )

        assert result == mock_response
        controller.client.put.assert_called_once()

    def test_update_labels_bad_parameter(self, controller):

        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.update_labels(
                nodepool_id=1, label_key="new_key", label_value=None
            )

        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_delete(self, controller):
        node_pool_id = 1
        mock_response = {"status code": 202, "message": "Accepted"}
        controller.client.delete.return_value = mock_response

        result = controller.delete(nodepool_id=node_pool_id)

        assert result == mock_response
        controller.client.delete.assert_called_once_with(
            f"/v1/k8s/clusters/{controller.client.cluster_id}/node-pools/{node_pool_id}"
        )
