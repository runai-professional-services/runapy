from unittest.mock import Mock

import pytest

from runai import assets
from runai import errors


@pytest.fixture
def mock_client():
    client = Mock()
    return client


def test_assets_controller_update_not_implemented(mock_client):
    controller = assets.AssetsController(mock_client)
    with pytest.raises(errors.RunaiNotImplementedError):
        controller.update()


def test_pvc_create(mock_client):
    pvc_controller = assets.PVCController(mock_client)
    api_path = "/api/v1/asset/datasource/pvc"

    pvc_controller.create(
        name="test-pvc",
        scope="tenant",
        spec={
            "path": "/container/my-claim",
            "existingPvc": False,
            "claimName": "my-claim",
            "readOnly": False,
            "ephemeral": False,
            "claimInfo": {
                "size": "1G",
                "storageClass": "my-storage-class",
                "accessModes": {
                    "readWriteOnce": True,
                    "readOnlyMany": False,
                    "readWriteMany": False,
                },
                "volumeMode": "Filesystem",
            },
        }
    )
    pvc_controller.client.post.assert_called_once_with(
        api_path,
        '{"meta":{"name":"test-pvc","scope":"tenant","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"path":"/container/my-claim","claimName":"my-claim","claimInfo":{"size":"1G","storageClass":"my-storage-class","accessModes":{"readWriteOnce":true,"readOnlyMany":false,"readWriteMany":false},"volumeMode":"Filesystem"},"existingPvc":false,"readOnly":false,"ephemeral":false}}'
    )


def test_s3_create(mock_client):
    s3_controller = assets.S3Controller(mock_client)
    api_path = "/api/v1/asset/datasource/s3"

    s3_controller.create(
        name="test-s3",
        scope="tenant",
        spec={"bucket": "bucket",
              "url": "https://bucket.s3.us-east-1.amazonaws.com",
              "path": "/home/jovyan/work",
              "accessKeyAssetId": "6bb6cdf4-08e7-4df0-abe7-d8400bc891b2"
              }

    )
    s3_controller.client.post.assert_called_once_with(
        api_path,
        '{"meta":{"name":"test-s3","scope":"tenant","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"bucket":"bucket","path":"/home/jovyan/work","url":"https://bucket.s3.us-east-1.amazonaws.com","accessKeyAssetId":"6bb6cdf4-08e7-4df0-abe7-d8400bc891b2"}}'
    )


def test_git_create(mock_client):
    git_controller = assets.GitController(mock_client)
    api_path = "/api/v1/asset/datasource/git"

    git_controller.create(
        name="test-git",
        scope="tenant",
        path="/app",
        repository="https://github.com/user/repo",
        password_asset_id="ca484ab7-5555-41d8-8ddc-f4a4de2b6d91"
    )
    git_controller.client.post.assert_called_once_with(
        api_path,
        '{"meta":{"name":"test-git","scope":"tenant","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"path":"/app","repository":"https://github.com/user/repo","passwordAssetId":"ca484ab7-5555-41d8-8ddc-f4a4de2b6d91","branch":null,"revision":null}}'
    )


def test_nfs_create(mock_client):
    nfs_controller = assets.NFSController(mock_client)
    api_path = "/api/v1/asset/datasource/nfs"

    nfs_controller.create(
        name="test-nfs",
        scope="tenant",
        path="/mnt/nfs",
        server="192.168.1.1",
        mount_path="/container/path"
    )
    nfs_controller.client.post.assert_called_once_with(
        api_path,
        '{"meta":{"name":"test-nfs","scope":"tenant","workloadSupportedTypes":null,"description":null,"clusterId":null,"departmentId":null,"projectId":null,"autoDelete":false},"spec":{"path":"/mnt/nfs","readOnly":true,"server":"192.168.1.1","mountPath":"/container/path"}}'
    )