# coding: utf-8
from env_cof import app_cof
import redis
import os


# 地址路径
class FileDir:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    # 顶层目录
    base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    # 日志文件
    proFile = os.path.join(base_dir, r'report_demo')
    # allure文件
    reportDir = os.path.join(base_dir, r'report_demo\reports')
    if not os.path.exists(reportDir):
        os.mkdir(reportDir)
    results = os.path.join(base_dir, r'report_demo\reports\results')
    # allure报告
    resultDir = os.path.join(base_dir, r'report_demo\reports\result_dir')
    # yaml路径
    yamlFile = os.path.join(base_dir, r'report_demo\cases_data')
    # 登陆后写入和获取的token.yaml文件
    tokenFile = os.path.join(base_dir, r'report_demo\config\token.yaml')
    # pytest.ini文件路径
    iniDir = os.path.join(base_dir, r'pytest.ini')


f = FileDir()

# 生成app_cof实例对象后导入才生效且不可删除ReadHandle包的导入
from report_demo.pages import RequestParam
from report_demo.utils.send_email import EmailSend
from report_demo.utils.db_service import DBService
# noinspection PyUnresolvedReferences
from report_demo.utils.yaml_handle import ReadHandle
from report_demo.utils.file_handle import GetFilePath
from report_demo.utils.request_handle import RequestHandle
from report_demo.utils.assert_handle import Assertion
from report_demo.utils.base_utils import (singleton, SqlData, SqlResult)


# noinspection PyMethodMayBeStatic
@singleton
class CaseData:
    """
    一、使用单例将当前类中的变量以及对象加载到内存中保存为唯一的内存ID

    二、提取所有公共对象，将配置文件做到统一管理，避免:
        1. 用例过多重复读取数据
        2. 数据获取错误时（例如mysql连接失败），每有一个用例则加载一次mysql连接
        3. 在cases.__init__文件时重复增加、修改数据会导致目录混乱，不便于数据管理

    三、可以通过globals_set以及local_set在所有的用例中设置和获取全局/局部变量
    """
    def __init__(self):
        # 全局变量、局部变量
        self.globals_variable = {}
        self.local_variable = {}

    def globals_set(self, key, value):
        """设置全局变量值"""
        self.globals_variable[key] = value

    def local_set(self, key, value):
        """设置局部变量值"""
        self.local_variable[key] = value

    # 公共断言类对象
    assert_handle = Assertion()

    # 文件处理对象
    file_handle = GetFilePath()

    # request请求对象
    request_handle = RequestHandle()

    # request请求数据对象
    request_param = RequestParam()

    # email对象
    email = EmailSend()

    # db: 根据环境允许链接数据库则创建db对象
    print("是否要使用数据库: ", app_cof.USE_MYSQL)
    if app_cof.USE_MYSQL:
        db = DBService

    # redis: 根据环境允许链接数据库则创建redis_store对象
    print("是否使用redis: ", app_cof.USE_REDIS)
    if app_cof.USE_REDIS:
        redis_store = redis.StrictRedis(app_cof.REDIS_HOST, app_cof.REDIS_PORT)

    # 获取sql语句
    # 考虑当前用例的模块并不会有很多，所以将sql语句写在一个文件内，如果有需要可以根据模块分开
    sql_obj = SqlData()
    sql_data = sql_obj.get_sql_sentence(r"\sql_sentence.yaml")

    # 获取sql处理结果
    sql_res = SqlResult()

    # 获取登录模块的用例数据
    path = f.yamlFile + r"\login.yaml"
    login_data = sql_obj.get_sql_sentence(r"\login.yaml")

    # 获取其他模块测试用例数据
    ...


case_data = CaseData()

# 生成allure报告
allure_command = "allure generate {} -o {} --clean".format(f.results, f.resultDir)



