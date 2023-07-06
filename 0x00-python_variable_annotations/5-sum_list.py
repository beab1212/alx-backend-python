#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Type-annotated function 'sum_list' which tackes
        Args:
            input_list (list[float]):
        Returns:
            returns their sum as float.
    """
    return sum(input_list)
