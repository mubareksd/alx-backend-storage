#!/usr/bin/env python3
""" web module """
import redis
import requests
from functools import wraps
from requests import Response
from typing import Callable


client = redis.Redis()


def url_count(method: Callable) -> Callable:
    """url_count function
    Args:
        method[Callable]:
    returns:
        Callable:
    """

    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper decorated function"""
        url = args[0]
        cache = client.get(f"cache:{url}")
        if cache:
            return cache.decode("utf-8")
        client.incr(f"count:{url}")
        client.setex(f"cache:{url}", 10, method(url))
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
    response: Response = requests.get(url)
    return response.text
