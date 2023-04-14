#!/usr/bin/env python3
"""web module
"""
import requests
import redis
from functools import wraps
from typing import Callable

_redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """count_requests function
    """
    @wraps(method)
    def wrapper(url):
        """wrapper function
        """
        cached = _redis.get(f"cached:{url}")
        if cached:
            return cached.decode("utf-8")
        _redis.incr(f"count:{url}")
        _redis.setex(f"cached:{url}", 10, method(url))
        return method(url)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """get_page function
    """
    response = requests.get(url)
    return response.text
