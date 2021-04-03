# coding: utf-8
import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# allure报告
# 本地项目可以写死，如果有部署则填写ip地址即可
resultDir = os.path.join(base_dir, r'allure_demo\report_demo\reports\result_dir')


class BaseConfig:
    """通用配置变量"""
    # base_url
    BASE_URL = "http://www.niuinfo.com"
    # mobile、user_name
    MOBILE = 17802156775
    USER_NAME = "test"
    # password
    PASSWORD = 123456
    # email（发件人邮箱以及授权码、发送邮件标题、发送邮件的html地址）
    USE_EMAIL = False
    SENDER_EMAIL = "13764502352@163.com"
    SENDER_PASSWORD = "SSMIVXVXDARXKHHF"
    SEND_SUB_TITLE = "本次接口自动化执行完成"
    SEND_EMAIL_HTML = r'{}\index.html'.format(resultDir)
    # mysql
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_LIBRARY = "dn"
    # redis
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
    RECEIVER_EMAIL = "1196010587@qq.com"
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


config_map = {
    "dev": DevConfig,
    "pre": PreConfig,
    "master": MasterConfig
}
