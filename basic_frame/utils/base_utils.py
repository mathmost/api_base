# coding: utf-8
import base64
import hashlib
import subprocess
from basic_frame.constans import f
from basic_frame.utils.yaml_handle import ReadHandle


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


def get_str_md5(string):
    """传入一个字符串，返回字符串md5值"""
    if not isinstance(string, str):
        raise TypeError("只支持字符串类型")
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


# noinspection PyIncorrectDocstring
def get_str_sha1(string):
    """sha1 算法加密"""
    if not isinstance(string, str):
        raise TypeError("只支持字符串类型")
    sh = hashlib.sha1()
    sh.update(string.encode('utf-8'))
    return sh.hexdigest()


# noinspection PyIncorrectDocstring
def to_base64(string):
    """传入一个字符串，返回字符串的Base64"""
    if not isinstance(string, str):
        raise TypeError("只支持字符串类型")
    base64_str = base64.b64encode(string.encode("utf-8"))
    return str(base64_str, 'utf-8')


# noinspection PyIncorrectDocstring
def from_base64(string):
    """传入一个Base64，返回字符串"""
    if not isinstance(string, str):
        raise TypeError("只支持字符串类型")
    missing_padding = 4 - len(string) % 4
    if missing_padding:
        string += '=' * missing_padding
    return str(base64.b64decode(string), 'utf-8')


def shell(cmd):
    """cmd命令执行函数"""
    output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o
