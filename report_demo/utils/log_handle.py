# coding: utf-8
from ..constans import f
import logging
import time
import os

# 定义日志文件路径
LOG_PATH = os.path.join(f.proFile, "logs")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:
    """日志"""
    logger = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.log_name = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
            cls.logger = logging.getLogger("log")
            cls.logger.setLevel(logging.DEBUG)
            cls.for_mater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
            cls.file_logger = logging.FileHandler(cls.log_name, mode='a', encoding="UTF-8")
            cls.console = logging.StreamHandler()
            cls.console.setLevel(logging.DEBUG)
            cls.file_logger.setLevel(logging.DEBUG)
            cls.file_logger.setFormatter(cls.for_mater)
            cls.console.setFormatter(cls.for_mater)
            cls.logger.addHandler(cls.file_logger)
            cls.logger.addHandler(cls.console)

        return cls.logger


logger = Logger().get_logger()
