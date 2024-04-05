#!/usr/bin/env python3
"""Test Module
"""
import unittest
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """Define TestMemoize Class
    """
    def test_memoize(self):
        """memoize method that test call once a_property
        """
        class TestClass:
            """Define Test Class
            """
            def a_method(self):
                """ method return 42
                """
                return 42

            @memoize
            def a_property(self):
                """method return a method
                """
                return self.a_method()

        Test_obj = TestClass()
        with patch.object(Test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            rslt1 = mock_method.a_property
            rslt2 = mock_method.a_property

            self.assertEqual(rslt1, 42)
            self.assertEqual(rslt2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
