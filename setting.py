# coding: utf-8
import os

# 以字典定义的全局变量以及局部变量先加载到内存中，方便多环境并行运行，环境变量不冲突
# 全局变量
globals_variable = {}

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# allure报告
# 本地项目可以写死，如果有部署则填写ip地址即可
resultDir = os.path.join(base_dir, r'api_base\report_demo\reports\result_dir')


# noinspection SpellCheckingInspection
class BaseConfig:
    """通用配置变量"""
    # base_url
    BASE_URL = "http://www.base.com"
    # mobile、user_name
    MOBILE = 17802156775
    USER_NAME = "test"
    # password
    PASSWORD = 123456
    # 是否在运行完成后写入变量值
    USE_WRITE_VARIABLE = False
    # email（发件人邮箱以及授权码、发送邮件标题、发送邮件的html地址）
    USE_EMAIL = False
    SENDER_EMAIL = "178@163.com"
    SENDER_PASSWORD = "SSMIVHHF"
    SEND_SUB_TITLE = "本次接口自动化执行完成"
    SEND_EMAIL_HTML = r'{}\index.html'.format(resultDir)
    # mysql
    USE_MYSQL = False
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_LIBRARY = "dn"
    # redis
    USE_REDIS = False
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_NODE = 0
    # mongo
    ...


class DevConfig(BaseConfig):
    """开发环境配置变量"""
    # mobile、username
    MOBILE = 17802156123
    # password
    PASSWORD = 123456
    # email（收件人邮箱）
    RECEIVER_EMAIL = "1196010@qq.com"
    # mysql
    USE_MYSQL = False
    # redis
    USE_REDIS = False
    ...


class PreConfig(BaseConfig):
    """预上线配置变量"""
    # base_url
    BASE_URL = "http://www.pre.com"
    # email（收件人邮箱）
    RECEIVER_EMAIL = ""
    # mysql
    USE_MYSQL = False
    # redis
    USE_REDIS = False
    ...


class MasterConfig(BaseConfig):
    """线上配置变量"""
    # base_url
    BASE_URL = "http://www.master.com"
    # email（收件人邮箱）
    RECEIVER_EMAIL = ""
    # mysql
    USE_MYSQL = False
    # redis
    USE_REDIS = False
    ...


class AddCustomer:
    """自定义客户类，继承BaseConfig"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, customer_config, inheritance_config):
        """
        :param customer_config: 客户类名
        :param inheritance_config: 继承的类名
        """
        self.customer_config = customer_config
        self.inheritance_config = inheritance_config

    def add_customer(self):
        """返回客户类的元类实例"""
        customer = type('{}'.format(self.customer_config), (self.inheritance_config,), {})

        return customer()


class Cus:
    """设置客户类的属性"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    # noinspection PyPep8Naming
    @staticmethod
    def set_customer(customer_config, **kwargs):
        """customer_config: 客户类"""
        CusConfig = AddCustomer(customer_config, BaseConfig).add_customer()
        # 获取客户的类名的属性列表
        attributes = dir(CusConfig)
        # 设置客户类的属性值
        for attribute in attributes:
            if kwargs.get(attribute):
                setattr(CusConfig, attribute, kwargs.get(attribute))

        return CusConfig


# 如果需要重写BaseConfig的数据则需要重新设置customer类的属性值
cus = Cus()
CustomerA_Config = cus.set_customer('CustomerAConfig',
                                    BASE_URL="http://www.basea.com",
                                    MOBILE=13764502512,
                                    PASSWORD=123456)
CustomerB_Config = cus.set_customer('CustomerBConfig',
                                    BASE_URL="http://www.baseb.com",
                                    MOBILE=18012345678,
                                    PASSWORD=123456)
CustomerC_Config = cus.set_customer('CustomerCConfig',
                                    BASE_URL="http://www.basec.com",
                                    MOBILE=18012378945,
                                    PASSWORD=123456)


class Enter:

    def __init__(self):
        self.local = {}
        self.config_map = {
            "dev": DevConfig,
            "pre": PreConfig,
            "master": MasterConfig,
            "customerA": CustomerA_Config,
            "customerB": CustomerB_Config,
            "customerC": CustomerC_Config
        }
        # 客户配置信息
        # op_environment: 执行环境
        # is_use: 是否执行
        # description: 企业描述信息
        # 如果是批量执行，则依次往下执行
        self.enters = {
            "op_environment": "dev",
            "is_use": True,
            "description": "这是一个客户描述信息"
        }
        if self.enters.get('is_use'):
            self.app_cof = self.config_map.get(self.enters.get('op_environment'))
            self.local[self.app_cof.BASE_URL] = {}
        else:
            raise Exception("please running environment")


ent = Enter()
# 执行环境
op_environment = ent.enters.get('op_environment')
# 环境变量
local_variable = ent.local
# app_cof
app_cof = ent.app_cof
