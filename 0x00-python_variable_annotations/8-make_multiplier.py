#!/usr/bin/env python3
"""Math Module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """method that
    returns a function that multiplies a float by multiplier"""
    return lambda new_value: new_value * multiplier
