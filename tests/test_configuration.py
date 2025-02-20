import os
import unittest
from unittest.mock import Mock, patch
import logging
import urllib3

import pytest

from runai.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://api.run.ai"
        self.client_id = "test-client"
        self.client_secret = "test-secret"
        self.bearer_token = "test-token"

    def test_default_initialization(self):
        """Test configuration with default values"""
        config = Configuration()

        # Check default values
        self.assertIsNone(config.runai_base_url)
        self.assertIsNone(config.client_id)
        self.assertIsNone(config.client_secret)
        self.assertIsNone(config.bearer_token)
        self.assertEqual(config.pool_maxsize, 4)
        self.assertEqual(config.pool_size, 4)
        self.assertTrue(config.retry_enabled)
        self.assertEqual(config.retry_max_retries, 3)
        self.assertEqual(config.retry_backoff_factor, 0.5)
        self.assertIsNone(config.proxy_url)
        self.assertEqual(config.proxy_headers, {})
        self.assertTrue(config.verify_ssl)
        self.assertTrue(config.auto_refresh_token)
        self.assertEqual(config.token_refresh_margin, 60)
        self.assertFalse(config.debug)

    def test_custom_initialization(self):
        """Test configuration with custom values"""
        config = Configuration(
            client_id=self.client_id,
            client_secret=self.client_secret,
            runai_base_url=self.base_url,
            pool_maxsize=10,
            pool_size=5,
            retry_enabled=False,
            proxy_url="http://proxy.local",
            proxy_headers={"User-Agent": "test"},
            verify_ssl=False,
            auto_refresh_token=False,
            token_refresh_margin=120,
            debug=True,
        )

        # Check custom values
        self.assertEqual(config.runai_base_url, self.base_url)
        self.assertEqual(config.client_id, self.client_id)
        self.assertEqual(config.client_secret, self.client_secret)
        self.assertIsNone(config.bearer_token)
        self.assertEqual(config.pool_maxsize, 10)
        self.assertEqual(config.pool_size, 5)
        self.assertFalse(config.retry_enabled)
        self.assertEqual(config.proxy_url, "http://proxy.local")
        self.assertEqual(config.proxy_headers, {"User-Agent": "test"})
        self.assertFalse(config.verify_ssl)
        self.assertFalse(config.auto_refresh_token)
        self.assertEqual(config.token_refresh_margin, 120)
        self.assertTrue(config.debug)

    def test_url_validation(self):
        """Test URL validation and cleanup"""
        # Test trailing slash removal
        config = Configuration(runai_base_url="https://api.run.ai/")
        self.assertEqual(config.runai_base_url, "https://api.run.ai")

        # Test None URL
        config = Configuration(runai_base_url=None)
        self.assertIsNone(config.runai_base_url)

    def test_ssl_path_validation(self):
        """Test SSL certificate path validation"""
        # Test with non-existent paths
        with pytest.raises(ValueError) as exc_info:
            Configuration(ssl_ca_cert="/nonexistent/ca.crt")
        self.assertIn("SSL ssl_ca_cert file not found", str(exc_info.value))

        with pytest.raises(ValueError) as exc_info:
            Configuration(cert_file="/nonexistent/cert.crt")
        self.assertIn("SSL cert_file file not found", str(exc_info.value))

        with pytest.raises(ValueError) as exc_info:
            Configuration(key_file="/nonexistent/key.pem")
        self.assertIn("SSL key_file file not found", str(exc_info.value))

    @patch("logging.getLogger")
    def test_logger_setup(self, mock_get_logger):
        """Test logger setup and configuration"""
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger

        # Test debug mode
        config = Configuration(debug=True)
        mock_logger.setLevel.assert_called_with(logging.DEBUG)

        # Test non-debug mode
        config = Configuration(debug=False)
        mock_logger.setLevel.assert_called_with(logging.INFO)

        # Test custom logger
        custom_logger = logging.getLogger("custom")
        config = Configuration(logger=custom_logger)
        self.assertEqual(config.logger, custom_logger)

    def test_retry_object(self):
        """Test retry object configuration"""
        config = Configuration(
            retry_enabled=True, retry_max_retries=5, retry_backoff_factor=1.0
        )
        retry = config.get_retry_object()

        self.assertIsInstance(retry, urllib3.Retry)
        self.assertEqual(retry.total, 5)
        self.assertEqual(retry.backoff_factor, 1.0)
        self.assertEqual(retry.status_forcelist, [401, 429, 500, 502, 503, 504])
        self.assertEqual(
            retry.allowed_methods, ["UPDATE", "GET", "PUT", "DELETE", "POST"]
        )

        # Test disabled retry
        config = Configuration(retry_enabled=False)
        self.assertIsNone(config.get_retry_object())

    def test_pool_size_validation(self):
        """Test pool size settings"""
        # Test pool_size defaults to pool_maxsize
        config = Configuration(pool_maxsize=8)
        self.assertEqual(config.pool_size, 8)

        # Test custom pool_size
        config = Configuration(pool_maxsize=8, pool_size=4)
        self.assertEqual(config.pool_size, 4)
        self.assertEqual(config.pool_maxsize, 8)

    def test_bearer_token_initialization(self):
        """Test configuration with bearer token"""
        config = Configuration(
            bearer_token=self.bearer_token, runai_base_url=self.base_url
        )

        # Check bearer token is set
        self.assertEqual(config.bearer_token, self.bearer_token)
        self.assertIsNone(config.client_id)
        self.assertIsNone(config.client_secret)

        # Check token refresh is disabled
        self.assertFalse(config.auto_refresh_token)
        self.assertEqual(config.token_refresh_margin, 0)

    def test_bearer_token_with_client_credentials(self):
        """Test that bearer token cannot be used with client credentials"""
        with pytest.raises(ValueError) as exc_info:
            Configuration(
                bearer_token=self.bearer_token,
                client_id=self.client_id,
                client_secret=self.client_secret,
            )
        self.assertIn(
            "Cannot provide both bearer_token and client credentials",
            str(exc_info.value),
        )

        with pytest.raises(ValueError) as exc_info:
            Configuration(bearer_token=self.bearer_token, client_id=self.client_id)
        self.assertIn(
            "Cannot provide both bearer_token and client credentials",
            str(exc_info.value),
        )

        with pytest.raises(ValueError) as exc_info:
            Configuration(
                bearer_token=self.bearer_token, client_secret=self.client_secret
            )
        self.assertIn(
            "Cannot provide both bearer_token and client credentials",
            str(exc_info.value),
        )


if __name__ == "__main__":
    unittest.main()
