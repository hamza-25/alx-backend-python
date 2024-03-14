#!/usr/bin/env python3
"""Math Module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """mrthod that sum float values in a list"""
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
