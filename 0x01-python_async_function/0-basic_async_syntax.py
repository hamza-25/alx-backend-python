#!/usr/bin/env python3
"""Define async module"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """func that print time after delay of time """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
