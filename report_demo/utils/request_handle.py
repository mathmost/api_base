# coding: utf-8
import requests


class RequestHandle:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

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


