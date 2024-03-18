#!/usr/bin/env python3
"""Define async module"""
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function that  return the list of all the delays (float values)"""
    delay_time: List[float] = []
    for i in range(n):
        await asyncio.sleep(random.uniform(0, max_delay))
        delay_time.append(random.uniform(0, max_delay))
    return sorted(delay_time)
