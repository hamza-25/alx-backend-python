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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """test_public_repos that check repo test
        """
        # payload = {
        #     'repos_url': "https://api.github.com/users/google/repos",
        #     'repos': [
        #         {
        #             "id": 65257748,
        #             "name": "repo1",
        #         },
        #         {
        #             "id": 1126548,
        #             "name": "repo2",
        #         },
        #     ]
        # }
        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = payload["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,) as mock_public_url:

            mock_public_url.return_value = payload["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             [
                    "episodes.dart",
                    "kratu",
                ],
                             )
            mock_public_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
