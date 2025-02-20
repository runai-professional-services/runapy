# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from runai.models.workload_template import WorkloadTemplate
from typing import Optional, Set
from typing_extensions import Self


class WorkloadTemplateListResponse(BaseModel):
    """
    Pydantic class model representing WorkloadTemplateListResponse.

    Parameters:
        ```python
        entries: List[WorkloadTemplate]
        ```
        entries: See model List[WorkloadTemplate] for more information.
    Example:
        ```python
        WorkloadTemplateListResponse(
            entries=[
                    runai.models.workload_template.WorkloadTemplate(
                        meta = {"name":"my-asset","scope":"tenant","id":"a418ed33-9399-48c0-a890-122cadd13bfd","kind":"s3","createdBy":"test@run.ai","createdAt":"2023-02-23T14:25:36.707685Z","updatedBy":"test@run.ai","updatedAt":"2023-02-23T14:25:36.707685Z","workloadSupportedTypes":{"workspace":false,"training":false,"distributed":true,"distFramework":"TF"}},
                        spec = runai.models.specific_run_info_fields.SpecificRunInfoFields(
                            assets = runai.models.assets_ref.AssetsRef(
                                environment = null,
                                compute = runai.models.assets_ref_compute.AssetsRefCompute(),
                                datasources = [
                                    runai.models.datasource_ref.DatasourceRef(
                                        id = '0',
                                        name = 'my-asset',
                                        kind = 'compute',
                                        overrides = runai.models.data_source_overrides.DataSourceOverrides(
                                            container_path = '/container/directory', ), )
                                    ],
                                workload_volumes = [
                                    ''
                                    ], ),
                            specific_env = runai.models.specific_run_params.SpecificRunParams(),
                            distributed = runai.models.info_distributed.InfoDistributed(), ), )
                    ]
        )
        ```
    """  # noqa: E501

    entries: List[WorkloadTemplate]
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
        """Create an instance of WorkloadTemplateListResponse from a JSON string"""
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
        """Create an instance of WorkloadTemplateListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "entries": (
                    [WorkloadTemplate.from_dict(_item) for _item in obj["entries"]]
                    if obj.get("entries") is not None
                    else None
                )
            }
        )
        return _obj
