# -*- encoding: UTF-8 -*-
from report_demo.enentMange.EventManager import *
import time

# 事件名称 新文章
EVENT_ARTICAL = "Event_Artical"


# 事件源 公众号
class PublicAccounts:
    def __init__(self, event_manager):
        self.__eventManager = event_manager

    def write_new_artical(self):
        # 事件对象，写了新文章
        event = Event(type_=EVENT_ARTICAL)
        event.dict["artical"] = u'如何写出更优雅的代码\n'
        # 发送事件
        self.__eventManager.SendEvent(event)
        print(u'公众号发送新文章')


# 监听器 订阅者
class Listener:
    def __init__(self, username):
        self.__username = username

    # 监听器的处理函数 读文章
    def read_artical(self, event):
        print(u'\n%s 收到新文章' % self.__username)
        print(u'正在阅读新文章内容：%s' % event.dict["artical"])


"""测试函数"""


def test():
    listener_1 = Listener("think_room")  # 订阅者1
    listener_2 = Listener("steve")  # 订阅者2

    event_manager = EventManager()

    # 绑定事件和监听器响应函数(新文章)
    event_manager.AddEventListener(EVENT_ARTICAL, listener_1.read_artical)
    event_manager.AddEventListener(EVENT_ARTICAL, listener_2.read_artical)
    event_manager.Start()

    public_acc = PublicAccounts(event_manager)
    while True:
        public_acc.write_new_artical()
        time.sleep(20)


if __name__ == '__main__':
    test()
