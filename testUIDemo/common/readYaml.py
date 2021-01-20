#! python3
#! -*- coding:utf-8 -*-

import yaml
import os

class ReadYaml(object):
    curFile = os.getcwd()
    # fath_path = os.path.abspath(os.path.dirname(curFile))
    fath_path = os.path.abspath(curFile)
    # filePath = os.path.join(fath_path, "testData\login.yaml") #键和值之间一定要多加一个空格，不然语法错误！

    def readFile(self,filePath):
        fileYaml = os.path.join(self.fath_path, filePath)
        f=open(fileYaml,'r',encoding='utf-8')
        cont=f.read()
        x=yaml.load(cont,Loader=yaml.Loader)#直接试用load会报错，需要加上后面的
        f.close()
        # print(x)
        return x

# r=ReadYaml()
# data=r.readFile("testData\login.yaml")
# print(data["case3"])

