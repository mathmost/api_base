# coding: utf-8
import pytest
import allure
from report_demo.constans import case_data
from report_demo.pages.funcs import login
from report_demo.utils.log_handle import logger


# noinspection PyUnusedLocal
@allure.feature("login_module")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.run(order=1)
class TestLoginRunner:
    """登录模块"""

    @allure.story("login")
    @pytest.mark.login
    @pytest.mark.parametrize('case', case_data.login_data)
    def test_login(self, case, something):
        data = case_data.login_data.get(case)
        mobile = data.get("mobile")
        password = data.get("password")
        logger.info("login_mobile: {}, login_password: {}".format(mobile, password))
        res = login(mobile, password)

        # 设置全局变量、局部变量
        case_data.globals_set('global_login_res', res.json())
        case_data.local_set('local_login_status_code', res.status_code)

        # 断言
        case_data.assert_handle.assert_equal_value(res.status_code, 200)

    @pytest.mark.fix_data(42)
    def test_fix(self, fix_name, something):
        case_data.assert_handle.assert_equal_value(fix_name, 42)
