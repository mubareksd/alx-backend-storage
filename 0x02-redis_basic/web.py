#!/usr/bin/env python3
""" web module """

from functools import wraps
from typing import Callable

import redis
import requests
from requests import Response

_redis = redis.Redis(host="localhost", port=6379, db=0)


def counter(method: Callable) -> Callable:
    """
    a counter decorator that counts how many times a particular URL was
    accessed. The value is cached in Redis and will expire after 10 seconds
    """

    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        wrapper function
        """
        _redis.incr(f"count:{args[0]}")

        html = _redis.get("html-cache:{args[0]}")
        if html is not None:
            return html.decode("utf-8")
        html = method(*args, **kwargs)
        _redis.setex(f"html-cache:{args[0]}", 10, html)
        return html

    return wrapper


@counter
def get_page(url: str) -> str:
    """
    a function that returns the HTML content of a particular URL
    """
    response: Response = requests.get(url)
    return response.text
