#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import requests
import redis
from functools import wraps


redis_conn = redis.Redis()


def count_access(func):
    """track how many times a particular URL
    was accessed in the key"""
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        """wrap the decorated function and return the wrapper"""
        access_count_key = f"count:{url}"
        redis_conn.incr(access_count_key)
        return func(url, *args, **kwargs)
    return wrapper


def cache_content(func):
    """cache the result with an expiration time of 10 seconds"""
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        """wrap the decorated function and return the wrapper"""
        cached_content = redis_conn.get(url)
        if cached_content is not None:
            return cached_content.decode("utf-8")

        content = func(url, *args, **kwargs)

        redis_conn.setex(url, 10, content)

        return content
    return wrapper


@count_access
@cache_content
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    response = requests.get(url)
    return response.text
