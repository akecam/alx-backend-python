#!/usr/bin/env/python3

"""
Parameterize and patch as decorator
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClint(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected = {"login": org_name, "id": 12345}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org()

        self.assertEqual(result, expected)
        url = "https://api.github.com/orgs/"
        mock_get_json.assert_called_once_with(f"{url}{org_name}")
