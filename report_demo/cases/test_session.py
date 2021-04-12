# coding: utf-8
import pytest
import allure
from report_demo.constans import case_data


# noinspection PyUnusedLocal
@allure.feature("get_after_get_login_session")
@allure.severity(allure.severity_level.NORMAL)
class TestSession:
    """测试获取登陆后的session"""

    @allure.step("get_login_session")
    @allure.story("get_login_session")
    @pytest.mark.get_result
    def test_login_session(self, fix_login_session, something):
        """
         获取测试用例执行结果: 调用001
        """
        print("get_after_get_login_session: ", fix_login_session)
        # 获取login用例中设置的全局变量、局部变量
        print("TestSession获取login用例中设置的全局变量: ", case_data.globals_get('global_login_res'))
        print("TestSession获取login用例中设置的环境变量: ", case_data.locals_get('local_login_status_code'))

        case_data.assert_handle.assert_equal_value(1, 1)
