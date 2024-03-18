#!/usr/bin/env python3
"""Define async module"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """function that  return the list of delays (float values)"""
    delay_time: List[float] = []
    for i in range(n):
        time = random.uniform(0, max_delay)
        await asyncio.sleep(time)
        delay_time.append(time)
    return sorted(delay_time)
