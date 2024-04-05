#!/usr/bin/env python3
"""Test Module
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Define TestAccessNestedMap Class
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method that test return value of mapping
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a", "b"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """method that raise Error
        """
        with self.assertRaises(expected) as context_error:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Define TestGetJson that fetch json data
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, expected):
        """fetch data api using Mock class
        """
        mock_get_json = Mock()
        mock_get_json.json.return_value = expected
        with patch("requests.get", return_value=mock_get_json):
            response = get_json(url)
            self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
