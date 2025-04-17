# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.access_key_spec import AccessKeySpec
from runai.models.asset_cluster_status_info import AssetClusterStatusInfo
from runai.models.asset_meta import AssetMeta
from runai.models.asset_usage_info import AssetUsageInfo
from runai.models.cluster_info1 import ClusterInfo1
from runai.models.compliance_info import ComplianceInfo
from typing import Optional, Set
from typing_extensions import Self


class AccessKey(BaseModel):
    """
    Pydantic class model representing AccessKey.

    Parameters:
        ```python
        meta: AssetMeta
        spec: AccessKeySpec
        used_by: Optional[AssetUsageInfo]
        compliance: Optional[ComplianceInfo]
        status: Optional[AssetClusterStatusInfo]
        cluster_info: Optional[ClusterInfo1]
        ```
        meta: See model AssetMeta for more information.
        spec: See model AccessKeySpec for more information.
        used_by: See model AssetUsageInfo for more information.
        compliance: See model ComplianceInfo for more information.
        status: See model AssetClusterStatusInfo for more information.
        cluster_info: See model ClusterInfo1 for more information.
    Example:
        ```python
        AccessKey(
            meta={"name":"my-asset","scope":"tenant","id":"a418ed33-9399-48c0-a890-122cadd13bfd","kind":"s3","createdBy":"test@run.ai","createdAt":"2023-02-23T14:25:36.707685Z","updatedBy":"test@run.ai","updatedAt":"2023-02-23T14:25:36.707685Z","workloadSupportedTypes":{"workspace":false,"training":false,"distributed":true,"distFramework":"TF"}},
                        spec="example",
                        used_by=runai.models.asset_usage_info.AssetUsageInfo(
                    workspaces = [
                        runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                            id = '',
                            name = 'my-workload-name',
                            status = '0', )
                        ],
                    trainings = [
                        runai.models.workload_ref_and_status.WorkloadRefAndStatus(
                            id = '',
                            name = 'my-workload-name',
                            status = '0', )
                        ],
                    distributed = [

                        ],
                    inferences = [

                        ],
                    templates = [
                        runai.models.asset_ref.AssetRef(
                            id = '0',
                            name = 'my-asset', )
                        ],
                    assets = runai.models.assets_usage_ref.AssetsUsageRef(
                        environment = runai.models.environment.environment(),
                        environments = [
                            runai.models.asset_ref.AssetRef(
                                id = '0',
                                name = 'my-asset', )
                            ],
                        compute = runai.models.assets_usage_ref_compute.AssetsUsageRefCompute(),
                        computes = [

                            ],
                        datasources = [
                            runai.models.asset_datasource_ref.AssetDatasourceRef(
                                id = '0',
                                name = 'my-asset',
                                kind = 'compute',
                                overrides = runai.models.data_source_overrides.DataSourceOverrides(
                                    container_path = '/container/directory', ), )
                            ], ), ),
                        compliance=runai.models.compliance_info.ComplianceInfo(
                    imposed = True,
                    compliance = True,
                    reason = [
                        runai.models.compliance_info_reason.ComplianceInfoReason(
                            field = '',
                            details = '', )
                        ], ),
                        status=runai.models.asset_cluster_status_info.AssetClusterStatusInfo(
                    status = 'Creating',
                    issues = [
                        runai.models.asset_cluster_status_issue.AssetClusterStatusIssue(
                            scope_id = '',
                            scope_type = 'system',
                            issue = 'ReplicationError', )
                        ],
                    message = '',
                    url = '', ),
                        cluster_info=runai.models.cluster_info1.ClusterInfo1(
                    resources = [
                        runai.models.cluster_resource_info.ClusterResourceInfo(
                            name = 'password-credential-1', )
                        ], )
        )
        ```
    """  # noqa: E501

    meta: AssetMeta
    spec: AccessKeySpec
    used_by: Optional[AssetUsageInfo] = Field(default=None, alias="usedBy")
    compliance: Optional[ComplianceInfo] = None
    status: Optional[AssetClusterStatusInfo] = None
    cluster_info: Optional[ClusterInfo1] = Field(default=None, alias="clusterInfo")
    __properties: ClassVar[List[str]] = [
        "meta",
        "spec",
        "usedBy",
        "compliance",
        "status",
        "clusterInfo",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AccessKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict["spec"] = self.spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of used_by
        if self.used_by:
            _dict["usedBy"] = self.used_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compliance
        if self.compliance:
            _dict["compliance"] = self.compliance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster_info
        if self.cluster_info:
            _dict["clusterInfo"] = self.cluster_info.to_dict()
        # set to None if used_by (nullable) is None
        # and model_fields_set contains the field
        if self.used_by is None and "used_by" in self.model_fields_set:
            _dict["usedBy"] = None

        # set to None if compliance (nullable) is None
        # and model_fields_set contains the field
        if self.compliance is None and "compliance" in self.model_fields_set:
            _dict["compliance"] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict["status"] = None

        # set to None if cluster_info (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_info is None and "cluster_info" in self.model_fields_set:
            _dict["clusterInfo"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "meta": (
                    AssetMeta.from_dict(obj["meta"])
                    if obj.get("meta") is not None
                    else None
                ),
                "spec": (
                    AccessKeySpec.from_dict(obj["spec"])
                    if obj.get("spec") is not None
                    else None
                ),
                "usedBy": (
                    AssetUsageInfo.from_dict(obj["usedBy"])
                    if obj.get("usedBy") is not None
                    else None
                ),
                "compliance": (
                    ComplianceInfo.from_dict(obj["compliance"])
                    if obj.get("compliance") is not None
                    else None
                ),
                "status": (
                    AssetClusterStatusInfo.from_dict(obj["status"])
                    if obj.get("status") is not None
                    else None
                ),
                "clusterInfo": (
                    ClusterInfo1.from_dict(obj["clusterInfo"])
                    if obj.get("clusterInfo") is not None
                    else None
                ),
            }
        )
        return _obj
