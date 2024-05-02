#!/usr/bin/env python3
"""
implement a get_page function.

"""
import redis
import requests
from typing import Callable
from functools import wraps

r_store = redis.Redis()
"""Redis Instance
"""


def cache_data(method: Callable) -> Callable:
    """
    This decorator caches the output of data retrieval methods.
    """
    @wraps(method)
    def cache_handler(url: str) -> str:
        '''This function handles the caching of the output.
        '''
        r_store.incr(f'count:{url}')
        cached_result = r_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        r_store.set(f'count:{url}', 0)
        r_store.setex(f'result:{url}', 10, result)
        return result
    return cache_handler


@cache_data
def get_page(url: str) -> str:
    """
    This function returns the content of a URL.
    It caches the response of the request
    and keeps track of the request count.
    """
    return requests.get(url).text
