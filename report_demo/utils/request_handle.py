# coding: utf-8
import requests
from .base_utils import singleton


@singleton
class RequestHandle:
    """接口请求封装"""

    @staticmethod
    def required(method, url, data=None, headers=None):
        """表单格式"""
        res = ""
        if method == "get":
            res = requests.get(url=url, params=data, headers=headers)
        if method == "post":
            res = requests.post(url=url, data=data, headers=headers)
        return res

    @staticmethod
    def required_json(method, url, data=None, headers=None):
        """json格式"""
        res = ""
        if method == "get":
            res = requests.get(url=url)
        if method == "post":
            res = requests.post(url=url, json=data, headers=headers)
        return res


