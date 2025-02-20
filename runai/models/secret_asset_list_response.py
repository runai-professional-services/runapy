# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from runai.models.secret_asset import SecretAsset
from typing import Optional, Set
from typing_extensions import Self


class SecretAssetListResponse(BaseModel):
    """
    Pydantic class model representing SecretAssetListResponse.

    Parameters:
        ```python
        entries: List[SecretAsset]
        ```
        entries: See model List[SecretAsset] for more information.
    Example:
        ```python
        SecretAssetListResponse(
            entries=[
                    runai.models.secret_asset.SecretAsset(
                        meta = {"name":"my-asset","scope":"tenant","id":"a418ed33-9399-48c0-a890-122cadd13bfd","kind":"s3","createdBy":"test@run.ai","createdAt":"2023-02-23T14:25:36.707685Z","updatedBy":"test@run.ai","updatedAt":"2023-02-23T14:25:36.707685Z","workloadSupportedTypes":{"workspace":false,"training":false,"distributed":true,"distFramework":"TF"}},
                        spec = runai.models.secret_asset_spec.SecretAssetSpec(),
                        used_by = runai.models.asset_usage_info.AssetUsageInfo(
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
                        usage_times = runai.models.usage_times_info.UsageTimesInfo(
                            last_used_by_workload = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                        compliance = runai.models.compliance_info.ComplianceInfo(
                            imposed = True,
                            reason = [
                                runai.models.compliance_info_reason.ComplianceInfoReason(
                                    field = '',
                                    details = '', )
                                ], ),
                        status = runai.models.asset_cluster_status_info.AssetClusterStatusInfo(
                            issues = [
                                runai.models.asset_cluster_status_issue.AssetClusterStatusIssue(
                                    scope_id = '',
                                    scope_type = 'system',
                                    issue = 'ReplicationError', )
                                ],
                            message = '',
                            url = '', ), )
                    ]
        )
        ```
    """  # noqa: E501

    entries: List[SecretAsset]
    __properties: ClassVar[List[str]] = ["entries"]

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
        """Create an instance of SecretAssetListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item_entries in self.entries:
                if _item_entries:
                    _items.append(_item_entries.to_dict())
            _dict["entries"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecretAssetListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "entries": (
                    [SecretAsset.from_dict(_item) for _item in obj["entries"]]
                    if obj.get("entries") is not None
                    else None
                )
            }
        )
        return _obj
