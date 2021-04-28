# coding: utf-8
from basic_frame.constans import f
import configparser


class IniHandle:
    """读取ini文件"""

    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = f.iniDir
        if node is None:
            self.node = "pytest"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    @staticmethod
    def load_ini(file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf

    def get_value(self, key):
        # 获取节点
        text = self.cf.get(self.node, key)
        return text

    def set_value(self, key, value):
        # 修改数据
        self.cf.set(self.node, key, value)
        self.cf.write(open(f.iniDir, "w+"))
