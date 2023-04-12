#!/usr/bin/env python3
"""web module
"""
import redis
from typing import Callable
import requests
from functools import wraps

client = redis.Redis()


def url_count(method: Callable) -> Callable:
    """url_count function"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        client.incr(f"count:{url}")
        cached = client.get(f"{url}")
        if cached:
            return cached.decode("utf-8")
        client.setex(f"{url}, 10, {method(url)}")
        return method(*args, **kwargs)

    return wrapper


@url_count
def get_page(url: str) -> str:
    """get_page function

    Args:
        url[str]:

    Returns:
        str:
    """
    return requests.get(url).text
