#!/usr/bin/env python3
"""Module that declares a redis class and methods"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        """initializes or creates a cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
