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
from runai.models.asset_meta import AssetMeta
from runai.models.asset_usage_info import AssetUsageInfo
from runai.models.compliance_info import ComplianceInfo
from runai.models.host_path_spec import HostPathSpec
from runai.models.usage_times_info import UsageTimesInfo
from typing import Optional, Set
from typing_extensions import Self


class HostPathAsset(BaseModel):
    """
    Pydantic class model representing HostPathAsset.

    Parameters:
        ```python
        meta: AssetMeta
        spec: HostPathSpec
        used_by: Optional[AssetUsageInfo]
        usage_times: Optional[UsageTimesInfo]
        compliance: Optional[ComplianceInfo]
        ```
        meta: See model AssetMeta for more information.
        spec: See model HostPathSpec for more information.
        used_by: See model AssetUsageInfo for more information.
        usage_times: See model UsageTimesInfo for more information.
        compliance: See model ComplianceInfo for more information.
    Example:
        ```python
        HostPathAsset(
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
                        usage_times=runai.models.usage_times_info.UsageTimesInfo(
                    last_used_by_workload = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                        compliance=runai.models.compliance_info.ComplianceInfo(
                    imposed = True,
                    compliance = True,
                    reason = [
                        runai.models.compliance_info_reason.ComplianceInfoReason(
                            field = '',
                            details = '', )
                        ], )
        )
        ```
    """  # noqa: E501

    meta: AssetMeta
    spec: HostPathSpec
    used_by: Optional[AssetUsageInfo] = Field(default=None, alias="usedBy")
    usage_times: Optional[UsageTimesInfo] = Field(default=None, alias="usageTimes")
    compliance: Optional[ComplianceInfo] = None
    __properties: ClassVar[List[str]] = [
        "meta",
        "spec",
        "usedBy",
        "usageTimes",
        "compliance",
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
        """Create an instance of HostPathAsset from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of usage_times
        if self.usage_times:
            _dict["usageTimes"] = self.usage_times.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compliance
        if self.compliance:
            _dict["compliance"] = self.compliance.to_dict()
        # set to None if used_by (nullable) is None
        # and model_fields_set contains the field
        if self.used_by is None and "used_by" in self.model_fields_set:
            _dict["usedBy"] = None

        # set to None if usage_times (nullable) is None
        # and model_fields_set contains the field
        if self.usage_times is None and "usage_times" in self.model_fields_set:
            _dict["usageTimes"] = None

        # set to None if compliance (nullable) is None
        # and model_fields_set contains the field
        if self.compliance is None and "compliance" in self.model_fields_set:
            _dict["compliance"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostPathAsset from a dict"""
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
                    HostPathSpec.from_dict(obj["spec"])
                    if obj.get("spec") is not None
                    else None
                ),
                "usedBy": (
                    AssetUsageInfo.from_dict(obj["usedBy"])
                    if obj.get("usedBy") is not None
                    else None
                ),
                "usageTimes": (
                    UsageTimesInfo.from_dict(obj["usageTimes"])
                    if obj.get("usageTimes") is not None
                    else None
                ),
                "compliance": (
                    ComplianceInfo.from_dict(obj["compliance"])
                    if obj.get("compliance") is not None
                    else None
                ),
            }
        )
        return _obj
