#!/usr/bin/env python3
"""
Writing strings to Redis:
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, bytes,  float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
