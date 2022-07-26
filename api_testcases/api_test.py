#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/23 0023 13:09


import paramunittest
import unittest
from common.testdata_utils import TestDataUtils
from common.requests_utils import RequestsUtils
from nb_log import LogManager

logger=LogManager(__file__).get_logger_and_add_handlers()
case_infos=TestDataUtils().get_testcase_data_list()
# case_infos=TestDataUtils().get_testcase_data_list_by_mysql()
@paramunittest.parametrized( *case_infos)

class ApiTest(paramunittest.ParametrizedTestCase):
    def setParameters(self, case_id,case_info):
        logger.info('加载测试数据')
        self.case_id=case_id
        self.case_info=case_info
    # def test_demo(self):
    #     print(self.case_id,self.case_info[0]['测试用例名称'])

    def test_api_common_function(self):
        logger.info('测试用例[%s]开始执行'%self.case_info[0].get('测试用例编号')+self.case_info[0].get('测试用例名称'))
        self._testMethodName=self.case_info[0].get('测试用例编号')
        self._testMethodDoc=self.case_info[0].get('测试用例名称')
        actual_result=RequestsUtils().requests_by_step(self.case_info)
        self.assertTrue(actual_result['check_result']),actual_result.get('message')

if __name__=='__main__':
    unittest.main()