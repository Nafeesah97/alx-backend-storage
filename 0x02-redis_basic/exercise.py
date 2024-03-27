#!/usr/bin/env python3
"""exercise"""
import redis
import uuid
from typing import Union

class Cache():
    """
    To create cache class

    Method:
        store(data): returns a string.
    """

    def __init__ (self):
        """to instantiate"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
