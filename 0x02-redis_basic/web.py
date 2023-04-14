#!/usr/bin/env python3
"""web module
"""
import redis
import requests
from functools import wraps
from requests import Response
from typing import Callable

_redis = redis.Redis(host='localhost', port=6379, db=0)


def counter(method: Callable) -> Callable:
    """counter function

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper decorated function

        Returns:
            _type_: _description_
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
    """get_page function

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    response: Response = requests.get(url)
    return response.text
