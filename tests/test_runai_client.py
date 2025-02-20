import unittest
from unittest.mock import Mock

import pytest

from runai.runai_client import RunaiClient


class TestRunaiClient(unittest.TestCase):
    def setUp(self):
        self.api_client = Mock()
        self.client = RunaiClient(self.api_client)

    def test_context_manager(self):
        """Test client as context manager"""
        with RunaiClient(self.api_client) as client:
            self.assertIsInstance(client, RunaiClient)
            self.assertEqual(client.api_client, self.api_client)
        # Verify close was called on exit
        self.api_client.close.assert_called_once()

    def test_close(self):
        """Test client cleanup"""
        self.client.close()
        self.api_client.close.assert_called_once()

    def test_del(self):
        """Test cleanup on deletion"""
        self.client.__del__()
        self.api_client.close.assert_called_once()

    def test_init_no_api_client(self):
        """Test initialization without api_client"""
        with pytest.raises(TypeError):
            RunaiClient()


if __name__ == "__main__":
    unittest.main()
