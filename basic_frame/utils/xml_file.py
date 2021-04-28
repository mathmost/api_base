# coding: utf-8
from pathlib2 import Path
from luban_common.base_utils import file_is_exist
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class Xml:
    """xml操作"""

    @staticmethod
    def xml_val(file_path):
        try:
            file = file_is_exist(file_path)
            if Path(file).suffix == ".xml":
                # 打开XML文档
                tree = ET.parse(file)
                # 获得文档根节点
                root = tree.getroot()
                # 获取当前节点标签的所有属性信息，并会以字典形式输出
                result = root.attrib
                return result
            else:
                raise RuntimeError("The file format must be xml")

        except BaseException as e:
            print("解析失败！", str(e))
