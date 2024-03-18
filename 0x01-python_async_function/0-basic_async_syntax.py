#!/usr/bin/env python3
"""
This is a task to familiarize myself with async syntax in python
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''function that returns random delay time after that period has elasped'''
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
