# coding: utf-8

"""
Test file for PolicyApi
Generated by OpenAPI Generator with custom template
"""

import pytest
import unittest.mock as mock
from datetime import datetime, timezone
import json

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.models import *
from runai.exceptions import ApiException


class TestPolicyApi:
    """Test cases for PolicyApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = PolicyApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_delete_distributed_policy(self):
        """Test case for delete_distributed_policy

        Delete a distributed policy. Use to delete a distributed policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        self.api.delete_distributed_policy(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v2/policy/distributed" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

    def test_delete_distributed_policy_error(self):
        """Test error handling for delete_distributed_policy"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_distributed_policy(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_delete_inference_policy(self):
        """Test case for delete_inference_policy

        Delete an inference policy. Use to delete an inference policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        self.api.delete_inference_policy(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v2/policy/inferences" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

    def test_delete_inference_policy_error(self):
        """Test error handling for delete_inference_policy"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_inference_policy(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_delete_training_policy(self):
        """Test case for delete_training_policy

        Delete a training policy. Use to delete a training policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        self.api.delete_training_policy(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v2/policy/trainings" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

    def test_delete_training_policy_error(self):
        """Test error handling for delete_training_policy"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_training_policy(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_delete_workspace_policy(self):
        """Test case for delete_workspace_policy

        Delete a workspace policy. Use to delete a workspace policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        self.api.delete_workspace_policy(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v2/policy/workspaces" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

    def test_delete_workspace_policy_error(self):
        """Test error handling for delete_workspace_policy"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_workspace_policy(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_get_distributed_policy_v2(self):
        """Test case for get_distributed_policy_v2

        Get a distributed policy. Retrieve the details of a distributed policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        response = self.api.get_distributed_policy_v2(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v2/policy/distributed" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

        # Verify response
        assert isinstance(response, DistributedPolicyV2)

    def test_get_distributed_policy_v2_error(self):
        """Test error handling for get_distributed_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_distributed_policy_v2(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_get_inference_policy_v2(self):
        """Test case for get_inference_policy_v2

        Get an inference policy. Retrieve the details of an inference policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        response = self.api.get_inference_policy_v2(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v2/policy/inferences" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

        # Verify response
        assert isinstance(response, InferencePolicyV2)

    def test_get_inference_policy_v2_error(self):
        """Test error handling for get_inference_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_inference_policy_v2(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_get_training_policy_v2(self):
        """Test case for get_training_policy_v2

        Get a training policy. Retrieve the details of an training policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        response = self.api.get_training_policy_v2(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v2/policy/trainings" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

        # Verify response
        assert isinstance(response, TrainingPolicyV2)

    def test_get_training_policy_v2_error(self):
        """Test error handling for get_training_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_training_policy_v2(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_get_workspace_policy_v2(self):
        """Test case for get_workspace_policy_v2

        Get a workspace policy. Retrieve the details of a workspace policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"  # str | The scope that the policy relates to.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.

        # Make request
        response = self.api.get_workspace_policy_v2(
            scope=scope,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v2/policy/workspaces" in kwargs["url"]

        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]

        # Verify response
        assert isinstance(response, WorkspacePolicyV2)

    def test_get_workspace_policy_v2_error(self):
        """Test error handling for get_workspace_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        scope = "scope_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_workspace_policy_v2(
                scope=scope,
            )
        assert exc_info.value.status == 400

    def test_list_policies(self):
        """Test case for list_policies

        List policies Retrieve a list of all the applied policies.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_type = (
            "workload_type_example"  # str | Policy for a specific workload type.
        )
        scope = "scope_example"  # str | filter by this scope.
        department_id = "1"  # str | Filter using the department id.
        project_id = "1"  # str | project id to filter by
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.
        include_fallback_policies = True  # bool | whether to include fallback policies in the list. Default to false.

        # Make request
        response = self.api.list_policies()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v2/policy" in kwargs["url"]

        # Verify query parameters
        assert "workloadType=" in kwargs["url"]
        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]
        # Verify query parameters
        assert "includeFallbackPolicies=" in kwargs["url"]

        # Verify response
        assert isinstance(response, PolicyListResponse)

    def test_list_policies_error(self):
        """Test error handling for list_policies"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.list_policies()
        assert exc_info.value.status == 400

    def test_overwrite_distributed_policy_v2(self):
        """Test case for overwrite_distributed_policy_v2

        Overwrite a distributed policy. Use to apply a distributed policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        distributed_policy_overwrite_request_v2 = (
            runai.DistributedPolicyOverwriteRequestV2()
        )  # DistributedPolicyOverwriteRequestV2 |

        # Make request
        response = self.api.overwrite_distributed_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v2/policy/distributed" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, DistributedPolicyV2)

    def test_overwrite_distributed_policy_v2_error(self):
        """Test error handling for overwrite_distributed_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.overwrite_distributed_policy_v2()
        assert exc_info.value.status == 400

    def test_overwrite_inference_policy_v2(self):
        """Test case for overwrite_inference_policy_v2

        Overwrite an inference policy. Use to apply an inference policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        inference_policy_overwrite_request_v2 = (
            runai.InferencePolicyOverwriteRequestV2()
        )  # InferencePolicyOverwriteRequestV2 |

        # Make request
        response = self.api.overwrite_inference_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v2/policy/inferences" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, InferencePolicyV2)

    def test_overwrite_inference_policy_v2_error(self):
        """Test error handling for overwrite_inference_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.overwrite_inference_policy_v2()
        assert exc_info.value.status == 400

    def test_overwrite_training_policy_v2(self):
        """Test case for overwrite_training_policy_v2

        Overwrite a training policy. Use to apply a training policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        training_policy_overwrite_request_v2 = (
            runai.TrainingPolicyOverwriteRequestV2()
        )  # TrainingPolicyOverwriteRequestV2 |

        # Make request
        response = self.api.overwrite_training_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v2/policy/trainings" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, TrainingPolicyV2)

    def test_overwrite_training_policy_v2_error(self):
        """Test error handling for overwrite_training_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.overwrite_training_policy_v2()
        assert exc_info.value.status == 400

    def test_overwrite_workspace_policy_v2(self):
        """Test case for overwrite_workspace_policy_v2

        Overwrite a workspace policy. Ue to apply a workspace policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        workspace_policy_overwrite_request_v2 = (
            runai.WorkspacePolicyOverwriteRequestV2()
        )  # WorkspacePolicyOverwriteRequestV2 |

        # Make request
        response = self.api.overwrite_workspace_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v2/policy/workspaces" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, WorkspacePolicyV2)

    def test_overwrite_workspace_policy_v2_error(self):
        """Test error handling for overwrite_workspace_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.overwrite_workspace_policy_v2()
        assert exc_info.value.status == 400

    def test_update_distributed_policy_v2(self):
        """Test case for update_distributed_policy_v2

        Update a distributed policy. Use to apply changes to distributed policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        distributed_policy_change_request_v2 = (
            runai.DistributedPolicyChangeRequestV2()
        )  # DistributedPolicyChangeRequestV2 |

        # Make request
        response = self.api.update_distributed_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v2/policy/distributed" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, DistributedPolicyV2)

    def test_update_distributed_policy_v2_error(self):
        """Test error handling for update_distributed_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_distributed_policy_v2()
        assert exc_info.value.status == 400

    def test_update_inference_policy_v2(self):
        """Test case for update_inference_policy_v2

        Update an inference policy. Use to apply changes to inference policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        inference_policy_change_request_v2 = (
            runai.InferencePolicyChangeRequestV2()
        )  # InferencePolicyChangeRequestV2 |

        # Make request
        response = self.api.update_inference_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v2/policy/inferences" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, InferencePolicyV2)

    def test_update_inference_policy_v2_error(self):
        """Test error handling for update_inference_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_inference_policy_v2()
        assert exc_info.value.status == 400

    def test_update_training_policy_v2(self):
        """Test case for update_training_policy_v2

        Update a training policy. Use to apply changes to training policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        training_policy_change_request_v2 = (
            runai.TrainingPolicyChangeRequestV2()
        )  # TrainingPolicyChangeRequestV2 |

        # Make request
        response = self.api.update_training_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v2/policy/trainings" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, TrainingPolicyV2)

    def test_update_training_policy_v2_error(self):
        """Test error handling for update_training_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_training_policy_v2()
        assert exc_info.value.status == 400

    def test_update_workspace_policy_v2(self):
        """Test case for update_workspace_policy_v2

        Update a workspace policy. Use to apply changes to workspace policy for a given organizational unit.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        validate_only = (
            True  # bool | Validate the given policy payload without applying it
        )
        workspace_policy_change_request_v2 = (
            runai.WorkspacePolicyChangeRequestV2()
        )  # WorkspacePolicyChangeRequestV2 |

        # Make request
        response = self.api.update_workspace_policy_v2()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v2/policy/workspaces" in kwargs["url"]

        # Verify query parameters
        assert "validateOnly=" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, WorkspacePolicyV2)

    def test_update_workspace_policy_v2_error(self):
        """Test error handling for update_workspace_policy_v2"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_workspace_policy_v2()
        assert exc_info.value.status == 400
