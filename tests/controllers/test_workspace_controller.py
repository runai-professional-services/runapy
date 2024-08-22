import pytest
import json
from unittest.mock import Mock, patch

from runai import controllers
from runai import errors
from runai.client import RunaiClient


@pytest.fixture
def mock_workload_response() -> dict:
    return {
        "actualPhase": "Creating",
        "clusterId": "461619fd-127a-4cc6-979c-5cd843a37a2d",
        "createdAt": "2024-08-13T14:55:14.358Z",
        "createdBy": "API",
        "departmentId": "8020",
        "desiredPhase": "Running",
        "name": "workspace-test5",
        "projectId": "47292",
        "requestedName": "workspace-test5",
        "spec": {
            "args": "--NotebookApp.base_url=/${RUNAI_PROJECT}/${RUNAI_JOB_NAME} --NotebookApp.token=''",
            "backoffLimit": 6,
            "command": "start-notebook.sh",
            "compute": {
                "gpuDevicesRequest": 1,
                "gpuPortionRequest": 0.5,
                "gpuRequestType": "portion",
            },
            "exposedUrls": [
                {
                    "container": 8888,
                    "toolName": "Jupyter",
                    "toolType": "jupyter-notebook",
                }
            ],
            "image": "gcr.io/run-ai-demo/jupyter-demo",
            "imagePullPolicy": "Always",
            "nodePools": ["default"],
            "priorityClass": "build",
            "security": {
                "hostIpc": False,
                "hostNetwork": False,
                "seccompProfileType": "RuntimeDefault",
            },
        },
        "workloadId": "8e11a5e3-3184-4cfb-8f3c-51a688c0307a",
    }


class TestWorkspaceController:
    @pytest.fixture
    def mock_client(self):
        client = Mock(RunaiClient)
        client.cluster_id = "461619fd-127a-4cc6-979c-5cd843a37a2d"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.WorkspaceController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.WorkspaceController(mock_client)
        assert controller.client == mock_client

    def test_init_missing_cluster_id(self):
        with patch.object(RunaiClient, "_generate_api_token"):
            client = RunaiClient(
                realm="test-realm",
                client_id="api-client",
                client_secret="test-client-secret",
                runai_base_url="https://test.runai.ai"
            )
        with pytest.raises(errors.RunaiClusterIDNotConfigured) as exc_info:
            controllers.WorkspaceController(client)
        assert "cluster_id is not configured" in str(exc_info)

    def test_create(self, controller):
        controller.client.post.return_value = mock_workload_response
        workspace_name = "workspace-test5"
        use_given_name_as_prefix = False
        project_id = "47292"
        cluster_id = controller.client.cluster_id
        spec = {
            "command": "start-notebook.sh",
            "args": "--NotebookApp.base_url=/${RUNAI_PROJECT}/${RUNAI_JOB_NAME}--NotebookApp.token=''",
            "image": "gcr.io/run-ai-demo/jupyter-demo",
            "imagePullPolicy": "Always",
            "compute": {
                "gpuDevicesRequest": 1,
                "gpuRequestType": "portion",
                "gpuPortionRequest": 0.5,
                "gpuPortionLimit": None,
                "gpuMemoryRequest": None,
                "gpuMemoryLimit": None,
                "migProfile": None,
                "cpuCoreRequest": None,
                "cpuCoreLimit": None,
                "cpuMemoryRequest": None,
                "cpuMemoryLimit": None,
                "largeShmRequest": None,
                "extendedResources": None
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": [
                "default"
            ],
            "podAffinity": None,
            "environmentVariables": None,
            "annotations": None,
            "labels": None,
            "tolerations": None,
            "terminateAfterPreemption": None,
            "autoDeletionTimeAfterCompletionSeconds": None,
            "backoffLimit": 6,
            "ports": None,
            "exposedUrls": [
                {
                    "container": 8888,
                    "toolType": "jupyter-notebook",
                    "toolName": "Jupyter",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None
                }
            ],
            "relatedUrls": None,
            "storage": None,
            "security": {
                "uidGidSource": None,
                "capabilities": None,
                "seccompProfileType": "RuntimeDefault",
                "runAsNonRoot": None,
                "readOnlyRootFilesystem": None,
                "runAsUid": None,
                "runAsGid": None,
                "supplementalGroups": None,
                "allowPrivilegeEscalation": None,
                "hostIpc": False,
                "hostNetwork": False
            },
            "priorityClass": "build"
        }

        expected_body = {
            "name": workspace_name,
            "projectId": project_id,
            "clusterId": cluster_id,
            "useGivenNameAsPrefix": use_given_name_as_prefix,
            "spec": spec,
        }
        expected_body = json.dumps(expected_body).replace(" ", "")

        result = controller.create(
            workspace_name=workspace_name,
            use_given_name_as_prefix=use_given_name_as_prefix,
            project_id=project_id,
            cluster_id=cluster_id,
            spec=spec,
        )
        assert result == mock_workload_response
        controller.client.post.assert_called_once_with(
            "/api/v1/workloads/workspaces", expected_body
        )

    def test_create_missing_image(self, controller):
        workspace_name = "workspace-test5"
        use_given_name_as_prefix = False
        project_id = "47292"
        cluster_id = controller.client.cluster_id
        spec = {
            "command": None,
            "args": None,
            "image": None,
            "imagePullPolicy": "Always",
            "compute": {
                "gpuDevicesRequest": 2,
                "gpuRequestType": None,
                "gpuPortionRequest": None,
                "gpuPortionLimit": None,
                "gpuMemoryRequest": None,
                "gpuMemoryLimit": None,
                "migProfile": None,
                "cpuCoreRequest": 0.2,
                "cpuCoreLimit": None,
                "cpuMemoryRequest": "200M",
                "cpuMemoryLimit": None,
                "largeShmRequest": None,
                "extendedResources": None,
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": ["default"],
            "podAffinity": None,
            "environmentVariables": [
                {"name": "LOG_DIR", "value": "./", "exclude": False}
            ],
            "annotations": None,
            "labels": [
                {"name": "MY_workspace_NUMBER", "value": "10241", "exclude": False}
            ],
            "tolerations": None,
            "terminateAfterPreemption": None,
            "autoDeletionTimeAfterCompletionSeconds": None,
            "backoffLimit": 6,
            "ports": None,
            "exposedUrls": [
                {
                    "container": 8888,
                    "toolType": "jupyter-notebook",
                    "toolName": "Jupyter",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None,
                },
                {
                    "container": 6006,
                    "toolType": "tensorboard",
                    "toolName": "TensorBoard",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None,
                },
            ],
            "relatedUrls": None,
            "storage": None,
            "security": None,
            "completions": None,
            "parallelism": None,
            "priorityClass": "train",
        }

        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(
                workspace_name=workspace_name,
                use_given_name_as_prefix=use_given_name_as_prefix,
                project_id=project_id,
                cluster_id=cluster_id,
                spec=spec,
            )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_create_wrong_priority_class(self, controller):
        workspace_name = "workspace-test5"
        use_given_name_as_prefix = False
        project_id = "47292"
        cluster_id = controller.client.cluster_id
        priority_class = "train"
        spec = {
            "command": None,
            "args": None,
            "image": "ubuntu",
            "imagePullPolicy": "Always",
            "compute": {
                "gpuDevicesRequest": 2,
                "gpuRequestType": None,
                "gpuPortionRequest": None,
                "gpuPortionLimit": None,
                "gpuMemoryRequest": None,
                "gpuMemoryLimit": None,
                "migProfile": None,
                "cpuCoreRequest": 0.2,
                "cpuCoreLimit": None,
                "cpuMemoryRequest": "200M",
                "cpuMemoryLimit": None,
                "largeShmRequest": None,
                "extendedResources": None,
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": ["default"],
            "podAffinity": None,
            "environmentVariables": [
                {"name": "LOG_DIR", "value": "./", "exclude": False}
            ],
            "annotations": None,
            "labels": [
                {"name": "MY_workspace_NUMBER", "value": "10241", "exclude": False}
            ],
            "tolerations": None,
            "terminateAfterPreemption": None,
            "autoDeletionTimeAfterCompletionSeconds": None,
            "backoffLimit": 6,
            "ports": None,
            "exposedUrls": [
                {
                    "container": 8888,
                    "toolType": "jupyter-notebook",
                    "toolName": "Jupyter",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None,
                },
                {
                    "container": 6006,
                    "toolType": "tensorboard",
                    "toolName": "TensorBoard",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None,
                },
            ],
            "relatedUrls": None,
            "storage": None,
            "security": None,
            "completions": None,
            "parallelism": None,
            "priorityClass": priority_class,
        }

        with pytest.raises(errors.RunaiBuildModelError) as exc_info:
            controller.create(
                workspace_name=workspace_name,
                use_given_name_as_prefix=use_given_name_as_prefix,
                project_id=project_id,
                cluster_id=cluster_id,
                spec=spec,
            )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()
