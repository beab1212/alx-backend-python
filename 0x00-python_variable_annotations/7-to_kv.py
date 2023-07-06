#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Type-annotated function 'to_kv' tat takes
        Args:
            k (str):
            v (Union[int, float]):
        Returns:
            returns a tuple. The first element of the tuple is the string k.
            The second element is the square of the int/float v.
    """
    return (k, v * v)
