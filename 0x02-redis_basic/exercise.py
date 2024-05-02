#!/usr/bin/env python3
"""
Writing strings to Redis:
"""

import redis
from typing import Union
import uuid


class Cache:
    def __init__(self, host='localhost', port=6379, db=0) -> None:
        """
        Constructor
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
