# coding: utf-8
import yaml
from pathlib2 import Path


class ReadHandle:
    """读取yaml文件"""

    def __init__(self, filepath):
        self.filepath = filepath

    @staticmethod
    def file_is_exist(file_path):
        """判断文件是否存在"""
        if not Path(file_path).exists():
            raise FileNotFoundError("请确认路径或文件是否正确！")
        return file_path

    def yaml_files_read(self):
        """the first methods"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            r = yaml.safe_load_all(f)
            for i in r:
                return i

    def get_yaml_data(self) -> dict:
        """the second methods"""
        file = self.file_is_exist(self.filepath)
        if Path(file).suffix == ".yaml":
            with open(file, 'r', encoding='utf-8-sig') as f:
                file_data = f.read()
            return yaml.safe_load(file_data)
        else:
            raise RuntimeError("The file format must be yaml")


class RwYaml(object):
    """读写yaml文件"""

    def __init__(self, file_name):
        self.y = yaml
        self.file = file_name  # yaml文件绝对路径

    # 读取
    def read_yaml_all(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            return self.y.load(f, Loader=self.y.FullLoader)

    # 写入
    def write_yaml(self, nb, key, value):
        data = {nb: {key: value}}
        old_data = self.read_yaml_all()
        if nb in old_data:
            old_data[nb][key] = value
            with open(self.file, 'w', encoding='utf-8') as f:
                self.y.dump(old_data, f)
                print('写入成功：%s' % old_data)
        else:
            with open(self.file, 'a', encoding='utf-8') as f:
                self.y.dump(data, f)
                print('写入成功：%s' % data)

    # 读取节点下面key的值
    def read_yaml_value(self, nb, key):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = self.y.load(f, Loader=self.y.FullLoader)
            try:
                if nb in data.keys():
                    return data[nb][key]
                else:
                    print('节点: %s不存在！' % nb)
            except KeyError as e:
                print('key：%s不存在！' % key)
