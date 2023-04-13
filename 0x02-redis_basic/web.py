#!/usr/bin/env python3
"""web module
"""
from functools import wraps
from typing import Callable

import redis
import requests
from requests import Response

_redis = redis.Redis(host="localhost", port=6379, db=0)


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
        _redis.incr(f"count:{args[0]}")

        html = _redis.get("html-cache:{args[0]}")
        if html is not None:
            return html.decode("utf-8")
        html = method(*args, **kwargs)
        _redis.setex(f"html-cache:{args[0]}", 10, html)
        return html

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


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
