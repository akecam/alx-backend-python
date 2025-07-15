#!/usr/bin/env python3

"""
Parameterize and patch as decorator
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
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

    def test_public_repos_url(self):
        """Unit test for _public_repos_url property"""

        expected_url = "https://api.github.com/orgs/test-org/repos"
        test_payload = {"repos_url": expected_url}

        with patch.object(GithubOrgClient, "org", return_value=test_payload):
            client = GithubOrgClient("test-org")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Unit test for public_repos method"""

        # Fake payload returned by mocked get_json
        mock_repo_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        mock_get_json.return_value = mock_repo_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            return_value="https://api.github.com/orgs/test-org/repos",
        ) as mock_url:
            client = GithubOrgClient("test-org")
            result = client.public_repos()
            expected = ["repo1", "repo2", "repo3"]

            self.assertEqual(result, expected)
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()
