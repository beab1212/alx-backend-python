#!/usr/bin/env python3
""" Let's excute multiple coroutines at the same time with async """
import asyncio


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ Create wait_random task n times.
        Args:
            n (int): no of times for task
            max_delay (int): maximum delay for each task
        Return:
            list of float for each task
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
