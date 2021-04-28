# coding: utf-8
import pytest
import allure
from basic_frame.constans import apibase
from basic_frame.pages.funcs import login
from basic_frame.utils.log_handle import logger


# noinspection PyUnusedLocal
@allure.feature("login_module")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.run(order=1)
class TestLoginRunner:
    """登录模块"""

    @allure.story("login")
    @pytest.mark.login
    @pytest.mark.parametrize('case', apibase.login_data)
    def test_login(self, case, something):
        data = apibase.login_data.get(case)
        mobile = data.get("mobile")
        password = data.get("password")
        logger.info("login_mobile: {}, login_password: {}".format(mobile, password))
        res = login(mobile, password)

        # 设置全局变量、环境变量
        apibase.globals_set('global_login_res', res.json())
        apibase.globals_set('global_login_res_1', 200000)
        apibase.globals_set('global_login_res_2', 1200000)
        apibase.globals_set('global_login_res_3', 3200000)

        apibase.locals_set('local_login_status_code', res.status_code)
        apibase.locals_set('local_login_test1', res.status_code + 1000000)
        apibase.locals_set('local_login_test2', res.status_code + 1800000)
        apibase.locals_set('local_login_test3', res.status_code + 3600000)

        # 断言
        apibase.assert_handle.assert_equal_value(res.status_code, 200)

    @pytest.mark.fix_data(42)
    def test_fix(self, fix_name, something):
        apibase.assert_handle.assert_equal_value(fix_name, 42)
