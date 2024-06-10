#!/usr/bin/env python3
'''Defines a function that returns wait time in seconds'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number in seconds'''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
