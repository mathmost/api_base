# coding: utf-8
import pytest
import allure
from report_demo.constans import case_data
from report_demo.pages.funcs import login


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
        user_query = case_data.db.select_mysql(case_data.sql_data.get('user_name').format(17802156123))

        if len(user_query) != 0:
            case_data.assert_handle.assert_equal_value(res.status_code, 200)
            # 分别获取: 数据库返回的username以及接口返回的username, 再进行断言
            sql_username, api_username = user_query[0].get('name'), res.json().get('userName')
            case_data.assert_handle.assert_equal_value(sql_username, api_username)

