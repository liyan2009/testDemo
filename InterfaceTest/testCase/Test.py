#!python3
#coding:utf-8

import unittest
from ddt import ddt,data,unpack
class Test(unittest.TestCase):


    # def test_case1(self,number):
    #     u'''打印测试条件1'''
    #     self.assertEquals(number,10,'不等于10')
    #
    # def test_case2(self,number):
    #     u'''打印测试条件2'''
    #     self.assertEquals(number,20,'不等于20')
    #
    # def test_case3(self,number):
    #     u'''打印测试条件3'''
    #     self.assertEquals(number,30,'不等于30')
    #
    @data(2)
    def test_case1(self,value):
        self.assertEqual(value,2)
    # if __name__=='__main__':
    #     unittest.main()