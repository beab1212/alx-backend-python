#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Type-annotated function 'make_multiplier' that takes
        Args:
            multiplier (float):
        Returns:
            returns a function that  multiplies a float by multiplier.
    """
    def myFunc(num: float) -> float:
        return multiplier * num
    return myFunc
