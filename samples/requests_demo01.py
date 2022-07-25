#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/17 0017 11:03
import re
import ast

# str='{"access_token":${token}}'
# temp={'token':'123456'}
# params=re.findall('\\${\w+}',str)[0]
# str=str.replace(params,'"'+temp.get(params[2:-1])+'"')
# print(str)
# str1='{"123":"321","111":"222"}'
# list1={"123":"321","111":"222"}
# for i in list1.items():
#     print(i)
# print(list1.items())
# print( ast.literal_eval(str1).items())

str1 = '{"access_token":"dsadasdas","expires_in":7200}'
str2 = re.findall(r'"access_token":"(.+?)"', str1)
print(str2)

