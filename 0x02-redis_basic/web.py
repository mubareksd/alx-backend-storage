#!/usr/bin/env python3
"""web module
"""
import redis
import requests
from functools import wraps


_redis = redis.Redis()


def count(method):
    """count function
    Args:
        method[Callable]:
    returns:
        Callable:
    """
    @wraps(method)
    def wrapper(url):
        """wrapper decorated function"""
        url = args[0]
        cache_key = "cache" + url
        cached = _redis.get(cache_key)
        if cached:
            return cached.decode("utf-8")
        _redis.incr("count:{}".format(url))
        _redis.set(cache_key, method(url))
        _redis.expire(cache_key, 10)
        return method(url)
    return wrapper


@count
def get_page(url: str) -> str:
    """get_page function
    Args:
        url[str]:
    Returns:
        str:
    """
    response = requests.get(url)
    return response.text
