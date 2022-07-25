#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/16 0016 10:21
import json

import requests
import ast
import re
import jsonpath
from common.config_utils import read_config


class RequestsTest:
    def __init__(self):
        self.hosts = read_config.get_url
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.session = requests.session()
        self.proxies = {'http': 'http://127.0.0.1:7890',
                   'https': 'http://127.0.0.1:7890'}
        self.temp_variables={}

    def __get(self,get_info):
        url=self.hosts+get_info['请求地址']
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_info['请求参数(get)']),
                                    proxies=self.proxies
                                    )
        response.encoding=response.apparent_encoding
        print(response.text)
        if get_info['取值方式'].__eq__('json取值'):
            value=jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
            self.temp_variables[get_info['传值变量']]=value
        elif get_info['取值方式'].__eq__('正则取值'):
            value=re.findall(get_info['取值代码'],response.text)[0]
            self.temp_variables[get_info['传值变量']]=value
        result={
            'code':0, #请求是否成功的标志位
            'response_reason':response.reason,
            'response_code':response.status_code,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def __post(self, post_info):
        url = self.hosts + post_info['请求地址']
        response = self.session.get(url=url,
                                    headers=self.headers,
                                    params=ast.literal_eval(post_info['请求参数(get)']),
                                    proxies=self.proxies,
                                    data=ast.literal_eval(post_info['提交数据(post)'])
                                    )
        response.encoding = response.apparent_encoding
        if post_info['取值方式'].__eq__('json取值'):
            value=jsonpath.jsonpath(response.json(),post_info['取值代码'])[0]
            self.temp_variables[post_info['传值变量']]=value
        elif post_info['取值方式'].__eq__('正则取值'):
            value = re.findall(post_info['取值代码'], response.text)[0]
            self.temp_variables[post_info['传值变量']] = value
        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def requests(self,step_info):
        params_variables_list = re.findall('\\${\w+}', step_info['请求参数(get)'])
        if params_variables_list:
            for params_variable in params_variables_list:
                step_info['请求参数(get)'] = step_info['请求参数(get)'].replace(params_variable,'"%s"%' % self.temp_variables.get(params_variable[2:-1]))
        if step_info['请求方式'].__eq__('get'):
            result=self.__get(step_info)
        elif step_info['请求方式'] == 'post':
            data_variables_list = re.findall('\\${\w+}', step_info['提交数据(post)'])
            if data_variables_list:
                for data_variable in data_variables_list:
                    step_info['提交数据(post)'] = step_info['提交数据(post)'].replace(data_variable,\
                                            '"%s"%' % self.temp_variables.get(data_variable[2:-1]))
            result=self.__post(step_info)
        else:
            result={'code':3,'result':'请求方式不支持'}
        return result

    def requests_by_step(self,setp_infos):
        for step_info in setp_infos:
            result= self.requests( step_info )
            if result['code']!=0:
                break
        return result


if __name__ == '__main__':
    get_infos={'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'stp_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': "{'grant_type':'client_credential','appid':'wx5112b86dc2a467ee','secret':'c47f6c4369cb884f9562ba0fc9b6934b'}", '取值方式': '正则取值', '取值代码': '"access_token":"(.+?)","e', '传值变量': 'token'}
    access_token=RequestsTest().requests(get_infos)
    print(type(access_token))
