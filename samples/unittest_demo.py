#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/23 0023 12:39
import paramunittest
import unittest

# @paramunittest.parametrized(   #如果是元组，setParameters中的参数可以随便写
#     (8,5),
#     (10,20)
# )
# @paramunittest.parametrized(   ##如果是列表，setParameters中的参数可以随便写
#     [8,5],
#     [10,20]
# )
# @paramunittest.parametrized(   ##如果是字典，setParameters中的参数只能写字典内的键
#     {'numa':5,'numb':8},
#     {'numb':10,'numa':20}
# )
#函数或者数据对象传入进去
test1=[{'numa':5,'numb':8},{'numb':10,'numa':20}]
def get_data():
    return [{'numa':5,'numb':8},{'numb':10,'numa':20}]
@paramunittest.parametrized( *get_data() )


class UnittestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa, numb):
        self.numa=numa
        self.numb=numb

    def test_case(self):
        print('numa:%d,numb:%d'%(self.numa,self.numb))
        self.assertGreater(self.numa,self.numb)

if __name__ == '__main__':
    unittest.main()