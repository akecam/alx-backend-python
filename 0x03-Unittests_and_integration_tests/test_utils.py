#!/usr/bin/env python3

"""
Parameterize a unit test
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Tuple, Union
from unittest.mock import Mock, patch
from utils import get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap: Test the function access_nested_map
    nested_map={"a": {"b": 2}}, path=("a", "b")
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Mapping, path, result):
        """
        test_access_nested_map:
        tests the result returned by the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Checks if the exception KeyError
        was raised when a key isn't found in dict
        """

        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    """
    Test the get_json function
    """

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """
        Test the get_json function using mock
        """

        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:

            with self.subTest(url=test_url):
                mock_response = Mock()            
                mock_response.json.return_value = test_payload
                mock_get.return_value = mock_response

                result = get_json(test_url)
                self.assertEqual(result, test_payload)
                mock_get.assert_called_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the Memoization function in utils
    """

    def test_memoize(self):
        """
        test_memoize: test that a result was cache'd
        """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()

        with patch.object(test_class, "a_method") as test_memoize:

            test_class.a_property
            test_class.a_property

            test_memoize.assert_called_once()


if __name__ == "__main__":
    unittest.main()
