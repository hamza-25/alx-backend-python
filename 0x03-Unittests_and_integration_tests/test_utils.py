#!/usr/bin/env python3
"""Test Module
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Union, Sequence, Mapping


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


if __name__ == '__main__':
    unittest.main()
