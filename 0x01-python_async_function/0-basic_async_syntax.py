#!/usr/bin/env python3
from random import uniform
import asyncio

'''
An Asynchronous coroutine
'''


async def wait_random(max_delay=10):
    '''
    waits for a random delay between 0 and max_delay
    included and float value) seconds and eventually
    returns it.
    '''

    value = uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
