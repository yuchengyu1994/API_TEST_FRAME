#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/26 0026 16:32
from faker import Faker

f=Faker(locale='zh_CN')

for i in range(10):
    print(f.name()+":"+f.ssn())