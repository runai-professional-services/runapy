from typing import Literal, Optional

from runai import models
from runai import errors
from runai.controllers import Controller


class CommonAssetsController(Controller):
    def __init__(self, client):
        self.client = client

    def _build_meta(
        self,
        name: str,
        scope: str,
        workload_supported_types: Optional[dict],
        description: Optional[str],
        cluster_id: Optional[str],
        department_id: Optional[str],
        project_id: Optional[str],
        auto_delete: Optional[bool],
    ):
        return {
            "name": name,
            "scope": scope,
            "workloadSupportedTypes": workload_supported_types,
            "description": description,
            "clusterId": cluster_id,
            "departmentId": department_id,
            "projectId": project_id,
            "autoDelete": auto_delete,
        }

    def get(self, id: str):
        path = f"{self.path}/{id}"
        return self.client.get(path)

    def delete(self, id: str):
        path = f"{self.path}/{id}"
        return self.client.delete(path)

    def update(self):
        # Updating assets is not implemented
        raise errors.RunaiNotImplementedError


class AssetsController(CommonAssetsController):
    def __init__(self, client):
        self.client = client

    def all(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        project_id: Optional[str] = None,
        department_id: Optional[str] = None,
        cluster_id: Optional[str] = None,
        usage_info: Optional[str] = None,
        comply_to_project: Optional[int] = None,
        comply_to_workload_type: Optional[str] = None,
        status_info: Optional[bool] = None,
        asset_id: Optional[str] = None,
        comply_to_replica_type: Optional[str] = None,
    ):

        path = self.path

        params = {
            "name": name,
            "scope": scope,
            "project_id": project_id,
            "department_id": department_id,
            "clutser_id": cluster_id,
            "usage_info": usage_info,
            "comply_to_project": comply_to_project,
            "comply_to_workload_type": comply_to_workload_type,
            "status_info": status_info,
            "assets_id": asset_id,
            "comply_to_replica_type": comply_to_replica_type,
        }

        query_params = models.build_query_params(
            query_model=models.AssetsGetAllQueryParams, params=params
        )
        return self.client.get(path, query_params)


class PVCController(AssetsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/datasource/pvc"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        spec: dict,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": spec,
        }

        pvc = models.build_model(model=models.PVCCreateRequest, data=data)
        payload = pvc.model_dump_json()

        return self.client.post(self.path, payload)


class S3Controller(AssetsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/datasource/s3"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        spec: dict,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": spec,
        }

        s3 = models.build_model(model=models.S3CreateRequest, data=data)
        payload = s3.model_dump_json()

        return self.client.post(self.path, payload)


class GitController(AssetsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/datasource/git"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        repository: str,
        path: str,
        password_asset_id: str,
        branch: Optional[str] = None,
        revision: Optional[str] = None,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "repository": repository,
                "path": path,
                "passwordAssetId": password_asset_id,
                "branch": branch,
                "revision": revision,
            },
        }

        git = models.build_model(model=models.GitCreateRequest, data=data)
        payload = git.model_dump_json()

        return self.client.post(self.path, payload)


class SecretAssetController(AssetsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/secrets"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        credential_asset_id: str,
        mount_path: str,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "credentialAssetId": credential_asset_id,
                "mountPath": mount_path,
            },
        }

        git = models.build_model(model=models.SecretAssetCreateRequest, data=data)
        payload = git.model_dump_json()

        return self.client.post(self.path, payload)


class NFSController(AssetsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/datasource/nfs"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        path: str,
        mount_path: str,
        server: str,
        read_only: Optional[bool] = True,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "path": path,
                "server": server,
                "readOnly": read_only,
                "mountPath": mount_path,
            },
        }

        git = models.build_model(model=models.NFSCreateRequest, data=data)
        payload = git.model_dump_json()

        return self.client.post(self.path, payload)


class CredentialsController(CommonAssetsController):
    def __init__(self, client):
        self.client = client

    def all(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        project_id: Optional[str] = None,
        department_id: Optional[str] = None,
        cluster_id: Optional[str] = None,
        usage_info: Optional[bool] = None,
        status_info: Optional[bool] = None,
    ):

        path = self.path

        params = {
            "name": name,
            "scope": scope,
            "project_id": project_id,
            "department_id": department_id,
            "cluster_id": cluster_id,
            "usage_info": usage_info,
            "status_info": status_info,
        }

        query_params = models.build_query_params(
            query_model=models.CredentialsGetAllQueryParams, params=params
        )
        return self.client.get(path, query_params)


class AccessKeyController(CredentialsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/credentials/access-key"

    def create(
        self,
        name: str,
        scope: Literal["system", "tenant", "cluster", "department", "project"],
        access_key_id: Optional[dict] = None,
        access_key_secret: Optional[dict] = None,
        existing_secret_name: Optional[str] = None,
        workload_supported_types: Optional[dict] = None,
        description: Optional[str] = None,
        cluster_id: Optional[str] = None,
        department_id: Optional[str] = None,
        project_id: Optional[str] = None,
        auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "accessKeyId": access_key_id,
                "secretAccessKey": access_key_secret,
                "existingSecretName": existing_secret_name,
            },
        }

        access_key_model = models.build_model(
            model=models.AccessKeyCredentialCreateRequest, data=data
        )
        payload = access_key_model.model_dump_json()

        return self.client.post(self.path, payload)


class PasswordController(CredentialsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/credentials/password"

    def create(
            self,
            name: str,
            scope: Literal["system", "tenant", "cluster", "department", "project"],
            user: Optional[dict] = None,
            password: Optional[dict] = None,
            existing_secret_name: Optional[str] = None,
            workload_supported_types: Optional[dict] = None,
            description: Optional[str] = None,
            cluster_id: Optional[str] = None,
            department_id: Optional[str] = None,
            project_id: Optional[str] = None,
            auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "user": user,
                "password": password,
                "existingSecretName": existing_secret_name,
            },
        }

        password_model = models.build_model(
            model=models.PasswordCredentialCreateRequest, data=data
        )
        payload = password_model.model_dump_json()

        return self.client.post(self.path, payload)


class DockerRegistryController(CredentialsController):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/credentials/docker-registry"

    def create(
            self,
            name: str,
            scope: Literal["system", "tenant", "cluster", "department", "project"],
            user: Optional[dict] = None,
            password: Optional[dict] = None,
            url: Optional[dict] = None,
            existing_secret_name: Optional[str] = None,
            workload_supported_types: Optional[dict] = None,
            description: Optional[str] = None,
            cluster_id: Optional[str] = None,
            department_id: Optional[str] = None,
            project_id: Optional[str] = None,
            auto_delete: Optional[bool] = False,
    ):

        data = {
            "meta": self._build_meta(
                name,
                scope,
                workload_supported_types,
                description,
                cluster_id,
                department_id,
                project_id,
                auto_delete,
            ),
            "spec": {
                "user": user,
                "password": password,
                "url": url,
                "existingSecretName": existing_secret_name,
            },
        }

        password_model = models.build_model(
            model=models.DockerRegistryCredentialCreateRequest, data=data
        )
        payload = password_model.model_dump_json()

        return self.client.post(self.path, payload)


class CredentialsFactory:
    def __init__(self, client):
        self.client = client

    def _get_controller(self, controller_cls):
        return controller_cls(self.client)

    @property
    def access_key(self):
        return self._get_controller(AccessKeyController)

    @property
    def password(self):
        return self._get_controller(PasswordController)

    @property
    def docker_registry_secret(self):
        return self._get_controller(DockerRegistryController)


class AssetsFactory:
    def __init__(self, client):
        self.client = client

    def _get_controller(self, controller_cls):
        return controller_cls(self.client)

    @property
    def pvc(self) -> PVCController:
        return self._get_controller(PVCController)

    @property
    def s3(self) -> S3Controller:
        return self._get_controller(S3Controller)

    @property
    def git(self) -> GitController:
        return self._get_controller(GitController)

    @property
    def nfs(self) -> NFSController:
        return self._get_controller(NFSController)

    @property
    def credentials(self) -> CredentialsFactory:
        return self._get_controller(CredentialsFactory)
