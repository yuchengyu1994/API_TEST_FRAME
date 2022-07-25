#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/25 0025 13:03

import pymysql

class SqlUtils:
    def __init__(self):
        self.connect = pymysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='',
                                  password='',
                                  database='',
                                  charset='utf8')
        self.cur=self.connect.cursor(cursot = pymysql.cursors.DictCursor)

    def get_mysql_test_info(self):
        sql_str='''
        '''
        self.cur.execute(sql_str)
        return  self.cur.fetchall()



