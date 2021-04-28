# coding: utf-8
import allure
from basic_frame.constans import *


@allure.step("调用登陆接口")
def login(mobile, password, env_url=None):
    """
    调用登陆接口
    :param mobile: 手机号
    :param password: 密码
    :param env_url: 访问地址
    """
    login_param = apibase.request_param.login_map
    if env_url:
        url = env_url + login_param.get('login')
    else:
        url = app_cof.BASE_URL + login_param.get('login')
    data = {
        "mobile": mobile,
        "password": password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    login_res = apibase.request_handle.required('post', url=url, data=data, headers=headers)

    return login_res


def something():
    ...
