#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/18 0018 14:38
import re

# str1 = 'test yuchengyu is your father!'
# str2 = "hunan1shanghai2fujian3shandong4henan"
# pattern = re.compile(r'(\w+) (\w+) (\w+) (\w+)(?P<sign>.*)')  # 加了r 是原生字符串
# result1 = re.match(r'(\w+) (\w+) (\w+) (\w+)(?P<sign>.*)', str1)  # 匹配以什么开头
# result1 = re.search(r'yuchengyu',str1)
# result1 = re.split(r'\d',str2)
# result1 = re.findall(r'\d',str2)
# result1 = re.finditer(r'\d',str2)
# print(result1)
# for i in result1:
#     print(i)


# print(result1.string)
# print(result1.re)
# print(result1.pos)
# print(result1.endpos)
# print(result1.lastindex)
# print(result1.lastgroup)
#
# print(result1.group())
# print(result1.groups())
# print(result1.groupdict())
# print(result1.start())
# print(result1.end())
# print(result1.span())
# print(result1.expand())


str1='summer hot~'
# result1=re.sub( r'(\w+) (\w+)',r'hello',str1 )
print(str1)
result = re.match(r'(\w+) (\w+)',str1 )
print(result.group(1).title())
def fun(m):
    return m.group(1).title() + ' ' +m.group(2).title()
result1=re.sub( r'(\w+) (\w+)',fun(result),str1 )
print(result1)
str1=re.subn(r'(\w+) (\w+)',fun(result),str1 )
print(str1)
str2=re.subn(r'(\w+) (\w+)',r'\2 \1','summer hot~' )
print(str2[0])