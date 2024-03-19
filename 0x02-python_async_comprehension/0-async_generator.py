#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    random_num: float
    for _ in range(10):
        await asyncio.sleep(1)
        random_num = random.random() * 10
        yield random_num