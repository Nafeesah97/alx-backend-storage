#!/usr/bin/env python3
"""exercise"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: callable) -> callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def counter(self, *args, **kwargs):
        """increment the counter"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return counter


def call_history(method: Callable) -> Callable:
    '''Tracks tinput and output of a method in a Cache class.
    '''
    @wraps(method)
    def retriver(self, *args, **kwargs) -> Any:
        '''Returns the method's output after storing its inputs and output.
        '''
        in_put = '{}:inputs'.format(method.__qualname__)
        out_put = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_put, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_put, output)
        return output
    return retriver


def replay(method: Callable) -> None:
    """Function to display the history of calls of a particular function."""
    cache_store = getattr(method.__self__, '_redis', None)
    input = f"{method.__qualname__}:inputs"
    output = f"{method.__qualname__}:outputs"

    inputs = cache_store.lrange(input, 0, -1)
    outputs = cache_store.lrange(output, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for args, output in zip(inputs, outputs):
        args_str = args.decode('utf-8')  # Convert bytes to string
        output_str = output.decode('utf-8')  # Convert bytes to string
        print(f"{method.__qualname__}(*{args_str}) -> {output_str}")


class Cache():
    """
    To create cache class

    Method:
        store(data): returns a string.
    """

    def __init__(self):
        """to instantiate"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
