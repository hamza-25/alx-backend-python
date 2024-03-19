#!/usr/bin/env python3
"""Define Async Module"""
import asyncio
import random


async def async_generator():
    """function that generate random values 0 to 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
