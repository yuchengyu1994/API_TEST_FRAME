#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/23 0023 13:47
import os
import unittest
from common.config_utils import read_config
from common import HTMLTestReportCN
from common.email_utils import EmailUtils

current_path=os.path.dirname(__file__)
test_case_path=os.path.join(current_path,'..',read_config.get_case_path)
test_reports_path=os.path.join(current_path,'..',read_config.get_report_path)
class RunAllCase:
    def __init__(self):
        self.test_case_path=test_case_path
        self.reports_path=test_reports_path
        self.title= '接口自动化测试报告'
        self.description = '自动化测试接口框架'
        self.tester='YuChengYu'

    def __load_test_suite(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path
                                                       )
        all_suite=unittest.TestSuite()
        all_suite.addTest(discover)
        return all_suite

    def run(self):
        report_dir=HTMLTestReportCN.ReportDirectory(self.reports_path)
        report_dir.create_dir(self.title)
        dir_path=HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        # dir_path=HTMLTestReportCN.GlobalMsg.get_value('report_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp =open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.__load_test_suite())
        fp.close()
        return dir_path

if __name__=='__main__':
    dir_path=RunAllCase().run()
    EmailUtils('自动化测试报告','来自python的自动化测试报告',dir_path).send_mail()