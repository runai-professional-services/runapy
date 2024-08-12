import pytest
import json
from unittest.mock import Mock

from runai import controllers
from runai import models
from runai import errors


class TestAccessRulesController:
    @pytest.fixture
    def mock_client(self):
        client = Mock()
        client.cluster_id = "71f69d83-ba66-4822-adf8-55ce55efd219"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.AccessRulesController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.AccessRulesController(mock_client)
        assert controller.client == mock_client

    def test_all_with_query_params(self, controller):
        mock_response = {
            "totalRecords": 1,
            "displayRecord": 1,
            "accessRules": [
                {
                    "subjectId": "ofir@run.ai",
                    "subjectType": "user",
                    "roleId": 4,
                    "scopeId": "212",
                    "scopeType": "tenant",
                    "roleName": "Research manager",
                    "scopeName": "envinaclick",
                    "id": 18956,
                    "createdAt": "2023-10-01T06:16:36.805641Z",
                    "updatedAt": "2023-10-01T06:16:36.805641Z",
                    "tenantId": 212,
                    "createdBy": "",
                }
            ],
        }
        controller.client.get.return_value = mock_response

        result = controller.all(
            filterBy="name==project1", sortBy="subjectType", sortOrder="asc", limit=1
        )

        assert result == mock_response
        controller.client.get.assert_called_once_with(
            "/api/v1/authorization/access-rules",
            params=models.AccessRulesQueryParams(
                filterBy="name==project1",
                sortBy="subjectType",
                sortOrder="asc",
                limit=1,
            ),
        )

    def test_all_wrong_filter(self, controller):
        with pytest.raises(errors.RunaiQueryParamsError) as exc_info:
            controller.all(
                filterBy="name==project1", sortBy="WRONG", sortOrder="asc", limit=1
            )
        assert "Failed to build query parameters" in str(exc_info)
        controller.client.get.assert_not_called()

    def test_create(self, controller):
        mock_response = {
            "subjectId": "ofir.eldar@run.ai",
            "subjectType": "user",
            "roleId": 5,
            "scopeId": "71f69d83-ba66-4822-adf8-55ce55efd219",
            "scopeType": "cluster",
            "clusterId": "71f69d83-ba66-4822-adf8-55ce55efd219",
        }
        controller.client.post.return_value = mock_response

        subject_id = "ofir.eldar@run.ai"
        subject_type = "user"
        role_id = 5
        scope_id = controller.client.cluster_id
        scope_type = "cluster"

        expected_body = {
            "subjectId": subject_id,
            "subjectType": subject_type,
            "roleId": role_id,
            "scopeId": scope_id,
            "scopeType": scope_type,
            "clusterId": controller.client.cluster_id,
        }

        expected_body = json.dumps(expected_body).replace(" ", "")

        controller.create(
            subject_id=subject_id,
            subject_type=subject_type,
            role_id=role_id,
            scope_id=scope_id,
            scope_type=scope_type,
        )

        controller.client.post.assert_called_once_with(
            "/api/v1/authorization/access-rules", expected_body
        )

    def test_create_wrong_subject_type(self, controller):
        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(
                subject_id="ofir.eldar@run.ai",
                subject_type="wrong",
                role_id=5,
                scope_id=controller.client.cluster_id,
                scope_type="cluster",
            )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.create.assert_not_called()
