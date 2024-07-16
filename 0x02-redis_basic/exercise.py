#!/usr/bin/env python3
"""
task 0
"""

import redis
from typing import Union, Optional, Callable
import uuid


class Cache:
    """
    cache class
    """

    def __init__(self) -> None:
        """redis init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn : Optional[Callable]):
        value = self._redis.get(key)
        if value is None:
            return "(nil)"
        if fn is not None:
            print(fn.__class__)
        
    
    def get_str(self, value: bytes, fn: Callable[[bytes], str]) -> str:
        return fn(value)
    
    def get_int(self, value: bytes, fn: Callable[[bytes], int]) -> int:
        return fn(value)
