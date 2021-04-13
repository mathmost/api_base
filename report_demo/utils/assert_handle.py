# coding: utf-8
from .db_service import DBService
from .base_utils import (singleton, GetKeys)
from collections import Counter


@singleton
class Assertion:
    """公共断言方法"""

    @classmethod
    def assert_equal_value(cls, reality_value, expected_value):
        """
        校验等于预期值
        :param reality_value: 实际值
        :param expected_value: 预期值
        :return:
        """
        assert expected_value == reality_value, "实际值: {} != 预期值: {}".format(reality_value, expected_value)

    @classmethod
    def assert_startswith(cls, data, expected_value):
        """
        校验以预期值开头
        :param data: 校验的data数据
        :param expected_value: 预期值
        :return:
        """
        if isinstance(data, str):
            assert data.startswith(expected_value), "没有以预期值: {} 开头".format(expected_value)
        else:
            assert False, '只支持 str 的校验，其余暂不支持'

    @classmethod
    def assert_endswith(cls, data, expected_value):
        """
        校验以预期值结尾
        :param data: 校验的data
        :param expected_value: 预期值
        :return:
        """
        if isinstance(data, str):
            assert data.endswith(expected_value), "没有以预期值: {} 结尾".format(expected_value)
        else:
            assert False, '只支持 str 的校验，其余暂不支持'

    @classmethod
    def assert_in_key(cls, data, key):
        """
        校验字典中存在预期key
        :param data: 响应数据
        :param key: 预期key值
        :return:
        """
        if isinstance(data, (list, dict)):
            assert key in GetKeys().get_all_key(data), "结果中不存在预期为: {} 的数据".format(key)
        else:
            assert False, "{}数据类型不支持".format(type(data))

    @classmethod
    def assert_is_none(cls, reality_value):
        """
        校验是否等于None
        :param reality_value: 实际值
        :return:
        """
        if reality_value is None:
            assert True
        else:
            assert False, "校验值不等于None"

    @classmethod
    def assert_is_empty(cls, reality_value):
        """
        校验值为空，当传入值为None、False、空字符串""、0、空列表[]、空字典{}、空元组()都会判定为空
        :param reality_value: 实际值
        :return:
        """
        if not reality_value:
            assert True
        else:
            assert False, "校验值不为空, 值为: {}".format(reality_value)

    @classmethod
    def assert_list_repetition(cls, lists: list):
        """
        校验列表中是否有重复项
        """
        if isinstance(lists, list):
            repetition = {key: value for key, value in dict(Counter(lists)).items() if value > 1}
            if repetition:
                assert False, '列表中有重复项, 重复项为: {}'.format(repetition)
        else:
            assert False, '传入的数据不是一个list'

    @classmethod
    def assert_mysql_except(cls, expected_value):
        """
        数据库与预期值对比
        :param expected_value: 预期值
        :return:
        """
        db = DBService()
        print("db and expected_value: ", db, expected_value)
        ...


