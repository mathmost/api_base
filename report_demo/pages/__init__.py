# coding: utf-8
from report_demo.utils.base_utils import singleton


@singleton
class RequestParam:
    """模块的URL请求参数，其他模块皆可以仿照"""

    # 登录
    login_map = {
        "login": '/test/user/login?',
    }

    # 需求
    needs_map = {

    }
    ...

