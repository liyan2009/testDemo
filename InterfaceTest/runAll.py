#! python3
# -*- coding:utf-8 -*-

import  time
import  unittest
import os
from ddt import ddt,data,unpack
from BeautifulReport import BeautifulReport
from tomorrow import threads
import  HTMLTestRunner

''' common：存放一些共通的方法

  result：执行过程中生成的文件夹，里面存放每次测试的结果

  testCase：用于存放具体的测试case

  testFile：存放测试过程中用到的文件，包括上传的文件，测试用例以及     数据库的sql语句

  caselist：txt文件，配置每次执行的case名称

    config：配置一些常量，例如数据库的相关信息，接口的相关信息等

    readConfig： 用于读取config配置文件中的内容

    runAll：用于执行case
'''

@ddt
class RunAll(unittest.TestCase):

    # def test_case1(self):
    #     self.assertEqual(self.number,15,msg='等于15')

    @data(1)
    def test_case2(self,value):
        print("qqqqq")
        print(value)
        self.assertEqual(value,1)

    # def test_case3(self):
    #     self.assertEqual(self.number,30,msg='不等于30')
    def tearDown(self):
        print("test over")

'''
if __name__=='__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(Test("test_case1"))
    testunit.addTest(Test("test_case2"))
    testunit.addTest(Test("test_case3"))
    #获取当前时间
    now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
    print(now)

    
    filepath="D:\\result\\"+now+".html"
    fp=open(filepath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="test",description=u"result:")
    runner.run(testunit)
    fp.close()

'''


#获取当前路径
curpath=os.path.dirname(os.path.realpath(__file__))
print(curpath)

#设置用例的路径
casepath=os.path.join(curpath,"testCase")
if not os.path.exists(casepath):
    print("测试用例需要放在testCase目录下面")
    os.mkdir(casepath)

#设置报告的路径
reportpath=os.path.join(curpath,"report")
if not os.path.exists(reportpath):
    print("测试用例需要放在report目录下面")
    os.mkdir(reportpath)

#添加用例，查找所有的用例
def add_case(case_path=casepath,rule="Test*.py"):
    discover=unittest.defaultTestLoader.discover(casepath,pattern=rule,top_level_dir=None)
    return discover


@threads(3)
def run(test_suite):
    result=BeautifulReport(test_suite)
    result.report(filename='report.html',description='测试报告',log_path='report')

if __name__=="__main__" :
    cases=add_case()
    # print(cases)
    for i in cases:
        run(i)


