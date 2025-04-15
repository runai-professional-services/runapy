"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import absolute_import

import datetime
import json
import re
import logging

from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool

from typing import Tuple, Dict, Optional, List
from urllib.parse import quote

from pydantic import BaseModel

from runai import rest, async_rest
from runai.token_refresher import TokenRefresher
from runai.exceptions import ApiException
from runai.api_response import ApiResponse, T as ApiResponseT

RequestSerialized = Tuple[str, str, Dict[str, str], Optional[str], List[str]]


class ApiClient:
    """Generic API client for API communication."""

    def __init__(self, configuration=None):
        self.configuration = configuration
        self.logger = (
            configuration.logger if configuration.logger else logging.getLogger("runai")
        )
        self.default_headers = {}
        self.user_agent = self.generate_user_agent()
        self.rest_client = rest.RESTClientObject(configuration)
        self._token = self._make_token_request()
        self.set_default_header("content-type", "application/json")
        self.set_default_header("authorization", f"Bearer {self._token}")

        if configuration.auto_refresh_token:
            # Token refresh management setup
            self.token_refresher = TokenRefresher(self)

    def _make_token_request(self) -> str:
        """Make the actual token request."""
        self.logger.debug("Generating API token")
        headers = {"Accept": "*/*", "Content-Type": "application/json"}
        data = json.dumps(
            {
                "grantType": "app_token",
                "AppId": self.configuration.client_id,
                "AppSecret": self.configuration.client_secret,
            }
        )
        url = f"{self.configuration.runai_base_url}/api/v1/token"
        self.logger.debug(f"Token request URL: {url}")

        resp = self.rest_client.request(
            method="POST", url=url, body=data, headers=headers
        )
        resp_data = json.loads(resp.read())

        if "accessToken" not in resp_data:
            self.logger.error(f"Failed to get access token. Response: {resp_data}")
            raise ValueError(
                f"Failed to get access token from response. Body={resp_data}"
            )

        return resp_data["accessToken"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self) -> None:
        self.rest_client.pool_manager.clear()

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    @property
    def user_agent(self) -> str:
        """User agent for this API client"""
        return self.default_headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value: str) -> None:
        self.default_headers["User-Agent"] = value

    def generate_user_agent(self) -> str:
        """Generate default User-Agent header."""
        import platform
        from runai import __version__

        return "runai-api-client-python/{version} python/{py} {os}/{arch}".format(
            version=__version__,
            py=platform.python_version(),
            os=platform.system(),
            arch=platform.machine(),
        )

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
    ) -> RequestSerialized:
        """Builds the HTTP request params needed by the request."""

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params, None))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, None)
            for k, v in path_params:
                resource_path = resource_path.replace(
                    "{%s}" % k, quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params:
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params, None)

        # body
        if body:
            body = self.sanitize_for_serialization(body)
            body = json.dumps(body)

        url = self.configuration.runai_base_url + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(query_params, None)
            url += "?" + url_query

        return method, url, header_params, body, post_params

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object."""
        if obj is None:
            return None
        elif isinstance(obj, (str, int, float, bool, bytes)):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, dict):
            return {
                key: self.sanitize_for_serialization(val) for key, val in obj.items()
            }
        elif isinstance(obj, BaseModel):
            return self.sanitize_for_serialization(obj.to_dict())

    def parameters_to_url_query(self, params, collection_formats):
        """Convert parameters to URL query string."""
        new_params: List[Tuple[str, str]] = []
        collection_formats = collection_formats or {}

        for k, v in params.items() if isinstance(params, dict) else params:
            if v is None:
                continue
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)
            if isinstance(v, list):
                v = ",".join(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, str(value)) for value in v)
                else:
                    delimiter = {"ssv": " ", "tsv": "\t", "pipes": "|"}.get(
                        collection_format, ","
                    )
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def parameters_to_tuples(self, params, collection_formats):
        """Convert parameters to list of tuples."""
        new_params = []
        collection_formats = collection_formats or {}

        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, value) for value in v)
                else:
                    delimiter = {"ssv": " ", "tsv": "\t", "pipes": "|"}.get(
                        collection_format, ","
                    )
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def call_api(
        self,
        method,
        resource_path,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ) -> rest.RESTResponse:

        if self.configuration.auto_refresh_token:
            self.token_refresher._check_token_expired()

        method, url, header_params, body, post_params = self.param_serialize(
            method=method,
            resource_path=resource_path,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
        )

        return self._call_api(
            method=method,
            url=url,
            header_params=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
        )

    def _call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ) -> rest.RESTResponse:
        """Makes the HTTP request and handles the response"""

        if self.configuration.debug:
            self.logger.debug(f"Making {method} request to {url}")
            self.logger.debug(f"Headers: {header_params}")
            self.logger.debug(f"Body: {body}")
            self.logger.debug(f"Post params: {post_params}")

        try:
            resp = self.rest_client.request(
                method,
                url,
                headers=header_params,
                body=body,
                post_params=post_params,
                _request_timeout=_request_timeout,
            )
            self.logger.debug(f"Received response: status={resp.status}")
        except ApiException as e:
            self.logger.error(f"API request failed: {str(e)}")
            raise e

        resp.read()
        return self.response_deserialize(resp, {"200": dict})

    def response_deserialize(
        self,
        response_data: rest.RESTResponse,
        response_types_map: Optional[Dict[str, ApiResponseT]] = None,
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object."""

        assert (
            response_data.data is not None
        ), "RESTResponse.read() must be called before passing it to response_deserialize()"

        response_type = response_types_map.get(str(response_data.status))
        if (
            not response_type
            and isinstance(response_data.status, int)
            and 100 <= response_data.status <= 599
        ):
            response_type = response_types_map.get(str(response_data.status)[0] + "XX")

        response_text = None
        return_data = None

        try:
            content_type = response_data.getheader("content-type")
            if content_type:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
                encoding = match.group(1) if match else "utf-8"
            else:
                encoding = "utf-8"

            response_text = response_data.data.decode(encoding)
            return_data = json.loads(response_text) if response_text else None

        finally:
            if not 200 <= response_data.status <= 299:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(
            status_code=response_data.status,
            data=return_data,
            headers=response_data.getheaders(),
        )


class AsyncApiClient(ApiClient):
    """Async API client for asynchronous API communication."""

    def __init__(self, configuration=None):
        super().__init__(configuration)
        self.rest_client = async_rest.AsyncRESTClientObject(configuration)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.rest_client.close()

    async def call_api(
        self,
        method,
        resource_path,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        """Override call_api to execute API calls asynchronously."""
        if self.configuration.auto_refresh_token:
            self.token_refresher._check_token_expired()

        # Serialize parameters and build URL just like the sync client
        method, url, headers, body, post_params = self.param_serialize(
            method, resource_path, None, query_params, header_params, body, post_params
        )

        # Make the async request
        response = await self.rest_client.request(
            method=method,
            url=url,
            headers=headers,
            body=body,
            post_params=post_params,
            timeout=_request_timeout,
        )

        # Read response data first
        await response.read()

        # Then deserialize with response type mapping
        return self.response_deserialize(response, {response.status: dict})


class ThreadedApiClient(ApiClient):
    """
    Threaded API client that wraps API calls in a thread pool for concurrent execution.
    Extends the base ApiClient to provide asynchronous API operations.
    """

    def __init__(self, configuration=None, pool_size=None):
        """
        Initialize the threaded client with optional configuration and pool size.

        Args:
            configuration: Configuration instance
            pool_size: Size of the thread pool. If None, uses the pool size from configuration
        """
        super().__init__(configuration)
        self._pool_size = pool_size or self.configuration.pool_maxsize
        self.pool = ThreadPool(processes=self._pool_size)

    def call_api(self, *args, **kwargs):
        """
        Override call_api to execute API calls in a thread pool.

        Returns:
            Future object representing the asynchronous execution
        """
        return self.pool.apply_async(super().call_api, args=args, kwds=kwargs)

    def close(self):
        """Close the thread pool and cleanup resources."""
        if self.pool:
            self.pool.close()
            self.pool.join()
        super().close()
