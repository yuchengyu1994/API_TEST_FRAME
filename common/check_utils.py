#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/19 0019 15:40
import re
import ast
import requests
from common.testdata_utils import TestDataUtils



class CheckUtils:
    def __init__(self,response=None):
        self.check_rule={
            '无':self.no_check,
            'json键是否存在':self.check_key,
            'json键值对':self.check_keyvalue,
            '正则匹配':self.check_regexp
        }
        self.response=response
        self.pass_result ={
            'code': 0,  # 请求是否成功的标志位
            'response_reason': self.response.reason,
            'response_code': self.response.status_code,
            'response_headers': self.response.headers,
            'response_body': self.response.text,
            'check_result':True,
            'message':'excute success'  #扩展作为日志输出
        }
        self.fail_result={
            'code': 1,  # 请求是否成功的标志位
            'response_reason': self.response.reason,
            'response_code': self.response.status_code,
            'response_headers': self.response.headers,
            'response_body': self.response.text,
            'check_result': False,
            'message': 'excute fail'
        }

    def no_check(self):
        return self.pass_result

    def check_key(self,check_data=None):
        check_data_list=check_data.split(',')
        result_list=[] #存放每次比较的结果
        wrong_key=[]#存放比较失败的key
        for data in check_data_list:
            if data in self.response.json().keys():
                result_list.append(self.pass_result)
            else:
                result_list.append(self.fail_result)
                wrong_key.append(data)
        if self.fail_result in result_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self,check_data=None):
        result_list = []  # 存放每次比较的结果
        wrong_items = []  # 存放比较失败的key
        for data in ast.literal_eval(check_data).json().items():
            if data in self.response.items():
                result_list.append(self.pass_result)
            else:
                result_list.append(self.fail_result)
                wrong_items.append(data)
        if False in result_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self,check_data=None):
        pattern=re.compile(check_data)
        if re.findall(pattern,self.response.text):
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self,check_type=None,check_data=None):
        code=self.response.status_code
        if code ==200:
            if check_type in self.check_rule.keys():
                result=self.check_rule[check_type](check_data)
                return result
            else:
                self.fail_result['message']='不支持%s判断方法'%check_type
                return self.fail_result
        else:
            self.fail_result['message']='请求的响应状态码非200'
            return self.fail_result



if __name__ == '__main__':
    proxies = {'http': 'http://127.0.0.1:7890',
                    'https': 'http://127.0.0.1:7890'}
    test_data_utils=TestDataUtils()
    all_caes_info=test_data_utils.get_testcase_data_list()
    case_info=all_caes_info[0].get('case_info')[0]
    session = requests.session()
    response = session.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=ast.literal_eval(case_info['请求参数(get)']),
                                proxies=proxies
                                )
    result = CheckUtils(response).run_check(case_info['期望结果类型'], case_info['期望结果'])
    print(result)