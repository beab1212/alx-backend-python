#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Args:
        Return:
            List of float numbers generated from async_generator func
    """
    return [i async for i in async_generator()]
