# coding: utf-8
import os
from pathlib2 import Path


class GetFilePath:
    """文件操作类"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.file_paths = []
        self.file_names = []

    @staticmethod
    def file_absolute_path(rel_path):
        """
        通过文件相对路径，返回文件绝对路径
        :param rel_path: 相对于项目根目录的路径，如data/check_lib.yaml
        """
        current_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
        file_path = os.path.join(current_path, rel_path)
        return file_path

    def current_dir_files(self, path):
        """
        获取当前目录下的所有文件的绝对路径以及文件名
        :param path: 文件的绝对路径
        """
        # 获取当前绝对路径下的所有目录及文件
        cur_files = os.listdir(path)
        for file in cur_files:
            file_path = os.path.join(path, file)
            # 如果是文件夹则循环调用
            if os.path.isdir(file_path):
                self.current_dir_files(file_path)
            # 保存文件路径及文件名
            elif os.path.isfile(file_path):
                self.file_paths.append(file_path)
                self.file_names.append(file)

        return self.file_paths, self.file_names
