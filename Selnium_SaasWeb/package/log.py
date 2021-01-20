#python3
#-*-coding:utf-8 -*-#

import logging



#日志的等级CRITICAL > ERROR > WARNING > INFO > DEBUG

'''这里是日志记录模块'''

class Log(object):
    def __init__(self,log_file):
        '''在初始化的时候构建logger对象'''
        # 创建一个logger,顶级的根目录getlogger,有两个分支,一个是FileHander,一个是StreamHandler
        self.logger=logging.getLogger('mylogger')
        self.logger.setLevel(logging.INFO)
        #创建一个handler，将log写入文件
        fh=logging.FileHandler(log_file,mode='w')
        fh.setLevel(logging.INFO)
        #再创建一个handler，将log输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #设置输出格式
        log_format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
        formatter=logging.Formatter(log_format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)


        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def info(self,content):
        self.logger.info(content)

    def error(self,content):
        self.logger.error(content)

    def debug(self,content):
        self.logger.debug(content)

'''测试专用'''
# log=Log("D:/autoAPI/log.txt")
# log.info("消息测试")
# log.error("错误测试")
# log.debug("错误测试")