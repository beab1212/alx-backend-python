#!/usr/bin/env python3
""" Measure the runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure run time.
        Args:
            n (int): no of times for task
            max_delay (int): maximum delay for each task
        Return:
            runtime time in second
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = (time.perf_counter() - s) / n
    return elapsed
