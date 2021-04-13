# coding: utf-8
import pytest
from report_demo.utils.yaml_handle import RwYaml
from report_demo.tasks import *
from report_demo.utils.time_handle import get_time
from report_demo.pages.funcs import login
from report_demo.constans import *
from env_cof import op_environment
from _pytest.fixtures import SubRequest
import os

# 运行前将用例失败和成功的变量赋值为0且加入到内存中
# noinspection PyRedeclaration
failNum, successNum = 0, 0


def pytest_addoption(parser):
    """注册ini配置文件的命令行参数"""
    parser.addini('globalConf', help='global configuration')
    # 注册命令行参数
    group = parser.getgroup("testing environment configuration")
    group.addoption("--driver",
                    default=os.getenv("py_test_driver", "chrome"),
                    choices=["chrome", "firefox", "ie"],
                    help="set Browser")
    group.addoption("--env",
                    default=os.getenv("py_test_env", None),
                    help="set testing environment")


@pytest.fixture(scope="session")
def env_conf(pytestconfig):
    """获取lb-env和globalConf环境配置文件"""
    env_conf = pytestconfig.getoption("--env")
    global_conf = pytestconfig.getini("globalConf")
    if env_conf:
        env_conf_stream = ReadHandle(case_data.file_handle.file_absolute_path(env_conf))
        if global_conf:
            global_cof_stream = ReadHandle(case_data.file_handle.file_absolute_path(global_conf))
            return {**env_conf_stream.get_yaml_data(), **global_cof_stream.get_yaml_data()}

        return env_conf_stream.get_yaml_data()
    else:
        raise RuntimeError("Configuration --env not found")


@pytest.fixture(scope="session", autouse=True)
def fix_module():
    """
    全局前后置处理
    根据不同环境执行登录获取session、token（根据业务获取）, 只需要登陆一次
    """
    print("====== start ====== ")
    #  获取session
    # 加载配置类信息登录
    print("执行环境: ", app_cof.BASE_URL)
    print("用户名以及密码: ", app_cof.MOBILE, app_cof.PASSWORD)
    fix_login_res = login(app_cof.MOBILE, app_cof.PASSWORD, env_url=app_cof.BASE_URL)
    res_status, login_res = fix_login_res.status_code, fix_login_res.json()
    ses = ""
    if res_status == 200:
        # 如果需要判断状态则需要获取ifSuccess字段的值
        # if_success = login_res.get('ifSuccess')
        # 获取session
        ses = str(fix_login_res.cookies).split('SESSION=')[1][:36]
        # 写入文件可忽略
        # 获取执行环境
        current_environment = op_environment
        # 写入config.yaml
        rw_handle = RwYaml(f.tokenFile)
        rw_handle.write_yaml(current_environment, "{}_token".format(current_environment), ses)
    yield ses

    # 生成allure报告
    execute_command.delay()
    # 发送邮件(根据不同环境选择收件人)
    print("执行完成, 失败{}个，成功{}个".format(failNum, successNum))
    if app_cof.USE_EMAIL:
        time.sleep(5)
        email_send.delay(app_cof.SENDER_EMAIL,
                         app_cof.RECEIVER_EMAIL,
                         app_cof.SENDER_PASSWORD,
                         "{}({})".format(app_cof.SEND_SUB_TITLE, get_time('date_str_time', 'num')),
                         "失败{}个，成功{}个".format(failNum, successNum),
                         ['html'],
                         [[app_cof.SEND_EMAIL_HTML]],
                         [['report.html']])
    # 全局以及环境变量写入文件
    if app_cof.USE_WRITE_VARIABLE:
        var_handle = RwYaml(f.variableFile)
        var_handle.write_yaml_with_dict(None, case_data.globals_variable)
        var_handle.write_yaml_with_dict("locals", case_data.local_variable)
    print("====== end ======")


@pytest.fixture(scope="session")
def fix_login_session(fix_module):
    """获取登陆后的session"""
    yield fix_module


@pytest.fixture(scope="session")
def global_cache(request):
    """全局缓存，当前执行生命周期有效"""
    return request.config.cache


@pytest.fixture(scope="session")
def fix_login(env_conf, global_cache):
    """根据不同环境执行登录"""
    login_res = login(app_cof.MOBILE, app_cof.PASSWORD, env_url=app_cof.BASE_URL)

    yield login_res


@pytest.fixture
def fix_name(request):
    """
        使用标记将数据传递到夹具
        使用该request对象，固定装置访问应用于测试功能的标记，对数据传递很有用
    """
    marker = request.node.get_closest_marker("fix_data")
    if marker is None:
        data = None
    else:
        data = marker.args[0]

    return data


# 获取测试用例执行结果
# noinspection PyUnusedLocal
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取测试用例执行结果: 钩子
    """
    # 获取钩子方法的调用结果
    outcome = yield
    # 从钩子方法的调用结果中获取测试报告
    rep = outcome.get_result()

    # print('从结果中获取测试报告：', rep)
    # print('从报告中分别获取 node_id: {}, 获取调用步骤: {}, 获取执行结果: {}'.format(rep.nodeid, rep.when, rep.outcome))

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def something(request: SubRequest):
    """
    获取测试用例执行结果: 夹具
    """
    global failNum
    global successNum

    yield

    outcome = request.node.rep_call.outcome
    if outcome == "failed":
        print('用例失败了哦')
        failNum += 1
    elif outcome == "passed":
        print('用例通过了哦')
        successNum += 1

    return outcome
