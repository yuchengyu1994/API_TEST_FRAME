#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/21 0021 11:30
from common.requests_utils import RequestsUtils
from common.testdata_utils import TestDataUtils

all_caes_info= TestDataUtils().get_testcase_data_list()
case_info=all_caes_info[0].get('case_info')
str1=RequestsUtils().requests_by_step(case_info)
print(str1)
