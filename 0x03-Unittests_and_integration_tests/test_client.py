#!/usr/bin/env python3
"""
"""
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Define TestGithubOrgClient class
    """
    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, expected: Dict,
                 mock_get_json: MagicMock) -> None:
        """test method org in GithubOrgClient class
        """
        mock_get_json.return_value = MagicMock(return_value=expected)
        github_repo = GithubOrgClient(org)
        self.assertEqual(github_repo.org(), expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """test public repo url in GithubOrgClient
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos"
                }
            gith_repo = GithubOrgClient("google")._public_repos_url
            self.assertEqual(gith_repo,
                             "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
