import abc

from runai import api
from runai.api_client import ApiClient


class _ApiGroup(abc.ABC):
    def options(self) -> list:
        # List cls properties
        return [
            attr
            for attr in dir(self)
            if isinstance(getattr(type(self), attr, None), property)
        ]


class Organizations(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def clusters(self) -> api.ClustersApi:
        return api.ClustersApi(self.api_client)

    @property
    def departments(self) -> api.DepartmentsApi:
        return api.DepartmentsApi(self.api_client)

    @property
    def reports(self) -> api.ReportsApi:
        return api.ReportsApi(self.api_client)

    @property
    def node_pools(self) -> api.NodePoolsApi:
        return api.NodePoolsApi(self.api_client)

    @property
    def nodes(self) -> api.NodesApi:
        return api.NodesApi(self.api_client)

    @property
    def projects(self) -> api.ProjectsApi:
        return api.ProjectsApi(self.api_client)

    @property
    def tenant(self) -> api.TenantApi:
        return api.TenantApi(self.api_client)

    @property
    def logo(self) -> api.LogoApi:
        return api.LogoApi(self.api_client)

    @property
    def researcher_command_line_interface(
        self,
    ) -> api.ResearcherCommandLineInterfaceApi:
        return api.ResearcherCommandLineInterfaceApi(self.api_client)

    @property
    def researcher_command_line_interface_deprecated(
        self,
    ) -> api.ResearcherCommandLineInterfaceDeprecatedApi:
        return api.ResearcherCommandLineInterfaceDeprecatedApi(self.api_client)

    @property
    def administrator_command_line_interface(
        self,
    ) -> api.AdministratorCommandLineInterfaceApi:
        return api.AdministratorCommandLineInterfaceApi(self.api_client)


class AuthenticationAndAuthorization(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def access_rules(self) -> api.AccessRulesApi:
        return api.AccessRulesApi(self.api_client)

    @property
    def permissions(self) -> api.PermissionsApi:
        return api.PermissionsApi(self.api_client)

    @property
    def applications(self) -> api.ApplicationsApi:
        return api.ApplicationsApi(self.api_client)

    @property
    def roles(self) -> api.RolesApi:
        return api.RolesApi(self.api_client)

    @property
    def tokens(self) -> api.TokensApi:
        return api.TokensApi(self.api_client)

    @property
    def users(self) -> api.UsersApi:
        return api.UsersApi(self.api_client)

    @property
    def user_applications(self) -> api.UserApplicationsApi:
        return api.UserApplicationsApi(self.api_client)

    @property
    def idps(self) -> api.IdpsApi:
        return api.IdpsApi(self.api_client)

    @property
    def me(self) -> api.MeApi:
        return api.MeApi(self.api_client)

    @property
    def settings(self) -> api.SettingsApi:
        return api.SettingsApi(self.api_client)

    @property
    def org_unit(self) -> api.OrgUnitApi:
        return api.OrgUnitApi(self.api_client)

    @property
    def logout(self) -> api.LogoutApi:
        return api.LogoutApi(self.api_client)


class Audit(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def audit_logs(self) -> api.AuditLogsApi:
        return api.AuditLogsApi(self.api_client)


class Datavolumes(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def datavolumes(self) -> api.DatavolumesApi:
        return api.DatavolumesApi(self.api_client)


class Workloads(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def events(self) -> api.EventsApi:
        return api.EventsApi(self.api_client)

    @property
    def pods(self) -> api.PodsApi:
        return api.PodsApi(self.api_client)

    @property
    def workloads(self) -> api.WorkloadsApi:
        return api.WorkloadsApi(self.api_client)

    @property
    def workspaces(self) -> api.WorkspacesApi:
        return api.WorkspacesApi(self.api_client)

    @property
    def trainings(self) -> api.TrainingsApi:
        return api.TrainingsApi(self.api_client)

    @property
    def inferences(self) -> api.InferencesApi:
        return api.InferencesApi(self.api_client)

    @property
    def revisions(self) -> api.RevisionsApi:
        return api.RevisionsApi(self.api_client)

    @property
    def distributed(self) -> api.DistributedApi:
        return api.DistributedApi(self.api_client)

    @property
    def workloads_batch(self) -> api.WorkloadsBatchApi:
        return api.WorkloadsBatchApi(self.api_client)

    @property
    def workloads_priorities(self) -> api.WorkloadsPrioritiesApi:
        return api.WorkloadsPrioritiesApi(self.api_client)

    @property
    def distributed_inferences(self) -> api.DistributedInferencesApi:
        return api.DistributedInferencesApi(self.api_client)


class WorkloadAssets(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def compute(self) -> api.ComputeApi:
        return api.ComputeApi(self.api_client)

    @property
    def credentials(self) -> api.CredentialsApi:
        return api.CredentialsApi(self.api_client)

    @property
    def datasources(self) -> api.DatasourcesApi:
        return api.DatasourcesApi(self.api_client)

    @property
    def environment(self) -> api.EnvironmentApi:
        return api.EnvironmentApi(self.api_client)

    @property
    def storage_classes(self) -> api.StorageClassesApi:
        return api.StorageClassesApi(self.api_client)

    @property
    def git(self) -> api.GitApi:
        return api.GitApi(self.api_client)

    @property
    def host_path(self) -> api.HostPathApi:
        return api.HostPathApi(self.api_client)

    @property
    def nfs(self) -> api.NFSApi:
        return api.NFSApi(self.api_client)

    @property
    def pvc(self) -> api.PVCApi:
        return api.PVCApi(self.api_client)

    @property
    def registry(self) -> api.RegistryApi:
        return api.RegistryApi(self.api_client)

    @property
    def s3(self) -> api.S3Api:
        return api.S3Api(self.api_client)

    @property
    def config_map(self) -> api.ConfigMapApi:
        return api.ConfigMapApi(self.api_client)

    @property
    def secret(self) -> api.SecretApi:
        return api.SecretApi(self.api_client)

    @property
    def template(self) -> api.TemplateApi:
        return api.TemplateApi(self.api_client)


class Policies(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def policy(self) -> api.PolicyApi:
        return api.PolicyApi(self.api_client)


class Notifications(_ApiGroup):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @property
    def notification_state(self) -> api.NotificationStateApi:
        return api.NotificationStateApi(self.api_client)

    @property
    def notification_types(self) -> api.NotificationTypesApi:
        return api.NotificationTypesApi(self.api_client)

    @property
    def notification_channels(self) -> api.NotificationChannelsApi:
        return api.NotificationChannelsApi(self.api_client)

    @property
    def subscriptions(self) -> api.SubscriptionsApi:
        return api.SubscriptionsApi(self.api_client)


class RunaiClient:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.aclose()

    def __del__(self):
        self.close()

    def close(self):
        """Close the client and cleanup resources."""
        if self.api_client:
            self.api_client.close()

    async def aclose(self):
        """Close the client and cleanup resources asynchronously."""
        if self.api_client:
            await self.api_client.close()

    @property
    def organizations(self) -> Organizations:
        return Organizations(self.api_client)

    @property
    def authentication_and_authorization(self) -> AuthenticationAndAuthorization:
        return AuthenticationAndAuthorization(self.api_client)

    @property
    def audit(self) -> Audit:
        return Audit(self.api_client)

    @property
    def datavolumes(self) -> Datavolumes:
        return Datavolumes(self.api_client)

    @property
    def workloads(self) -> Workloads:
        return Workloads(self.api_client)

    @property
    def workload_assets(self) -> WorkloadAssets:
        return WorkloadAssets(self.api_client)

    @property
    def policies(self) -> Policies:
        return Policies(self.api_client)

    @property
    def notifications(self) -> Notifications:
        return Notifications(self.api_client)
