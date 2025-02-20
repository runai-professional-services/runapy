"""
Async REST client implementation.
"""

import io
import json
import aiohttp
import aiohttp_retry
from typing import Optional

from runai.configuration import Configuration
from runai.exceptions import ApiException


class RESTResponse(io.IOBase):
    """Wrapper for aiohttp response."""

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = None

    async def read(self):
        """Read response data."""
        if self.data is None:
            self.data = await self.response.read()
        return self.data

    def getheaders(self):
        """Returns a CIMultiDictProxy of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class AsyncRESTClientObject:
    """Async REST client for making HTTP requests."""

    def __init__(self, configuration: Optional[Configuration] = None):
        """Initialize the REST client with configuration."""
        self.configuration = configuration or Configuration()
        self.pool_manager = None
        self.retry_client = None
        self.maxsize = configuration.pool_maxsize if configuration else 4
        self.retries = configuration.retries
        self.proxy_url = configuration.proxy_url
        self.proxy_headers = configuration.proxy_headers
        self.ssl_context = configuration.ssl_context

    async def close(self) -> None:
        if self.pool_manager:
            await self.pool_manager.close()
        if self.retry_client:
            await self.retry_client.close()

    async def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        timeout=None,
    ):
        """Make an HTTP request using aiohttp.

        Args:
            method: HTTP method
            url: URL to request
            headers: Request headers
            body: Request body
            post_params: Form parameters
            timeout: Request timeout in seconds
        """
        if not self.pool_manager:
            self.pool_manager = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(ssl=self.ssl_context, limit=self.maxsize)
            )

        # Convert timeout to aiohttp format
        if timeout:
            if isinstance(timeout, (int, float)):
                timeout = aiohttp.ClientTimeout(total=timeout)
            elif isinstance(timeout, tuple) and len(timeout) == 2:
                timeout = aiohttp.ClientTimeout(connect=timeout[0], total=timeout[1])

        # Prepare request parameters
        request_kwargs = {
            "headers": headers,
            "timeout": timeout,
            "ssl": self.ssl_context,
        }

        if body is not None:
            request_kwargs["json"] = body
        elif post_params:
            request_kwargs["data"] = post_params

        if self.proxy_url:
            request_kwargs["proxy_url"] = self.proxy_url
            if self.proxy_headers:
                request_kwargs["proxy_headers"] = self.proxy_headers

        # Make request
        response = await self.pool_manager.request(method, url, **request_kwargs)

        return RESTResponse(response)
