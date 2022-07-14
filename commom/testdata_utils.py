#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/14 0014 15:53
import os
from commom.excel_utils import ExcelUtils

test_data_path = os.path.join(os.path.dirname(__file__), '..', 'test_data/test_case.xlsx')
class TestDataUtils:
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data=ExcelUtils('Sheet1',self.test_data_path).get_sheet_data_dict()

    def __get_testcase_data_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            test_case_dict.setdefault( row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict


    def get_testcase_data_list(self):
        test_case_list=[]
        for k,v in self.__get_testcase_data_dict().items():
            case_dict={}
            case_dict['case_name']=k
            case_dict['case_info']=v
            test_case_list.append(case_dict)
        return  test_case_list
#{'case01': [{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}], 'case02': [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '是', '测试用例步骤': 'stp_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': ''}], 'case03': [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}, {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'stp_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': ''}]}

if __name__=='__main__':
    test_data_utils=TestDataUtils()
    # print(test_data_utils.test_data)
    value=test_data_utils.get_testcase_data_list()
    print(value)
    for i in value:
        print(i)
