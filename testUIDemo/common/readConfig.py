import os
import configparser
import requests
import json

class ReadConfig(object):

    def readConfig(self):
        cf=configparser.ConfigParser()
        #获取对应文件夹
        proDir=os.path.split(os.path.realpath(__file__))[0]

        #获取上级目录
        curDir=os.path.dirname(proDir)
        #获取配置文件夹所在的路径
        configPath=os.path.join(curDir,"common\\baseconf.ini")

        cf.read(configPath, encoding="utf-8-sig")#含中文的需要加这个编码
        return cf

