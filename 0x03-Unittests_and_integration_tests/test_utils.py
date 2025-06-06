#!/usr/bin/env python3

"""
Parameterize a unit test
"""


"""
Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_utils.py


"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Tuple, Union


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
        """test_access_nested_map: tests the result returned by the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map=nested_map, path=path), result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Checks if the exception KeyError was raised when a key isn't found in dict"""

        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)
