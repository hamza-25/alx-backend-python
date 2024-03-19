#!/usr/bin/env python3
"""Define Async Module"""
import asyncio
from typing import List
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that will execute async_comprehension four times"""
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return (time() - start_time)
