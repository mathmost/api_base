# coding: utf-8
import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# allure报告
# 本地项目可以写死，如果有部署则填写ip地址即可
resultDir = os.path.join(base_dir, r'allure_demo\report_demo\reports\result_dir')


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
    USE_WRITE_VARIABLE = True
    # email（发件人邮箱以及授权码、发送邮件标题、发送邮件的html地址）
    USE_EMAIL = False
    SENDER_EMAIL = "XXXXXX@163.com"
    SENDER_PASSWORD = "SSMIVXVDWDWDWDAXXXXXDARXKHHF"
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
    RECEIVER_EMAIL = "1196010XXXXXX@qq.com"
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

# config类指向
config_map = {
    "dev": DevConfig,
    "pre": PreConfig,
    "master": MasterConfig,
    "customerA": CustomerA_Config,
    "customerB": CustomerB_Config,
    "customerC": CustomerC_Config
}

# 执行环境的配置信息 dev, pre, master
# 如果需要添加客户信息，则继续添加类继承BaseConfig以及在config_map中添加指向即可
op_environment = "customerB"
app_cof = config_map.get(op_environment)
