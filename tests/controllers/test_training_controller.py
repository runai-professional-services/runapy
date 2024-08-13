import pytest
import json
from unittest.mock import Mock

from runai import controllers
from runai import errors
from runai.client import RunaiClient


@pytest.fixture
def mock_workload_response() -> dict:
    return {
        "actualPhase": "Creating",
        "clusterId": "461619fd-127a-4cc6-979c-5cd843a37a2d",
        "createdAt": "2024-08-13T14:11:34.054Z",
        "createdBy": "API",
        "departmentId": "8020",
        "desiredPhase": "Running",
        "name": "training-test5",
        "projectId": "47292",
        "requestedName": "training-test5",
        "spec": {
            "backoffLimit": 6,
            "compute": {
                "cpuCoreRequest": 0.2,
                "cpuMemoryRequest": "200M",
                "gpuDevicesRequest": 2,
            },
            "environmentVariables": [{"exclude": False, "name": "LOG_DIR", "value": "./"}],
            "exposedUrls": [
                {"container": 8888, "toolName": "Jupyter", "toolType": "jupyter-notebook"},
                {"container": 6006, "toolName": "TensorBoard", "toolType": "tensorboard"},
            ],
            "image": "gcr.io/run-ai-demo/jupyter-tensorboard",
            "imagePullPolicy": "Always",
            "labels": [{"exclude": False, "name": "MY_TRAINING_NUMBER", "value": "10241"}],
            "nodePools": ["default"],
            "priorityClass": "train",
        },
        "workloadId": "fbe92d5c-1854-4e68-ae4d-c86e958e84dc",
    }


class TestTrainingController:
    @pytest.fixture
    def mock_client(self):
        client = Mock(RunaiClient)
        client.cluster_id = "461619fd-127a-4cc6-979c-5cd843a37a2d"
        return client

    @pytest.fixture
    def controller(self, mock_client):
        return controllers.TrainingController(mock_client)

    def test_init(self, mock_client):
        controller = controllers.TrainingController(mock_client)
        assert controller.client == mock_client

    def test_create(self, controller):
        controller.client.post.return_value = mock_workload_response
        training_name = "training-test5"
        use_given_name_as_prefix = False
        project_id = "47292"
        cluster_id = controller.client.cluster_id
        spec = {
            "command": None,
            "args": None,
            "image": "gcr.io/run-ai-demo/jupyter-tensorboard",
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
                "extendedResources": None
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": ["default"],
            "podAffinity": None,
            "environmentVariables": [{"name": "LOG_DIR", "value": "./","exclude":False}],
            "annotations": None,
            "labels": [
                {
                    "name": "MY_TRAINING_NUMBER",
                    "value": "10241",
                    "exclude": False
                }
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
                    "url": None
                },
                {
                    "container": 6006,
                    "toolType": "tensorboard",
                    "toolName": "TensorBoard",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None
                }
            ],
            "relatedUrls": None,
            "storage": None,
            "security": None,
            "completions": None,
            "parallelism": None,
            "priorityClass": "train",
        }

        expected_body = {
            "name": training_name,
            "projectId": project_id,
            "clusterId": cluster_id,
            "useGivenNameAsPrefix": use_given_name_as_prefix,
            "spec": spec
        }
        expected_body = json.dumps(expected_body).replace(" ", "")

        result = controller.create(
            training_name=training_name,
            use_given_name_as_prefix=use_given_name_as_prefix,
            project_id=project_id,
            cluster_id=cluster_id,
            spec=spec
            )
        assert result == mock_workload_response
        controller.client.post.assert_called_once_with(
            "/api/v1/workloads/trainings", expected_body
        )
    
    def test_create_missing_image(self, controller):
        training_name = "training-test5"
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
                "extendedResources": None
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": ["default"],
            "podAffinity": None,
            "environmentVariables": [{"name": "LOG_DIR", "value": "./","exclude":False}],
            "annotations": None,
            "labels": [
                {
                    "name": "MY_TRAINING_NUMBER",
                    "value": "10241",
                    "exclude": False
                }
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
                    "url": None
                },
                {
                    "container": 6006,
                    "toolType": "tensorboard",
                    "toolName": "TensorBoard",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None
                }
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
                training_name=training_name,
                use_given_name_as_prefix=use_given_name_as_prefix,
                project_id=project_id,
                cluster_id=cluster_id,
                spec=spec
                )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

    def test_create_wrong_priority_class(self, controller):
        training_name = "training-test5"
        use_given_name_as_prefix = False
        project_id = "47292"
        cluster_id = controller.client.cluster_id
        priority_class = "noexist"
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
                "extendedResources": None
            },
            "workingDir": None,
            "createHomeDir": None,
            "probes": None,
            "nodeType": None,
            "nodePools": ["default"],
            "podAffinity": None,
            "environmentVariables": [{"name": "LOG_DIR", "value": "./","exclude":False}],
            "annotations": None,
            "labels": [
                {
                    "name": "MY_TRAINING_NUMBER",
                    "value": "10241",
                    "exclude": False
                }
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
                    "url": None
                },
                {
                    "container": 6006,
                    "toolType": "tensorboard",
                    "toolName": "TensorBoard",
                    "authorizedUsers": None,
                    "authorizedGroups": None,
                    "name": None,
                    "url": None
                }
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
                training_name=training_name,
                use_given_name_as_prefix=use_given_name_as_prefix,
                project_id=project_id,
                cluster_id=cluster_id,
                spec=spec
                )
        assert "Failed to build body scheme" in str(exc_info)
        controller.client.post.assert_not_called()

