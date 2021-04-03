# coding: utf-8
from report_demo.constans import f
from report_demo.utils.yaml_handle import ReadHandle


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
    """获取sql语句"""

    @staticmethod
    def get_sql_sentence(filename):
        abs_sql_path = f.yamlFile + filename
        module_sql_data = ReadHandle(abs_sql_path).yaml_files_read()

        return module_sql_data
