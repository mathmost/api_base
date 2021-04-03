# coding: utf-8
import allure
from report_demo.constans import *


@allure.step("登录")
def login(mobile, password, env_url=None):
    if env_url:
        url = env_url + '/test/user/login?'
    else:
        url = app_cof.BASE_URL + '/test/user/login?'
    data = {
        "mobile": mobile,
        "password": password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    login_res = case_data.request_handle.required('post', url=url, data=data, headers=headers)

    return login_res


def something():
    ...
