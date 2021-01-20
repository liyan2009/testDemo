#! python3
# -*- coding:utf-8 -*-
import requests,json,re #使用json，正则表达式
import  xlwt #写excel
import  xlrd #读取excel
from package.test_api import testApi
from package.writeExcel import writeExcel
import package.editSocialPost
from bs4 import BeautifulSoup  #解析html及xml文件
from xlutils.copy import copy  #修改excel


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
baseUrl = "https://guanli.mayihr.com"
method="post"
Rurl="https://guanli.mayihr.com/public/afs"
data="{'username':'13469968124','password':'mayihr1234'}"
we = writeExcel(header)
ycookies=we.getCookie(method,Rurl,data)
# print(ycookies)
# we = writeExcel(header)
old_excel = xlrd.open_workbook('D:\\autoAPI\\fileName1.xls', 'formatting_info=True')
# 将操作对象拷贝变成可写的workbook对象
new_excel = copy(old_excel)
# 获取第一个excel的sheet内容
ws = new_excel.get_sheet(0)

class newCitygetPhone(object):
    #先获取登录的cookie信息
    # def getCookie(self,method,url,data):
    #     ta=testApi(method,url,eval(data)) #一定要注意这里字符串的转化
    #     rs=ta.testInterface
    #     ycookies=rs.cookies.get_dict()
    #     print('打印的值%s' %ycookies)
    #     return ycookies

    #读取excel的身份证信息
    def readCardID(self):
        readbook = xlrd.open_workbook(r'D:\\autoAPI\\fileName1.xls')
        sheet=readbook.sheet_by_index(0)
        fileName=r'D:\\autoAPI\\fileName1.xls'
        rowCount=we.GetRows(fileName)
        i = 3
        while (i < rowCount):
            card = sheet.cell(i, 2).value  # 身份证
            name=sheet.cell(i, 0).value
            a=package.editSocialPost.SelectYG(card,header,ycookies,baseUrl) #这里的梗后面再进行改进
            bbb=package.editSocialPost.ZfcTQUrl(a[0])
            # print(bbb)
            listJson=self.getPhone(bbb)
            print(listJson)
            we.writeDetailExcel(listJson,i,ws,name,card)
            i=i+1

    #获取员工的基本信息（手机号、学历、民族、社保状态、社保账号、公积金状态、公积金账号）
    def getPhone(self,ygUID):
        reqUrl = baseUrl + ygUID
        rs = requests.get(reqUrl, headers=header, cookies=ycookies)
        html = rs.text
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        listInfo=[]
        content = soup.find_all("div", attrs={"class": "col-sm-8 left"})
        sex=content[1].get_text().strip()   #获取性别
        strPhone = content[2].get_text().strip()   #获取手机号
        strXueLi = content[5].get_text().strip()  # 获取学历
        mzContent = soup.find_all("div", attrs={"class": "col-sm-7 left"})
        strMZ=mzContent[0].get_text().strip()   #获取民族

        #获取员工的所在城市及户口信息
        strTY=soup.find_all("span", attrs={"class": "col-sm-2 text-left"})
        strCity=strTY[0].get_text().strip() #获取城市



        strHJContent = soup.find_all("span", attrs={"class": "col-sm-1 text-left"})
        strHJ = strHJContent[0].get_text().strip()  # 获取户籍信息


        #获取社保信息
        contentSocial = soup.find_all("div", attrs={"class": "col-sm-4 left"})
        # print(contentSocial)
        strSBJS=contentSocial[0].get_text().strip()  # 获取社保基数
        strJN = contentSocial[1].get_text().strip()  # 获取社保是否在当地缴纳
        strZH = contentSocial[3].get_text().strip()  # 社保电脑号
        strGZ = contentSocial[4].get_text().strip()  # 社保规则

        # print(contentSocial)
        # 获取公积金相关信息
        # print(contentSocial[5].get_text().strip()) #or (contentSocial[5].get_text().strip()!="--")
        if (sex=="女" and strCity=="深圳")or (contentSocial[5].get_text().strip()!="--" and strCity=="大兴") :
            strFundBase = contentSocial[6].get_text().strip()  # 公积金基数
            strFundStatus = contentSocial[7].get_text().strip()  # 公积金缴纳状态
            strFund=contentSocial[10].get_text().strip()  # 公积金规则
            strAcct=contentSocial[9].get_text().strip()  # 公积金账号
        else:
            strFundBase = contentSocial[5].get_text().strip()  # 公积金基数
            strFundStatus = contentSocial[6].get_text().strip()  # 公积金缴纳状态
            strFund=contentSocial[9].get_text().strip()  # 公积金规则
            strAcct=contentSocial[8].get_text().strip()  # 公积金账号
        # print(strFundStatus)
        #获取社保和公积金缴纳状态
        contentJN = soup.find_all("div", attrs={"class": "col-sm-4 left text-primary"})
        # print(contentJN)
        strSJN=contentJN[0].get_text().strip() #社保是否缴纳
        strFJN = contentJN[2].get_text().strip()  # 公积金是否缴纳

        #获取杭州外地户口的户籍信息
        # strhz_HKtype=self.getHj(ygUID)

        listInfo.append(sex)
        listInfo.append(strPhone)
        listInfo.append(strXueLi)
        listInfo.append(strMZ)
        listInfo.append(strCity)
        listInfo.append(strHJ)
        listInfo.append(strSBJS)
        listInfo.append(strJN)
        listInfo.append(strZH)
        listInfo.append(strGZ)
        listInfo.append(strFundBase)
        listInfo.append(strFundStatus)
        listInfo.append(strFund)
        listInfo.append(strAcct)
        listInfo.append(strSJN)
        listInfo.append(strFJN)
        # listInfo.append(strhz_HKtype)
        # print(listInfo)
        return  listInfo


    #把值写入到excel中


    #针对杭州的获取户籍是省内还是省外
    #https://guanli.mayihr.com/yg/editSocial/id/8555
    def getHj(self,ygUID):
        # hjTypeUrl="https://guanli.mayihr.com/yg/editSocial/id/815839"
        ygHk=ygUID.replace('detail','editSocial')
        reqUrl = baseUrl + ygHk
        #怎么进行替换
        rs = requests.get(reqUrl, headers=header, cookies=ycookies)
        html = rs.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.find_all("select", attrs={"id": "hz_hk_type"})
        options = content[0].find_all("option",{'selected':{''}})#获取被中的值
        hktypes=options[0].get_text().strip()
        # print(hktypes)
        return hktypes
ncp=newCitygetPhone()
ncp.readCardID()
new_excel.save('D:\\autoAPI\\fileName.xls')
# ncp.getPhone("/yg/detail/id/651300")
#写入excel中
