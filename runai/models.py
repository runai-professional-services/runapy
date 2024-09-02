import uuid

from typing import Optional, List, Literal
from enum import StrEnum

import pydantic
from pydantic import BaseModel, UUID4

from . import errors


def convert_to_uuid4(uuid_string: str) -> UUID4:
    try:
        uuid_obj = uuid.UUID(uuid_string, version=4)
        if str(uuid_obj) == uuid_string:
            return UUID4(uuid_obj)
        else:
            raise errors.RunaiClientError(err=None, message=f"Bad convertion from str to uuid4 back to str. Original str '{uuid_string}' , new str '{str(uuid_obj)}'")
    except Exception:
        raise errors.RunaiClientError(err=None, message=f"Failed to convert string to uuid4, string: '{uuid_string}' is not a valid UUID4")


class UUID4Model(BaseModel):
    field: UUID4

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_cluster_id

    @classmethod
    def validate_cluster_id(cls, v):
        return convert_to_uuid4(v)


class ResourcesPlacementStrategy(BaseModel):
    cpu: Literal["spread", "binpack"]
    gpu: Literal["spread", "binpack"]


class NodePoolLabels(BaseModel):
    labelKey: str
    labelValue: str


class NodePool(BaseModel):
    id: int
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class NodePoolUpdateRequest(BaseModel):
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class NodePoolCreateRequest(BaseModel):
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class Resource(BaseModel):
    deserved: int
    limit: int
    overQuotaWeight: Optional[int] = None


class Memory(Resource):
    units: Literal["Mib", "MB", "GB"]


class NodeTypes(BaseModel):
    """
    training : Optional[List[str]]
    workspace: Optional[List[str]]
    """

    training: Optional[List[str]] = None
    workspace: Optional[List[str]] = None


class SchedulingRules(BaseModel):
    """
    Scheduling rules to be applied on all workloads within the project

    interactiveJobTimeLimitSeconds: Optional[int] = None
    interactiveJobMaxIdleDurationSeconds: Optional[int] = None
    interactiveJobPreemptIdleDurationSeconds: Optional[int] = None
    trainingJobTimeLimitSeconds: Optional[int] = None
    trainingJobMaxIdleDurationSeconds: Optional[int] = None
    """

    interactiveJobTimeLimitSeconds: Optional[int] = None
    interactiveJobMaxIdleDurationSeconds: Optional[int] = None
    interactiveJobPreemptIdleDurationSeconds: Optional[int] = None
    trainingJobTimeLimitSeconds: Optional[int] = None
    trainingJobMaxIdleDurationSeconds: Optional[int] = None


class NodePoolIdentifier(BaseModel):
    id: str
    name: str


class Resources(BaseModel):
    """
        Set the gpu, cpu, and memory resources for a given nodepool.
        CPU/Memory may not work if your organization does not permit assiging these resources

        "nodePool": {
            id: str
            name: str
        },
        "gpu": {
            deserved: int
            limit: int
            overQuotaWeight: int
        },
        "cpu": {
            "deserved": int,
            "limit": int,
            "overQuotaWeight": int
        },
            "memory": {
                "deserved": int,
                "limit": int,
                "overQuotaWeight": int,
                "units": "Mib" or "GB" or "MB,
        }

        Example:
        {
            {
                "nodePool": {
                "id": 22,
                "name": "default"
            },
                "gpu": {
                "deserved": 1000,
                "limit": 0,
                "overQuotaWeight": 2
            },
                "cpu": {
                "deserved": 1000,
                "limit": 0,
                "overQuotaWeight": 2
            },
                "memory": {
                "deserved": 1000,
                "limit": 0,
                "overQuotaWeight": 2,
                "units": "Mib"
            }
    }
        }
    """

    nodePool: NodePoolIdentifier
    gpu: Resource
    cpu: Optional[Resource] = None
    memory: Optional[Memory] = None


class ProjectUpdateRequest(BaseModel):
    resources: List[Resources]
    nodeTypes: Optional[NodeTypes] = None
    defaultNodePools: Optional[List[str]] = None
    schedulingRules: Optional[SchedulingRules] = None


class ProjectCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]
    nodeTypes: Optional[NodeTypes] = None
    defaultNodePools: Optional[List[str]] = None
    schedulingRules: Optional[SchedulingRules] = None
    requestedNamespace: Optional[str] = None
    parentId: Optional[str] = None


class DepartmentCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]


class DepartmentUpdateRequest(BaseModel):
    resources: List[Resources]
    nodeTypes: Optional[NodeTypes] = None
    defaultNodePools: Optional[List[str]] = None
    schedulingRules: Optional[SchedulingRules] = None


class UserCreateRequest(BaseModel):
    email: str
    resetPassword: Optional[bool] = False


class AccessRule(BaseModel):
    subjectId: str
    subjectType: Literal["user", "app", "group"]
    roleId: int
    scopeId: str
    scopeType: Literal["system", "tenant", "cluster", "department", "project"]
    clusterId: str


class ProbeReadinessHandlerHTTPGet(BaseModel):
    path: str
    port: int
    host: str
    scheme: Literal["HTTP", "HTTPS"]


class ReadinessProbe(BaseModel):
    initialDelaySeconds: int
    periodSeconds: int
    timeoutSeconds: int
    successThreshold: int
    failureThreshold: int
    handler: ProbeReadinessHandlerHTTPGet


class Probes(BaseModel):
    readiness: ReadinessProbe


class PodAffinity(BaseModel):
    key: str
    type: Literal["Required", "Preferred"]


class EnvironmentVariable(BaseModel):
    name: str
    value: str
    exclude: bool = False


class Annotations(BaseModel):
    name: str
    value: str
    exclude: bool = False


class Labels(BaseModel):
    name: str
    value: str
    exclude: bool = False


class Tolerations(BaseModel):
    name: str
    operator: Literal["Equal", "Exists"]
    key: str
    value: str
    effect: Literal["NoSchedule", "NoExecute", "PreferNoSchedule"]
    seconds: int


class Port(BaseModel):
    container: int
    serviceType: Literal["LoadBalancer", "NodePort", "ClusterIP"]
    external: int
    toolType: str
    toolName: str
    name: str


class ExposedUrl(BaseModel):
    container: int
    toolType: str
    toolName: str
    authorizedUsers: Optional[List[str]] = None
    authorizedGroups: Optional[List[str]] = None
    name: Optional[str] = None
    url: Optional[str] = None


class RelatedUrl(BaseModel):
    url: str
    type: str
    name: str


class ExtendedResource(BaseModel):
    resource: str
    quantity: str
    exclude: bool


class Compute(BaseModel):
    gpuDevicesRequest: Optional[int] = None
    gpuRequestType: Optional[Literal["portion", "memory", "migProfile"]] = None
    gpuPortionRequest: Optional[float] = None
    gpuPortionLimit: Optional[float] = None
    gpuMemoryRequest: Optional[str] = None
    gpuMemoryLimit: Optional[str] = None
    migProfile: Optional[
        Literal[
            "1g.5gb",
            "1g.10gb",
            "2g.10gb",
            "2g.20gb",
            "3g.20gb",
            "3g.40gb",
            "4g.20gb",
            "4g.40gb",
            "7g.40gb",
            "7g.80gb",
        ]
    ] = None
    cpuCoreRequest: Optional[float] = None
    cpuCoreLimit: Optional[float] = None
    cpuMemoryRequest: Optional[str] = None
    cpuMemoryLimit: Optional[str] = None
    largeShmRequest: Optional[bool] = None
    extendedResources: Optional[ExtendedResource] = None


class WorkloadDataVolume(BaseModel):
    id: str
    mountPath: str


class WorkloadPvcClaimInfoAccessModes(BaseModel):
    readWriteOnce: bool = True
    readOnlyMany: bool = False
    readWriteMany: bool = False


class WorkloadPvcClaimInfo(BaseModel):
    size: str
    storageClass: str
    accessModes: WorkloadPvcClaimInfoAccessModes
    volumeMode: Literal["Filesystem", "Block"] = "Filesystem"


class WorkloadPvc(BaseModel):
    name: Optional[str] = None
    claimName: str
    path: str
    existingPvc: Optional[bool] = False
    readOnly: Optional[bool] = False
    ephemeral: Optional[bool] = False
    claimInfo: Optional[WorkloadPvcClaimInfo] = None


class WorkloadGit(BaseModel):
    name: str
    repository: str
    branch: str
    revision: str
    path: str
    passwordSecret: str
    secretKeyOfUser: str
    secretKeyOfPassword: str


class WorkloadConfigMapVolume(BaseModel):
    name: Optional[str] = None
    configMap: str
    mountPath: str


class WorkloadSecretVolume(BaseModel):
    name: Optional[str] = None
    secret: str
    mountPath: str


class WorkloadHostPath(BaseModel):
    name: Optional[str] = None
    path: str
    mountPath: str
    mountPropagation: Optional[Literal["None", "HostToContainer"]] = "None"
    readOnly: Optional[bool] = True


class WorkloadNfs(BaseModel):
    name: Optional[str] = None
    path: str
    mountPath: str
    server: str
    readOnly: Optional[bool] = True


class WorkloadS3(BaseModel):
    name: Optional[str] = None
    path: str
    bucket: str
    url: str
    server: str
    accessKeySecret: str
    secretKeyOfAccessKeyId: str
    secretKeyOfSecretKey: str


class WorkloadStorage(BaseModel):
    dataVolume: Optional[WorkloadDataVolume] = None
    pvc: Optional[List[WorkloadPvc]] = None
    git: Optional[WorkloadGit] = None
    configMapVolume: Optional[List[WorkloadConfigMapVolume]] = None
    secretVolume: Optional[WorkloadSecretVolume] = None
    hostPath: Optional[WorkloadHostPath] = None
    nfs: Optional[WorkloadNfs] = None
    s3: Optional[WorkloadS3] = None


class WorkloadSecurity(BaseModel):
    uidGidSource: Optional[Literal["fromTheImage", "fromIdpToken", "custom"]] = None
    capabilities: Optional[
        List[
            Literal[
                "AUDIT_CONTROL",
                "AUDIT_READ",
                "AUDIT_WRITE",
                "BLOCK_SUSPEND",
                "CHOWN",
                "DAC_OVERRIDE",
                "DAC_READ_SEARCH",
                "FOWNER",
                "FSETID",
                "IPC_LOCK",
                "IPC_OWNER",
                "KILL",
                "LEASE",
                "LINUX_IMMUTABLE",
                "MAC_ADMIN",
                "MAC_OVERRIDE",
                "MKNOD",
                "NET_ADMIN",
                "NET_BIND_SERVICE",
                "NET_BROADCAST",
                "NET_RAW",
                "SETGID",
                "SETFCAP",
                "SETPCAP",
                "SETUID",
                "SYS_ADMIN",
                "SYS_BOOT",
                "SYS_CHROOT",
                "SYS_MODULE",
                "SYS_NICE",
                "SYS_PACCT",
                "SYS_PTRACE",
                "SYS_RAWIO",
                "SYS_RESOURCE",
                "SYS_TIME",
                "SYS_TTY_CONFIG",
                "SYSLOG",
                "WAKE_ALARM",
            ]
        ]
    ] = None
    seccompProfileType: Optional[
        Literal["RuntimeDefault", "Unconfined", "Localhost"]
    ] = None
    runAsNonRoot: Optional[bool] = None
    readOnlyRootFilesystem: Optional[bool] = None
    runAsUid: Optional[int] = None
    runAsGid: Optional[int] = None
    supplementalGroups: Optional[str] = None
    allowPrivilegeEscalation: Optional[bool] = None
    hostIpc: Optional[bool] = False
    hostNetwork: Optional[bool] = False


class WorkloadBaseSpec(BaseModel):
    command: Optional[str] = None
    args: Optional[str] = None
    image: str
    imagePullPolicy: Literal["Always", "IfNotPresent", "Never"] = "Always"
    compute: Compute
    workingDir: Optional[str] = None
    createHomeDir: Optional[bool] = None
    probes: Optional[Probes] = None
    nodeType: Optional[str] = None
    nodePools: Optional[List[str]] = None
    podAffinity: Optional[PodAffinity] = None
    environmentVariables: Optional[List[EnvironmentVariable]] = None
    annotations: Optional[List[Annotations]] = None
    labels: Optional[List[Labels]] = None
    tolerations: Optional[List[Tolerations]] = None
    terminateAfterPreemption: Optional[bool] = None
    autoDeletionTimeAfterCompletionSeconds: Optional[int] = None
    backoffLimit: Optional[int] = None
    ports: Optional[List[Port]] = None
    exposedUrls: Optional[List[ExposedUrl]] = None
    relatedUrls: Optional[List[RelatedUrl]] = None
    storage: Optional[WorkloadStorage] = None
    security: Optional[WorkloadSecurity] = None


class TrainingWorkloadSpec(WorkloadBaseSpec):
    completions: Optional[int] = None
    parallelism: Optional[int] = None
    priorityClass: Optional[Literal["train"]] = "train"  # Default value for training


class WorkspaceWorkloadSpec(WorkloadBaseSpec):
    priorityClass: Optional[Literal["build", "interactive-preemptible"]] = (
        "build"  # Default value for workspace
    )


class WorkspaceCreateRequest(BaseModel):
    name: str
    projectId: str
    clusterId: str
    useGivenNameAsPrefix: bool = False
    spec: WorkspaceWorkloadSpec


class TrainingCreateRequest(BaseModel):
    name: str
    projectId: str
    clusterId: str
    useGivenNameAsPrefix: bool = False
    spec: TrainingWorkloadSpec


class ServingPort(BaseModel):
    container: int
    protocol: Literal["http", "grpc"]


class AutoScaling(BaseModel):
    minReplicas: int
    maxReplicas: int
    scaleToZeroRetentionSeconds: int
    metric: Literal["throughput", "concurrency", "latency"]
    metricThreshold: int


class InferenceWorkloadSpec(WorkloadBaseSpec):
    servingPort: ServingPort
    autoscaling: AutoScaling


class InferenceCreateRequest(BaseModel):
    name: str
    projectId: str
    clusterId: str
    useGivenNameAsPrefix: bool = False
    spec: InferenceWorkloadSpec


class DistributedWorkloadSpec(WorkloadBaseSpec):
    numWorkers: int
    distributedFramework: Literal["MPI", "PyTorch", "TF", "XGBoost"]
    slotsPerWorker: Optional[int] = 1
    minReplicas: Optional[int] = None
    maxReplicas: Optional[int] = None


class DistributedCreateRequest(BaseModel):
    name: str
    projectId: str
    clusterId: str
    spec: DistributedWorkloadSpec
    useGivenNameAsPrefix: bool = False
    masterSpec: Optional[DistributedWorkloadSpec] = None


def build_model(model: BaseModel, data: dict) -> BaseModel:
    try:
        built_model = model(**data)
        return built_model
    except pydantic.ValidationError as e:
        raise errors.RunaiBuildModelError(err=e)


class SortOrderEnum(StrEnum):
    asc = "asc"
    desc = "desc"


class ProjectSortByEnum(StrEnum):
    name = "name"
    clusterId = "clusterId"
    departmentId = "departmentId"
    createdAt = "createdAt"


class CommonGetAllQueryParams(BaseModel):
    filterBy: Optional[str] = None
    sortOrder: Optional[Literal["asc", "desc"]] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


class ProjectQueryParams(CommonGetAllQueryParams):
    sortBy: Optional[ProjectSortByEnum] = None


class DepartmentSortByEnum(StrEnum):
    name = "name"
    clusterId = "clusterId"
    createdAt = "createdAt"


class DepartmentQueryParams(BaseModel):
    filterBy: Optional[str] = None
    sortBy: Optional[Literal["name", "clusterId", "createdAt"]] = None
    sortOrder: Optional[Literal["asc", "desc"]] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


class NodePoolsQueryParams(BaseModel):
    start: str
    end: str
    metricType: Literal[
        "GPU_UTILIZATION",
        "GPU_MEMORY_UTILIZATION",
        "CPU_UTILIZATION",
        "CPU_MEMORY_UTILIZATION",
        "TOTAL_GPU",
        "GPU_QUOTA",
        "ALLOCATED_GPU",
        "AVG_WORKLOAD_WAIT_TIME",
    ]
    numberOfSamples: Optional[int] = 20


class AccessRulesSortByEnum(StrEnum):
    subjectId = "subjectId"
    subjectType = "subjectType"
    roleId = "roleId"
    scopeId = "scopeId"
    scopeType = "scopeType"
    roleName = "roleName"
    scopeName = "scopeName"
    createdAt = "createdAt"
    deletedAt = "deletedAt"
    createdBy = "createdBy"


class AccessRulesQueryParams(BaseModel):
    subjectType: Optional[str] = None
    subjectIds: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    lastUpdated: Optional[str] = None
    includeDeleted: Optional[bool] = None
    clusterId: Optional[str] = None
    scopeId: Optional[str] = None
    filterBy: Optional[str] = None
    sortBy: Optional[AccessRulesSortByEnum] = None
    sortOrder: Optional[SortOrderEnum] = "asc"


class ClusterQueryParams(BaseModel):
    verbosity: Optional[Literal["full", "metadata"]] = "full"


class WorkloadsCountQueryParams(BaseModel):
    deleted: bool
    filterBy: Optional[str] = None


class WorkloadsTelemetryQueryParams(BaseModel):
    telemetryType: Literal["WORKLOADS_COUNT", "GPU_ALLOCATION"]
    clusterId: Optional[str] = None
    nodepoolName: Optional[str] = None
    departmentId: Optional[str] = None
    groupBy: Optional[str] = None


class WorkloadMetricsQueryParams(BaseModel):
    start: str
    end: str
    metricType: Literal[
        "GPU_UTILIZATION",
        "GPU_MEMORY_REQUEST_BYTES",
        "CPU_USAGE_CORES",
        "CPU_REQUEST_CORES",
        "CPU_LIMIT_CORES",
        "CPU_MEMORY_USAGE_BYTES",
        "CPU_MEMORY_REQUEST_BYTES",
        "CPU_MEMORY_LIMIT_BYTES",
        "POD_COUNT",
        "RUNNING_POD_COUNT",
        "GPU_ALLOCATION",
    ]
    numberOfSamples: Optional[int] = 20


class InferenceWorkloadQueryParams(BaseModel):
    start: str
    end: str
    metricType: Literal["THROUGHPUT", "LATENCY"]
    numberOfSamples: Optional[int] = 20


class WorkloadsGetAllQueryParams(CommonGetAllQueryParams):
    deleted: Optional[bool] = False
    sortBy: Optional[
        Literal[
            "type",
            "name",
            "clusterId",
            "projectId",
            "projectName",
            "departmentId",
            "departmentName",
            "createdAt",
            "deletedAt",
            "submittedBy",
            "phase",
            "completedAt",
            "nodepool",
            "allocatedGPU",
        ]
    ] = None


def build_query_params(query_model: BaseModel, params: dict) -> BaseModel:
    try:
        built_model = query_model(**params)
        return built_model
    except pydantic.ValidationError as e:
        raise errors.RunaiQueryParamsError(err=e)
