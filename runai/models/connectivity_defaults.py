# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.exposed_urls_defaults import ExposedUrlsDefaults
from runai.models.ports_defaults import PortsDefaults
from runai.models.related_urls_defaults import RelatedUrlsDefaults
from typing import Optional, Set
from typing_extensions import Self


class ConnectivityDefaults(BaseModel):
    """
    Pydantic class model representing ConnectivityDefaults.

    Parameters:
        ```python
        ports: Optional[PortsDefaults]
        exposed_urls: Optional[ExposedUrlsDefaults]
        related_urls: Optional[RelatedUrlsDefaults]
        ```
        ports: See model PortsDefaults for more information.
        exposed_urls: See model ExposedUrlsDefaults for more information.
        related_urls: See model RelatedUrlsDefaults for more information.
    Example:
        ```python
        ConnectivityDefaults(
            ports=runai.models.ports_defaults.PortsDefaults(
                    attributes = runai.models.port.Port(
                        container = 8080,
                        service_type = 'LoadBalancer',
                        external = 30080,
                        tool_type = 'pytorch',
                        tool_name = 'my-pytorch',
                        name = 'port-instance-a', ),
                    instances = [
                        runai.models.port.Port(
                            container = 8080,
                            external = 30080,
                            tool_type = 'pytorch',
                            tool_name = 'my-pytorch',
                            name = 'port-instance-a', )
                        ], ),
                        exposed_urls=runai.models.exposed_urls_defaults.ExposedUrlsDefaults(
                    attributes = runai.models.exposed_url.ExposedUrl(
                        container = 8080,
                        url = 'https://my-url.com',
                        authorized_users = ["user-a","user-b"],
                        authorized_groups = ["group-a","group-b"],
                        tool_type = 'jupyter',
                        tool_name = 'my-pytorch',
                        name = 'url-instance-a', ),
                    instances = [
                        runai.models.exposed_url.ExposedUrl(
                            container = 8080,
                            url = 'https://my-url.com',
                            authorized_users = ["user-a","user-b"],
                            authorized_groups = ["group-a","group-b"],
                            tool_type = 'jupyter',
                            tool_name = 'my-pytorch',
                            name = 'url-instance-a', )
                        ], ),
                        related_urls=runai.models.related_urls_defaults.RelatedUrlsDefaults(
                    attributes = runai.models.related_url.RelatedUrl(
                        url = 'https://my-url.com',
                        type = 'wandb',
                        name = 'url-instance-a', ),
                    instances = [
                        runai.models.related_url.RelatedUrl(
                            url = 'https://my-url.com',
                            type = 'wandb',
                            name = 'url-instance-a', )
                        ], )
        )
        ```
    """  # noqa: E501

    ports: Optional[PortsDefaults] = None
    exposed_urls: Optional[ExposedUrlsDefaults] = Field(
        default=None, alias="exposedUrls"
    )
    related_urls: Optional[RelatedUrlsDefaults] = Field(
        default=None, alias="relatedUrls"
    )
    __properties: ClassVar[List[str]] = ["ports", "exposedUrls", "relatedUrls"]

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
        """Create an instance of ConnectivityDefaults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ports
        if self.ports:
            _dict["ports"] = self.ports.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposed_urls
        if self.exposed_urls:
            _dict["exposedUrls"] = self.exposed_urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_urls
        if self.related_urls:
            _dict["relatedUrls"] = self.related_urls.to_dict()
        # set to None if ports (nullable) is None
        # and model_fields_set contains the field
        if self.ports is None and "ports" in self.model_fields_set:
            _dict["ports"] = None

        # set to None if exposed_urls (nullable) is None
        # and model_fields_set contains the field
        if self.exposed_urls is None and "exposed_urls" in self.model_fields_set:
            _dict["exposedUrls"] = None

        # set to None if related_urls (nullable) is None
        # and model_fields_set contains the field
        if self.related_urls is None and "related_urls" in self.model_fields_set:
            _dict["relatedUrls"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectivityDefaults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ports": (
                    PortsDefaults.from_dict(obj["ports"])
                    if obj.get("ports") is not None
                    else None
                ),
                "exposedUrls": (
                    ExposedUrlsDefaults.from_dict(obj["exposedUrls"])
                    if obj.get("exposedUrls") is not None
                    else None
                ),
                "relatedUrls": (
                    RelatedUrlsDefaults.from_dict(obj["relatedUrls"])
                    if obj.get("relatedUrls") is not None
                    else None
                ),
            }
        )
        return _obj
