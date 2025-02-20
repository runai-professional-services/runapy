import io
import json
import re
import ssl

import urllib3

from runai.exceptions import ApiException, ApiValueError

RESTResponseType = urllib3.HTTPResponse


class RESTResponse(io.IOBase):

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = None

    def read(self):
        if self.data is None:
            self.data = self.response.data
        return self.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class RESTClientObject:
    """REST client for making HTTP requests."""

    def __init__(self, configuration) -> None:
        """Initialize REST client with configuration.

        Args:
            configuration: Configuration instance
        """
        # Set up SSL/TLS configuration
        cert_reqs = ssl.CERT_REQUIRED if configuration.verify_ssl else ssl.CERT_NONE

        # Build pool arguments
        pool_args = {
            "cert_reqs": cert_reqs,
            "ca_certs": configuration.ssl_ca_cert,
            "cert_file": configuration.cert_file,
            "key_file": configuration.key_file,
            "maxsize": configuration.pool_maxsize,
        }

        if configuration.retry_enabled:
            pool_args["retries"] = configuration.get_retry_object()

        if configuration.proxy_server_name:
            pool_args["server_hostname"] = configuration.proxy_server_name

        # Initialize the appropriate pool manager
        if configuration.proxy_url:
            pool_args["proxy_url"] = configuration.proxy_url
            pool_args["proxy_headers"] = configuration.proxy_headers
            self.pool_manager = urllib3.ProxyManager(
                num_pools=configuration.pool_size, **pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=configuration.pool_size, **pool_args
            )

        # Store configuration for later use
        self.configuration = configuration

    def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, float)):
                timeout = urllib3.Timeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1]
                )

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ["POST", "PUT", "PATCH", "OPTIONS", "DELETE"]:

                # no content type provided or payload is json
                content_type = headers.get("Content-Type")
                if not content_type or re.search("json", content_type, re.IGNORECASE):
                    request_body = None
                    if body is not None:
                        request_body = body
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=request_body,
                        timeout=timeout,
                        headers=headers,
                        preload_content=False,
                    )
                elif content_type == "application/x-www-form-urlencoded":
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=post_params,
                        encode_multipart=False,
                        timeout=timeout,
                        headers=headers,
                        preload_content=False,
                    )
                elif content_type == "multipart/form-data":
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers["Content-Type"]
                    # Ensures that dict objects are serialized
                    post_params = [
                        (a, json.dumps(b)) if isinstance(b, dict) else (a, b)
                        for a, b in post_params
                    ]
                    r = self.pool_manager.request(
                        method,
                        url,
                        fields=post_params,
                        encode_multipart=True,
                        timeout=timeout,
                        headers=headers,
                        preload_content=False,
                    )
                # Pass a `string` parameter directly in the body to support
                # other content types than JSON when `body` argument is
                # provided in serialized form.
                elif isinstance(body, str) or isinstance(body, bytes):
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=body,
                        timeout=timeout,
                        headers=headers,
                        preload_content=False,
                    )
                elif headers["Content-Type"] == "text/plain" and isinstance(body, bool):
                    request_body = "true" if body else "false"
                    r = self.pool_manager.request(
                        method,
                        url,
                        body=request_body,
                        preload_content=False,
                        timeout=timeout,
                        headers=headers,
                    )
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(
                    method,
                    url,
                    fields={},
                    timeout=timeout,
                    headers=headers,
                    preload_content=False,
                )
        except urllib3.exceptions.SSLError as e:
            msg = "\n".join([type(e).__name__, str(e)])
            raise ApiException(status=0, reason=msg)

        return RESTResponse(r)
