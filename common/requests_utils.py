#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/16 0016 10:21
import json

import requests
import ast
import re
import jsonpath
from requests.exceptions import RequestException
from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError
from common.check_utils import CheckUtils
from common.config_utils import read_config
from common.testdata_utils import TestDataUtils
from nb_log import LogManager


logger=LogManager(__file__).get_logger_and_add_handlers()

class RequestsUtils:
    def __init__(self):
        self.hosts = read_config.get_url
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.session = requests.session()
        self.proxies = {'http': 'http://127.0.0.1:7890',
                   'https': 'http://127.0.0.1:7890'}
        self.temp_variables={}

    def __get(self,get_info):
        try:
            url=self.hosts+get_info['请求地址']
            response = self.session.get(url=url,
                                        params=ast.literal_eval(get_info['请求参数(get)']),
                                        proxies=self.proxies
                                        )
            response.encoding=response.apparent_encoding
            if get_info['取值方式'].__eq__('json取值'):
                value=jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
                self.temp_variables[get_info['传值变量']]=value
            elif get_info['取值方式'].__eq__('正则取值'):
                value=re.findall(get_info['取值代码'],response.text)[0]
                self.temp_variables[get_info['传值变量']]=value
            result = CheckUtils(response).run_check(get_info['期望结果类型'],get_info['期望结果'])
        except ProxyError as e:
            result = {'code':4,'result':'[%s]请求代理异常，原因是%s'%(get_info['接口名称'],e.__str__())}
        except ConnectionError as e:
            result = {'code':4,'result':'[%s]请求连接超时，原因是%s'%(get_info['接口名称'],e.__str__())}
        except RequestException as e:
            result = {'code':4,'result':'[%s]请求执行报Request异常，原因是%s'%(get_info['接口名称'],e.__str__())}
        except Exception as e:
            result = {'code':4,'result':'[%s]请求执行报系统错误，原因是%s'%(get_info['接口名称'],e.__str__())}
        return result

    def __post(self, post_info):
        try:
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
            result = CheckUtils(response).run_check(post_info['期望结果类型'],post_info['期望结果'])
        except ProxyError as e:
            result = {'code':4,'result':'[%s]请求代理异常，原因是%s'%(post_info['接口名称'],e.__str__())}
        except ConnectionError as e:
            result = {'code':4,'result':'[%s]请求连接超时，原因是%s'%(post_info['接口名称'],e.__str__())}
        except RequestException as e:
            result = {'code':4,'result':'[%s]请求执行报Request异常，原因是%s'%(post_info['接口名称'],e.__str__())}
        except Exception as e:
            result = {'code':4,'result':'[%s]请求执行报系统错误，原因是%s'%(post_info['接口名称'],e.__str__())}
        return result

    def requests(self,step_info):
        try:
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
                logger.error('请求方式不支持')
        except Exception as e:
            result = {'code':4,'result':'[%s]请求执行报系统错误，requests异常，原因是%s'%(step_info['接口名称'],e.__str__())}
            logger.error('[%s]请求执行报系统错误，requests异常，原因是%s'%(step_info['接口名称'],e.__str__()))
        return result

    def requests_by_step(self,setp_infos):
        for step_info in setp_infos:
            result= self.requests( step_info )
            # print(result)
            if result['code']!=0:
                TestDataUtils().write_result_to_excel(step_info['测试用例编号'],step_info['测试用例步骤'],'失败')
                break
            else:
                TestDataUtils().write_result_to_excel(step_info['测试用例编号'],step_info['测试用例步骤'])
        return result


if __name__ == '__main__':
    test_data_utils=TestDataUtils()
    all_caes_info=test_data_utils.get_testcase_data_list()
    get_infos=all_caes_info[0].get('case_info')
    access_token=RequestsUtils().requests_by_step(get_infos)
    print(type(access_token))
