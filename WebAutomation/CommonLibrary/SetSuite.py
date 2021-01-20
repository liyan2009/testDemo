#! python3
#-*- coding:utf-8 -*-

import os
import unittest

#这个是获取配置文件里要执行的*.py文件
class SetSuite(object):
    #获取脚本的目录
    path=os.path.split(os.path.dirname(__file__))[0]

    #获取要执行用例的py文件
    def getFile(self):
        set_FileList=[]
        #这里是需要改进的地方
        casePath="C:/Users/liyan/PycharmProjects/WebAutomation/caselist.txt"
        fb=open(casePath)
        for file in fb.readlines():
            caseFile=str(file)
            if caseFile !="" and not caseFile.startswith("#"):
                set_FileList.append(caseFile.replace("\n",""))
        fb.close()
        return set_FileList


    #获取要执行的用例集
    def getSuite(self):
        file_list=self.getFile()
        print(file_list)
        suite_model=[]
        #这里需要优化
        path="C:/Users/liyan/PycharmProjects/WebAutomation/TestCaseRepository"
        suite=unittest.TestSuite()
        for case_file in file_list :
            print(case_file)
            #获取某个指定py的所有用例集
            discover=unittest.defaultTestLoader.discover(path,pattern=case_file+".py",top_level_dir=None)
            suite_model.append(discover)
        print(suite_model)
        if len(suite_model)>0:
            for case in suite_model:
                suite.addTest(case)
        else:
            return None
        print(suite)
        return suite




ss=SetSuite()
ss.getFile()
ss.getSuite()