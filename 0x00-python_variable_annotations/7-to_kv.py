#!/usr/bin/env python3
"""Math Module
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """method that return square of v as float"""
    return (k, v*v)
