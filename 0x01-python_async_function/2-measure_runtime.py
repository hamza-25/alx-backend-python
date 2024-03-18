#!/usr/bin/env python3
"""Define async module"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function that calculate delay time of async func"""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
