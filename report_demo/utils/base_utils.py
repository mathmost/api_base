# coding: utf-8
from report_demo.constans import f
from report_demo.utils.yaml_handle import ReadHandle


# noinspection PyUnusedLocal
def singleton(cls, *args, **kwargs):
    """单例"""
    instance = {}

    def _instance():
        if cls not in instance:
            instance[cls] = cls(*args, *kwargs)
        return instance[cls]
    return _instance


class GetKeys:
    """获取全部字典的key，包含列表中包含的字典"""

    @staticmethod
    def get_all_key(data):
        """
        :param data: {}, [{}]
        :return: key组成的列表，未去重
        """
        all_key = []

        # noinspection PyShadowingNames
        def in_key(data):
            if isinstance(data, list):
                for item in data:
                    in_key(item)
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, (list, dict)):
                        in_key(value)
                    all_key.append(key)

            return all_key

        return in_key(data)


class SqlData:
    """获取yaml文件下的sql语句、用例数据等"""

    @staticmethod
    def get_sql_sentence(filename):
        abs_sql_path = f.yamlFile + filename
        module_sql_data = ReadHandle(abs_sql_path).yaml_files_read()

        return module_sql_data


class SqlResult:
    """对sql查询的结果进行判断, 可以指定index获取返回结果"""

    @staticmethod
    def get_res(sql_query_res, index=None):
        if len(sql_query_res) != 0:
            return sql_query_res[0] if index in (0, None) or type(index) != int else sql_query_res[index]
        else:
            raise Exception("res is empty")

