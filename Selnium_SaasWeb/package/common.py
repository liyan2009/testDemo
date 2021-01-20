#! python3
# -*- coding:utf-8 -*-

import os
# from package import readConfig
from xlrd import open_workbook


'''操作excel文件类'''
class Common(object):

    # xls_name = "1.xls"
    # sheet_name = "Sheet1"
    # proDir = os.path.split(os.path.realpath(__file__))[0]
    # curDir = os.path.dirname(proDir)
    # caseFile = os.path.join(curDir, "result")
    # xlsPath = os.path.join(caseFile, xls_name)

    def __init__(self,xls_name,sheet_name):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        curDir = os.path.dirname(proDir)
        caseFile = os.path.join(curDir, "result")
        self.xlsPath = os.path.join(caseFile, xls_name)
        self.sheet_name=sheet_name

    '''这个是使用xlrd操作excel'''
    #获取excel中的测试用例
    def get_Excel(self):
        # 获取excel的路径
        # print(self.caseFile)
        cls=[]
        file=open_workbook(self.xlsPath)
        sheet=file.sheet_by_name(self.sheet_name)
        nrows=sheet.nrows
        #print(nrows)
        for i in range(nrows):
            if sheet.row_values(i)[1] !="case_name":
                cls.append(sheet.row_values(i))
        #print(cls)
        return cls

    #获取sheet
    @property
    def get_sheet(self):
        xl=open_workbook(self.xlsPath)
        sheet=xl.sheet_by_name(self.sheet_name)
        return sheet

    #获取excel的rows
    @property
    def get_rows(self):
        rows=self.get_sheet.nrows
        return  rows

    @property
    def get_cols(self):
        cols=self.get_sheet.ncols
        return  cols

    #获取用例ID
    @property
    def get_caseID(self):
        caseName=[]
        for i in range(1,self.get_rows):
            caseName.append(self.get_sheet.cell_value(i,0))
        return caseName

    #获取用例名称
    @property
    def get_caseName(self):
        caseName=[]
        for i in range(1,self.get_rows):
            caseName.append(self.get_sheet.cell_value(i,1))
        return caseName



    #获取发送请求类型
    @property
    def get_method(self):
        method=[]
        for i in range(1,self.get_rows):
            method.append(self.get_sheet.cell_value(i,2))
        return method

    #获取url地址
    @property
    def get_url(self):
        url=[]
        for i in range(1,self.get_rows):
            url.append(self.get_sheet.cell_value(i,3))
        return url

    #获取参数类型地址
    @property
    def get_dataType(self):
        data=[]
        for i in range(1,self.get_rows):
            data.append(self.get_sheet.cell_value(i,4))
        return data

    #获取参数值
    @property
    def get_data(self):
        data=[]
        for i in range(1,self.get_rows):
            data.append(self.get_sheet.cell_value(i,5))
            # print(self.get_sheet.cell_value(i,5))
        return data


    #获取检查点
    @property
    def get_CheckData(self):
        data=[]
        for i in range(1,self.get_rows):
            data.append(self.get_sheet.cell_value(i,6))
        return data


    #修改excel列的值
    def update_sheetValue(self,bool):
        sheet=self.get_sheet
        for i in range(1,self.get_rows):
            # sheet.cell(i,7).value=str(content)
            sheet.cell(i,10).value = bool
        #这里还差一步保存excel



# 测试代码
# cn=Common("1.xls","Sheet1")
# print(cn.get_Excel())
# cn.get_method
# print(cn.get_data)
