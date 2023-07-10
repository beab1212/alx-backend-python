#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """  Create task_wait_random task n times.
        Args:
            n (int): no of times for task
            max_delay (int): maximum delay for each task
        Return:
            list of float for each task
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
