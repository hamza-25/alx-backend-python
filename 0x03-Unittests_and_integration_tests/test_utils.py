#!/usr/bin/env python3
"""Test Module
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized # type: ignore
from typing import Union, Sequence, Mapping


class TestAccessNestedMap(unittest.TestCase):
    """Define TestAccessNestedMap Class
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, x: Mapping, y: Sequence, expected: Union[int, dict[str, int]])-> None:
        """method that test return value of mapping
        """
        result = access_nested_map(x, y)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a", "b"), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(self, x: Mapping, y: Sequence, expected: Union[int, dict[str, int]])-> None:
        """method that raise Error
        """
        self.assertRaises(KeyError)


if __name__ == '__main__':
    unittest.main()
