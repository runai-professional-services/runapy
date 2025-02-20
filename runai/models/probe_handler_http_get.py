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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.probe_handler_scheme import ProbeHandlerScheme
from typing import Optional, Set
from typing_extensions import Self


class ProbeHandlerHttpGet(BaseModel):
    """
    Pydantic class model representing An action based on HTTP Get requests..

    Parameters:
        ```python
        path: Optional[str]
        port: Optional[int]
        host: Optional[str]
        scheme: Optional[ProbeHandlerScheme]
        ```
        path: Path to access on the HTTP server, defaults to /.
        port: Number of the port to access on the container.
        host: Host name to connect to, defaults to the pod IP.
        scheme: See model ProbeHandlerScheme for more information.
    Example:
        ```python
        ProbeHandlerHttpGet(
            path='',
                        port=1,
                        host='',
                        scheme='HTTP'
        )
        ```
    """  # noqa: E501

    path: Optional[StrictStr] = Field(
        default=None, description="Path to access on the HTTP server, defaults to /."
    )
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(
        default=None, description="Number of the port to access on the container."
    )
    host: Optional[StrictStr] = Field(
        default=None, description="Host name to connect to, defaults to the pod IP."
    )
    scheme: Optional[ProbeHandlerScheme] = None
    __properties: ClassVar[List[str]] = ["path", "port", "host", "scheme"]

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
        """Create an instance of ProbeHandlerHttpGet from a JSON string"""
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
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict["path"] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict["port"] = None

        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict["host"] = None

        # set to None if scheme (nullable) is None
        # and model_fields_set contains the field
        if self.scheme is None and "scheme" in self.model_fields_set:
            _dict["scheme"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProbeHandlerHttpGet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "path": obj.get("path"),
                "port": obj.get("port"),
                "host": obj.get("host"),
                "scheme": obj.get("scheme"),
            }
        )
        return _obj
