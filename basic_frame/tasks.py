# coding: utf-8
import os
import time
from celery import Celery
from basic_frame.constans import (allure_command, app_cof, apibase)


broker = 'redis://{}:{}'.format(app_cof.REDIS_HOST, app_cof.REDIS_PORT)
app = Celery('tasks', broker=broker)
app.conf.update(
    CELERY_RESULT_BACKEND=broker,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ENABLE_UTC=True
)

"""后置脚本: 异步任务处理"""


# allure报告
@app.task
def execute_command():
    time.sleep(1)
    os.system(allure_command)


# 发送邮件
@app.task
def email_send(sender, receive, pass_wd, sub_title, content, send_type, file_path: list, file_name: list):
    apibase.email.for_email(sender, receive, pass_wd, sub_title, content, send_type, file_path, file_name)
