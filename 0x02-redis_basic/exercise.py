#!/usr/bin/env python3
"""exercise"""
import redis
import uuid
from typing import Union, Callable, Optional

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
    
    def get(self, key: str, fn: Optional[Callable] = None):
        """creat get method"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get to int"""
        return self.get(key, fn=int)
    