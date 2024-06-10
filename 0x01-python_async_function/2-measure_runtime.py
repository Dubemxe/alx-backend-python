#!/usr/bin/env python3
'''
Defines a function that measures the execution 
time for the wait random func
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n