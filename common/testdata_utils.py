#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/14 0014 15:53
import os
import re
from common.excel_utils import ExcelUtils
from common.config_utils import read_config
from common.sql_utils import SqlUtils

test_data_path = os.path.join(os.path.dirname(__file__), '..', read_config.get_case_data_path)
class TestDataUtils:
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data_sheet=ExcelUtils('Sheet1',self.test_data_path)
        self.test_data = self.test_data_sheet.get_sheet_data_dict()
        # self.test_data_bysql=SqlUtils().get_mysql_test_info()

    def __get_testcase_data_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            if row_data['用例执行'] == '是':
                test_case_dict.setdefault( row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict


    def get_testcase_data_list(self):
        test_case_list=[]
        for k,v in self.__get_testcase_data_dict().items():
            case_dict={}
            case_dict['case_id']=k
            case_dict['case_info']=v
            test_case_list.append(case_dict)
        return  test_case_list
#{'case01': [{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}], 'case02': [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '是', '测试用例步骤': 'stp_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': ''}], 'case03': [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': ''}, {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'stp_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': ''}]}
    def __get_testcase_data_dict_by_mysql(self):
        test_case_dict = {}
        for row_data in self.self.test_data_bysql:
            test_case_dict.setdefault( row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict


    def get_testcase_data_list_by_mysql(self):
        test_case_list=[]
        for k,v in self.__get_testcase_data_dict_by_mysql().items():
            case_dict={}
            case_dict['case_id']=k
            case_dict['case_info']=v
            test_case_list.append(case_dict)
        return  test_case_list

    def get_row_num(self,case_id,case_step_name):
         for j in range (len(self.test_data)):
             if self.test_data[j]['测试用例编号']==case_id and self.test_data[j]['测试用例步骤']==case_step_name:
                 break
         return j+1

    def get_result_id(self):
        for col_id in range(len(self.test_data_sheet.sheet.row(0))):
            if self.test_data_sheet.sheet.row(0)[col_id]=='测试结果':
                break
        return col_id

    def write_result_to_excel(self,case_id,case_step_name,content='通过'):
        row_id=self.get_row_num(case_id,case_step_name)
        col_id=self.get_result_id()
        self.test_data_sheet.update_excel_data(row_id,col_id,content)

    def clear_result_to_excel(self):
        row_count=self.test_data_sheet.get_row_count()
        col_id=self.get_result_id()
        for row_id in range(1,row_count):
            self.test_data_sheet.update_excel_data(row_id,col_id,'')

if __name__=='__main__':
    test_data_utils=TestDataUtils()
    # test_data_utils.clear_result_to_excel()
    # test_data_utils.write_result_to_excel('case01','stp_01','失败')
    # print(test_data_utils.test_data)
    value=test_data_utils.get_testcase_data_list()
    print(value)
    # for i in value:
    #     print(i)
    # all_caes_info=test_data_utils.get_testcase_data_list()
    # case_info=all_caes_info[0].get('case_info')



