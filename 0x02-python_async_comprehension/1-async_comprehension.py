#!/usr/bin/env python3
"""Define Async Module"""
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that generate random values 0 to 10 and return list"""
    return [number async for number in async_generator()]
