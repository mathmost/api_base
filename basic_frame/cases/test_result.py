# coding: utf-8
import pytest
import allure
from basic_frame.constans import apibase


# noinspection PyUnusedLocal
@allure.feature("get_result_module")
@allure.severity(allure.severity_level.NORMAL)
class TestResult:
    """测试获取测试用例执行结果"""

    @allure.step("test_001")
    @allure.story("get_result_001")
    @pytest.mark.get_result
    def test_001(self, something):
        """
         获取测试用例执行结果: 调用001
        """
        print("test_001_something: ", something)
        apibase.assert_handle.assert_equal_value(1, 0)

    @allure.step("test_002")
    @allure.story("get_result_002")
    @pytest.mark.get_result
    def test_002(self, something):
        """
         获取测试用例执行结果: 调用002
        """
        print("test_002_something: ", something)
        apibase.assert_handle.assert_equal_value(1, 1)
