#!/usr/bin/env python3
"""web module
"""
import redis
import requests
from functools import wraps
from requests import Response
from typing import Callable


_redis = redis.Redis()


def count(method: Callable) -> Callable:
    """count function
    Args:
        method[Callable]:
    returns:
        Callable:
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper decorated function"""
        url = args[0]
        cached = _redis.get("cache:{}".format(url))
        if cached:
            return cached.decode("utf-8")
        _redis.incr("count:{}".format(url))
        _redis.set("cache:{}".format(url), method(url))
        _redis.expire("cache:{}".format(url), 10)
        return method(*args, **kwargs)

    return wrapper


@count
def get_page(url: str) -> str:
    """get_page function
    Args:
        url[str]:
    Returns:
        str:
    """
    response: Response = requests.get(url)
    return response.text
