#!/usr/bin/env python3
"""
Module for writing strings to Redis
"""
import sys
from uuid import uuid4
from functools import wraps
from typing import Union, Optional, Callable


import redis


union_of_types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    Add a comment here
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Another comment
        """
        self._redis,incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Another comment here
    """
    key = method.__qualname__
    tmp = "".join([key, ":inputs"])
    temp = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Comment here
        """
        self._redis.rpush(tmp, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(temp, str(res))
        return res

    return wrapper


class Cache:
    """
    Redis Cache class.
    """
    def __init__(self):
        """
        __init__ method to store a Redis instance as
        a private variable named _redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        Generates a random key by use of uuid
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            UnionOfTypes:
        """
        Convert back data
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """
        Get a number
        """
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """
        Get a str
        """
        return self.decode("utf-8")
