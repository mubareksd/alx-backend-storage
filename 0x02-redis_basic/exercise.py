#!/usr/bin/env python3
"""exercise module
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self):
        """init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store function

        Args:
            data[str, bytes, int, float]: value

        Returns:
            str: key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return str(key)
