# coding: utf-8
import time
import datetime
import inspect


class TimeHandle:
    """时间处理类"""

    def __init__(self, _time=None):
        self._time = _time

    # 返回datetime
    @staticmethod
    def date_time():
        return datetime.datetime.now()

    # 返回2020-10-01 00:00:00
    @staticmethod
    def date_day():
        today = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
        return today

    # 返回2020-10-01 10:00:00以及10:00:00
    def date_str_time(self, num=None):
        cur_time = self.date_time()
        ts = datetime.datetime.strftime(cur_time, "%Y-%m-%d %H:%M:%S")
        res = ts[:4] if num == 4 else ts[-8:] if num == -1 else ts

        return res

    # 返回当前时间的时间戳 1514583789
    def time_span(self):
        cur_time = self.date_time()
        ts = datetime.datetime.strptime(str(cur_time), "%Y-%m-%d %H:%M:%S.%f")
        cur_ts = ts.timetuple()
        timespan = int(time.mktime(cur_ts))

        return timespan

    # 返回当天剩余时间
    def surplus_time(self, res_type):
        if self.date_str_time(num=-1) != "00:00:00":
            today = self.date_day()
            tomorrow = today + datetime.timedelta(days=1)
            current_time = self.date_time()
            micro_res = (tomorrow - current_time).microseconds  # 获取毫秒
            sec_res = (tomorrow - current_time).seconds  # 获取秒
            min_res = (tomorrow - current_time).min  # 获取分钟
            if res_type == "micro":
                res = micro_res
            elif res_type == "sec":
                res = sec_res
            else:
                res = min_res
        else:
            res = 0

        return res


def get_time(time_type, *args, **kwargs):
    """
    获取时间: get_time('time_span')、get_time('date_str_time', 4)、get_time('surplus_time', 'sec')
    :param time_type: 时间类型
    """
    v_param = []
    t = TimeHandle()
    if hasattr(t, time_type):
        func = getattr(t, time_type)
        r = inspect.getfullargspec(func)
        for i in r.args:
            # 去除类本身参数
            if i != 'self':
                v_param.append(*args, **kwargs)

        return func(*v_param)
