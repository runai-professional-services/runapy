import pytest
from unittest.mock import Mock

from runai import models
from runai import errors
from runai import controllers


class TestWorkloadsController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.WorkloadsController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.WorkloadsController(mock_client)
        assert controller.client == mock_client

    def test_all(self, controller):
        deleted = True
        limit = 5
        offset = 5
        sort_by = "type"
        sort_order = "asc"

        controller.all(
            deleted=deleted,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order
        )

        params = {
            "deleted": deleted,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "sortOrder": sort_order

        }

        controller.client.get.assert_called_once_with(
            "/api/v1/workloads",
            models.WorkloadsGetAllQueryParams(**params),
        )

    def test_all_wrong_params(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.all(
                deleted=True, filter_by="name==workload1", sort_by=5, sort_order="NONE", limit="1"
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_count_workloads(self, controller):
        deleted = True
        controller.count_workloads(
            deleted=deleted
        )

        params = {
            "deleted": deleted
        }

        controller.client.get.assert_called_once_with(
            "/api/v1/workloads/count",
            models.WorkloadsCountQueryParams(**params)
        )

    def test_count_workloads_wrong_params(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.count_workloads(
                deleted=True, filter_by=5
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_get_workloads_telemetry(self, controller):
        telemetry_type = "WORKLOADS_COUNT"
        group_by = "ClusterId"

        controller.get_workloads_telemetry(
            telemetry_type=telemetry_type,
            group_by=group_by
        )

        params = {
            "telemetryType": telemetry_type,
            "groupBy": group_by
        }

        controller.client.get.assert_called_once_with(
            "/api/v1/workloads/telemetry",
            models.WorkloadsTelemetryQueryParams(**params)
        )

    def test_get_workloads_telemetry_wrong_params(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.get_workloads_telemetry(
                telemetry_type="DONT_EXISTS"
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_get_workloads_metrics(self, controller):
        workload_id = "ce254bb8-5a7a-401b-b8bf-2b009c861c31"
        start = "2023-06-06T12:09:18.211Z"
        end = "2025-06-06T12:09:18.211Z"
        metric_type = ["GPU_MEMORY_REQUEST_BYTES"]

        controller.get_workload_metrics(
            workload_id=workload_id,
            start=start,
            end=end,
            metric_type=metric_type
        )

        params = {
            "workloadId": workload_id,
            "start": start,
            "end": end,
            "metricType": metric_type,
        }

        controller.client.get.assert_called_once_with(
            f"/api/v1/workloads/{workload_id}/metrics",
            models.WorkloadMetricsQueryParams(**params)
        )

    def test_get_workloads_metrics_wrong_params(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.get_workloads_telemetry(
                telemetry_type="DONT_EXISTS"
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()
