#!/usr/bin/env python3
""" The basics of asyncs """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Corotine that takes in an integer
        Args:
            max_delay (int): maximum delay
        Return:
            random float no b/n 0 - max_delay
    """
    delay = random.uniform(0, mx_delay)
    await asyncio.sleep(delay)
    return delay
