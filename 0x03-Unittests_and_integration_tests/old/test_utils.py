#!/usr/bin/env python3
"""
Testing cases for utils.py
"""
from parameterized import parameterized
import unittest
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    utils.access_nested_map test cases
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """
        access_nested_map method test cases
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a", 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Exception) -> None:
        """
        documentation
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
