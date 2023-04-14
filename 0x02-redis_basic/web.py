#!/usr/bin/env python3
"""web module
"""
import redis
import requests
from functools import wraps


_redis = redis.Redis()


def count(method):
    """count function
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = _redis.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        _redis.incr(count_key)
        _redis.set(cached_key, html)
        _redis.expire(cached_key, 10)
        return html
    return wrapper


@count
def get_page(url: str) -> str:
    """get_page function
    """
    response = requests.get(url)
    return response.text
