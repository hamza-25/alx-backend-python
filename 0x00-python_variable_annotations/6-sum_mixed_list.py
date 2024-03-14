#!/usr/bin/env python3
"""Math Module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """method that sum float and int values in a list"""
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
