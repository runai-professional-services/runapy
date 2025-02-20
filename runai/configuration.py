"""
Configuration module for the Run:AI API client.

This module provides configuration settings for the Run:AI API client,
Including authentication, connection pooling, timeouts, retry, proxy, SSL/TLS, and other HTTP settings.
"""

import os
import re
import urllib3
import logging
import ssl

from typing import Optional


class Configuration:
    """Configuration class for Run:AI API client.

    ### Parameters:
        client_id: Run:ai application client name
        client_secret: Run:ai application client secret
        bearer_token: Bearer CLIv2 token for user authentication
        runai_base_url: Base URL for Run:AI API
        pool_maxsize: Maximum number of connections to keep in pool
        pool_size: Initial number of connections in pool
        retry_enabled: Whether to enable request retries
        retry_max_retries: Maximum number of retry attempts
        retry_backoff_factor: Exponential backoff factor between retries
        proxy_url: URL for proxy server
        proxy_headers: Additional headers for proxy
        proxy_server_name: SNI hostname for TLS connections
        verify_ssl: Whether to verify SSL certificates
        ssl_ca_cert: Path to CA certificate file
        cert_file: Path to client certificate file
        key_file: Path to client key file
        auto_refresh_token: Whether to auto refresh token before expiry
        token_refresh_margin: Seconds before expiry to refresh token
        debug: Enable debug logging
        logger: Custom logger instance
    """

    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        bearer_token: str = None,
        runai_base_url: str = None,
        verify_ssl: bool = True,
        ssl_ca_cert: str = None,
        cert_file: str = None,
        key_file: str = None,
        pool_maxsize: int = 4,
        pool_size: int = None,
        retry_enabled: bool = True,
        retry_max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
        proxy_url: str = None,
        proxy_headers: dict = None,
        proxy_server_name: str = None,
        auto_refresh_token: bool = True,
        token_refresh_margin: int = 60,
        debug: bool = False,
        logger: logging.Logger = None,
    ):
        if bearer_token and (client_id or client_secret):
            raise ValueError(
                "Cannot provide both bearer_token and client credentials (client_id/client_secret)"
            )

        # Set up logger
        self.logger = logger or self._setup_logger(debug)

        # Base API Settings
        self.runai_base_url = self._ensure_valid_url(runai_base_url)
        self.client_id = client_id
        self.client_secret = client_secret
        self.bearer_token = bearer_token
        self.auto_refresh_token = auto_refresh_token
        self.token_refresh_margin = token_refresh_margin

        # Connection Pool Settings
        self.pool_maxsize = pool_maxsize
        self.pool_size = pool_size if pool_size is not None else pool_maxsize

        # Retry Settings
        self.retry_enabled = retry_enabled
        self.retry_max_retries = retry_max_retries
        self.retry_backoff_factor = retry_backoff_factor
        self.retries = retry_max_retries if retry_enabled else None
        self.retry_status_forcelist = [401, 429, 500, 502, 503, 504]
        self.retry_allowed_methods = ["UPDATE", "GET", "PUT", "DELETE", "POST"]

        # SSL Settings
        self.verify_ssl = verify_ssl
        self.ssl_ca_cert = ssl_ca_cert
        self.cert_file = cert_file
        self.key_file = key_file

        # Create SSL context if we have any SSL settings
        if ssl_ca_cert or (cert_file and key_file):
            self.ssl_context = ssl.create_default_context()
            if ssl_ca_cert:
                self.ssl_context.load_verify_locations(ssl_ca_cert)
            if cert_file and key_file:
                self.ssl_context.load_cert_chain(cert_file, key_file)
        else:
            self.ssl_context = False

        # Proxy Settings
        self.proxy_url = proxy_url
        self.proxy_headers = proxy_headers
        self.proxy_server_name = proxy_server_name

        # Logging Settings
        self.debug = debug

        # Validate SSL paths if provided
        self._validate_ssl_paths()

        if bearer_token:
            self.auto_refresh_token = False  # Bearer tokens cannot be refreshed
            self.token_refresh_margin = 0

    def _ensure_valid_url(self, url: Optional[str]) -> Optional[str]:
        """Ensure URL is valid and strip trailing slashes.

        Args:
            url: URL to validate

        Returns:
            Validated URL without trailing slashes
        """
        if url:
            return re.sub(r"/+$", "", url)
        return url

    def _validate_ssl_paths(self) -> None:
        """Validate that SSL certificate paths exist if provided."""
        ssl_files = [
            ("ssl_ca_cert", self.ssl_ca_cert),
            ("cert_file", self.cert_file),
            ("key_file", self.key_file),
        ]
        for name, path in ssl_files:
            if path and not os.path.exists(path):
                raise ValueError(f"SSL {name} file not found: {path}")

    def _setup_logger(self, debug: bool) -> logging.Logger:
        """Setup a logger instance.

        Args:
            debug: Enable debug logging

        Returns:
            Logger instance
        """
        # Set urllib3 logger level to only show warnings and above
        urllib3_logger = logging.getLogger("urllib3")
        urllib3_logger.setLevel(logging.WARNING)

        # Setup our logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG if debug else logging.INFO)

        # Only add handler if logger doesn't already have handlers
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
            )
            logger.addHandler(handler)

        return logger

    def get_retry_object(self) -> urllib3.Retry:
        """Get configured retry object.

        Returns:
            urllib3.Retry object configured with current settings
        """
        if not self.retry_enabled:
            return None

        return urllib3.Retry(
            total=self.retry_max_retries,
            backoff_factor=self.retry_backoff_factor,
            status_forcelist=self.retry_status_forcelist,
            allowed_methods=self.retry_allowed_methods,
        )
