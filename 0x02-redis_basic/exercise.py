#!/usr/bin/python3
"""
Writing strings to Redis:
"""
from typing import Any
import redis
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
