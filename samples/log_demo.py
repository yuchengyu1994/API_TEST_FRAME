#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/26 0026 19:40
import re
str0={'123':'123','223':'223'}
str1="{'一':'${123}','二':'${223}'}"
params_variables_list = re.findall('\\${\w+}', str1)
print(params_variables_list)
if params_variables_list:
    for params_variable in params_variables_list:
        print(params_variable[2:-1])
        str1 = str1.replace(params_variable,'"%s"' % str0.get(params_variable[2:-1]))

print(str1)

str2='123456789'
print(str2[3:-1])