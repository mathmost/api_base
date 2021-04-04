# coding: utf-8
import pytest
import allure
from report_demo.pages.funcs import login
from report_demo.constans import case_data


# noinspection PyUnusedLocal
@allure.feature("test_sql_module")
@allure.severity(allure.severity_level.NORMAL)
class TestSqlRunner:
    """测试数据库校验"""

    @allure.story("sql_module")
    @pytest.mark.mysql
    def test_mysql(self, something):
        res = login(17802156123, 123456)
        # 根据手机号查询数据库
        user_query_res = case_data.db.select_mysql(case_data.sql_data.get('user_name').format(17802156123))

        # 断言
        case_data.assert_handle.assert_equal_value(res.status_code, 200)
        # 分别获取: 数据库返回的username以及接口返回的username, 再进行断言
        sql_username, api_username = case_data.sql_res.get_res(user_query_res).get('name'), res.json().get('userName')
        case_data.assert_handle.assert_equal_value(sql_username, api_username)


