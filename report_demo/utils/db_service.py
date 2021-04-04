# coding: utf-8
import mysql.connector
from ..constans import app_cof
from .log_handle import logger
from .base_utils import singleton


# mysql connect
def connect():
    conn = mysql.connector.connect(
        host=app_cof.MYSQL_HOST,
        port=app_cof.MYSQL_PORT,
        user=app_cof.MYSQL_USERNAME,
        password=app_cof.MYSQL_PASSWORD,
        database=app_cof.MYSQL_LIBRARY,
        auth_plugin="mysql_native_password",
        charset="utf8"
    )

    return conn


@singleton
class DBService:
    """数据库执行"""

    def __init__(self):
        self.conn = connect()

    # select
    def select_mysql(self, sql) -> list:
        """查询数据，返回[{}, {}, {}]"""

        conn = self.conn
        cursor = conn.cursor()
        cursor.execute(sql)

        # 获取表数据、表结构
        values = cursor.fetchall()
        fields = cursor.description
        try:
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error("数据库查询异常: {}".format(e))
        conn.close()
        # 定义表结构列表再提取字段追加到列表中
        column_lst = []
        for i in fields:
            column_lst.append(i[0])
        sql_lst = []
        for row in values:
            result = {}
            for i in range(len(row)):
                result[column_lst[i]] = row[i]
            sql_lst.append(result)

        return sql_lst

    # insert update...
    def operation_mysql(self, sql):
        """执行增删改语句"""

        conn = self.conn
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()

        try:
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error("数据库执行异常: {}".format(e))
        conn.close()
