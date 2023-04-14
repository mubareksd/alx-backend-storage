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

    Args:
        method (Callable): method

    Returns:
        Callable: wrapper
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper function

        Returns:
            [type]: wrapper
        """
        url = args[0]
        response = method(*args, **kwargs)
        _redis.incr("count:{}".format(url))
        _redis.setex(url, 10, response)
        return response
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """get_page function

    Args:
        url (str): url

    Returns:
        str: response
    """
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    get_page("http://slowwly.robertomurray.co.uk")
