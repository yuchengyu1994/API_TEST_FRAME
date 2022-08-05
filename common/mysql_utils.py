#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/8/5 0005 22:00
import pymysql
from common.config_utils import read_config

#未实现，猜测解决方法
class MysqlUtils:

    def __init__(self, host=read_config.get_db_host, port=read_config.get_db_port,
                 user=read_config.get_db_username, password=read_config.get_db_password,database=read_config.get_db_name):
        self.connect = pymysql.connect(user=user,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=database,
                                    charset=read_config.get_db_charset
                                    )
        self.cur = self.connect.cursor(cursot=pymysql.cursors.DictCursor)

    def query_one(self, sql):
        self.cur.execute(sql)
        data = self.cur.fetchone()
        self.cur.close()
        return data

    def query_all(self, sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.cur.close()
        return data



    # 自己实现上下文管理器
    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     return self.close()


mysql_utils = MysqlUtils()

if __name__ == '__main__':
    db = MysqlUtils()
    sql = 'select mobile_phone from futureloan.member limit 5'


