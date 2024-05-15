#!/usr/bin/env python3
""" redis"""

import redis
import uuid
from typing import Union


class Cache:
    """ class cach"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: callable = None) -> Union[str, bytes, int, float, None]:
        """ get methode"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)

    def get_str(self, key: str) -> Union[str, None]:
        """ get str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """ get str"""
        return self.get(key, fn=int)
