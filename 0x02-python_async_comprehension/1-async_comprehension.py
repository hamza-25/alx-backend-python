#!/usr/bin/env python3
"""Define Async Module"""
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, List[float]]:
    """function that generate random values 0 to 10 and return list"""
    new_list = []
    for i in range(10):
        new_list.append(random.uniform(0, 10))
    return new_list
