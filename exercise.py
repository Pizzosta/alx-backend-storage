#!/usr/bin/env python3
"""Module that declares a redis class and methods"""

import redis
from uuid import uuid4


class Cache:
    def __init__(self):
        """creates a cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
