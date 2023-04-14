#!/usr/bin/env python3
"""web module
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """count_url_access function

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(url):
        """wrapper decorated function

        Returns:
            _type_: _description_
        """
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """get_page function

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    res = requests.get(url)
    return res.text
