#!/usr/bin/env python3
"""
Writing strings to Redis:
"""

import redis
from typing import Union, Optional, Callable
import uuid


def count_calls(method: Callable) -> Callable:
    """
    count_calls method to count Cache class' method calls
    """
    import functools
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self, host='localhost', port=6379, db=0) -> None:
        """
        Constructor
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        get method
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        get_str method
        """
        return self._redis.get(key, fn=lambda v: v.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        get_int method
        """
        v = self._redis.get(key)
        try:
            v = int(v.decode("utf-8"))
        except Exception:
            return None
        return v
