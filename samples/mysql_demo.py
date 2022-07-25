#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/24 0024 23:43

import pymysql

connect = pymysql.connect(host='127.0.0.1',
                          port=3306,
                          user='',
                          password='',
                          database='',
                          charset='utf8')

cur = connect.cursor( cursot = pymysql.cursors.DictCursor) #执行的sql返回值以字典形式展示
cur = connect.cursor( ) #执行的sql返回值以元组形式展示

sql_str='select * from table'
cur.execute(sql_str) #执行sql语句
cur.fetchall()