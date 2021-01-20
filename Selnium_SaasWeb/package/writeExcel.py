#! python3
# -*- coding:utf-8 -*-
import requests,bs4,json,re #使用json，正则表达式
import  xlwt #写excel
import  xlrd #读取excel
from xlutils.copy import copy  #修改excel
import datetime as dt

import http.cookiejar
from package.test_api import testApi
'''
@author:把后台的数据写入到excel中
'''
class writeExcel(object):
    def __init__(self,header):
        self.header=header

    #先获取登录的cookie信息
    def getCookie(self,method,url,data):
        ta=testApi(method,url,eval(data)) #一定要注意这里字符串的转化
        rs=ta.testInterface
        ycookies=rs.cookies.get_dict()
        # print('打印的值%s' %ycookies)
        return ycookies

    #获取半自动化的界面社保/公积金数据
    def getSocialorFund(self,parms,baseUrl,kz,ycookies):
        url=baseUrl+kz
        r=requests.get(url,headers=self.header,cookies = ycookies,params=parms)
        print(r.url)
        str=r.json()#转化为json格式
        #打印出获取的结果
        print(r.json())
        #打印出对应的值
        print(str["aaData"])#提取所需要的list信息
        return  str["aaData"]

    #把读取的值写入到excel
    def writeExcel(self,listJson,id,i,ws,kz,strName,strCard):
        ws.write(i, 0, strName)  # 姓名
        ws.write(i, 1, '身份证')
        ws.write(i, 2, strCard)#身份证
        ws.write(i, 4, '全职')
        style=xlwt.easyxf(num_format_str='yyyy/m/d')
        ws.write(i, 5, dt.date.today(),style)
        ws.write(i, 8, '10')
        ws.write(i, 10, '各缴')

        if id in(1,17):#社保需要填的值
            if kz == "socialDataOperation":
                ws.write(i, 11, '缴纳')
                ws.write(i, 15, listJson[13])  # 规则
                ws.write(i, 16, listJson[15])  # 基数
                ws.write(i, 14, listJson[12])  # 户口类型
            else:        #公积金需要填的值
                ws.write(i, 18, '缴纳')
                ws.write(i, 19, listJson[14])  # 规则
                ws.write(i, 20, listJson[16])  # 基数
                ws.write(i, 14, listJson[13])  # 户口类型
            if id==1:
                proviceName='直辖市北京'
                cityName='海淀'
            else:
                proviceName='直辖市北京'
                cityName='朝阳'
        #如果是上海
        if id==20:
            if kz == "socialDataOperation":
                ws.write(i, 14, listJson[14])  # 户口类型
                ws.write(i, 11, '缴纳')
                ws.write(i, 15, listJson[15])  # 规则
                ws.write(i, 16, listJson[17])  # 基数
            else:
                ws.write(i, 14, listJson[13])  # 户口类型
                ws.write(i, 18, '缴纳')
                ws.write(i, 19, listJson[14])  # 规则
                ws.write(i, 20, listJson[16])  # 基数
            proviceName='直辖市上海'
            cityName='上海市'

        #深圳
        if id==45:
            if kz == "socialDataOperation":
                ws.write(i, 14, listJson[13])  # 户口类型
                ws.write(i, 11, '缴纳')
                ws.write(i, 15, listJson[14])  # 规则
                ws.write(i, 16, listJson[16])  # 基数
            else:
                ws.write(i, 14, listJson[12])  # 户口类型
                ws.write(i, 18, '缴纳')
                ws.write(i, 19, listJson[13])  # 规则
                ws.write(i, 20, listJson[15])  # 基数
            proviceName='广东省深圳'
            cityName='深圳'

        #广州
        if id==1000:
            ws.write(i, 14, listJson[11])  # 户口类型
            if kz == "socialDataOperation":
                ws.write(i, 15, listJson[12])  # 规则
                ws.write(i, 16, listJson[14])  # 基数
            else:
                ws.write(i, 18, '缴纳')
                ws.write(i, 19, listJson[12])  # 规则
                ws.write(i, 20, listJson[14])  # 基数
            proviceName='广东省广州'
            cityName='天河区'
        style1=xlwt.easyxf(num_format_str='m-yy')
        ws.write(i, 12, proviceName)
        ws.write(i, 13, cityName)
        ws.write(i, 17, dt.datetime.today(),style1)#缴纳月份
        ws.write(i, 21, dt.datetime.today(),style1)#缴纳月份
        ws.write(i, 23, '否')#缴纳月份

    #将从员工明细里抓取到的信息写入到excel
    def writeDetailExcel(self,listJson,i,ws,name,card):
        ws.write(i, 0, name)  # 姓名
        ws.write(i, 1, '身份证')
        ws.write(i, 2, card)#身份证
        ws.write(i, 4, '全职')
        style=xlwt.easyxf(num_format_str='yyyy/m/d')
        ws.write(i, 5, dt.date.today(),style)
        ws.write(i, 8, '10')
        ws.write(i, 10, '各缴')
        ws.write(i, 14, listJson[5])  # 户口类型
        # print(listJson[5])
        #社保部分
        if listJson[14]=="缴纳":
            ws.write(i, 11, '缴纳') #是否缴纳社保
            ws.write(i, 16, listJson[9])  # 规则
            ws.write(i, 17, listJson[6])  # 基数
        else:
            ws.write(i, 11, '')

        #公积金部分
        if listJson[15]=="缴纳":
            ws.write(i, 19, '缴纳') #是否缴纳公积金
            ws.write(i, 20, listJson[12])  # 公积金规则
            ws.write(i, 21, listJson[10])  # 公积金基数
        else:
            ws.write(i, 19, '')

        city=listJson[4]
        # print(city)
        if city == "北京海淀":
            proviceName = '直辖市北京'
            cityName = '海淀'
        if city == "北京朝阳5加5":
            proviceName = '直辖市北京'
            cityName = '朝阳5加5'
        if city == "北京朝阳":
            proviceName = '直辖市北京'
            cityName = '朝阳'
        if city == "北京丰台托管":
            proviceName = '直辖市北京'
            cityName = '丰台'
        if city == "北京大兴托管":
            proviceName = '直辖市北京'
            cityName = '大兴'

        if city == "北京朝阳直营":
            proviceName = '直辖市北京'
            cityName = '垓蚁'  # test

        if city == "北京朝阳":
            proviceName = '直辖市北京'
            cityName = '朝阳'
        if city=="上海市":
            proviceName='直辖市上海'
            cityName='上海市'
        if city=="深圳":
            proviceName='广东省深圳'
            cityName='深圳'

        if city=="深圳直营代理":
            proviceName='广东省深圳'
            cityName='直营代理'

        if city=="广州天河区":
            proviceName='广东省广州'
            cityName='天河区'
        if city=="杭州杭州":
            proviceName='浙江省杭州'
            cityName='杭州'
            ws.write(i, 15, listJson[16])
        if city=="成都高新区":
            proviceName='四川省成都'
            cityName='高新区'
        if city=="上海只缴社保":
            proviceName='直辖市上海'
            cityName='只缴社保'

        if city=="长沙代理":
            proviceName='长沙'
            cityName='长沙'

        if city=="武汉":
            proviceName='湖北省武汉'
            cityName='武汉'

        if city=="杭州直营":
            proviceName='浙江省杭州'
            cityName='直营'
        #     15是杭州户口类型   成都高新区

        style1=xlwt.easyxf(num_format_str='m-yy')


        ws.write(i, 12, proviceName)
        ws.write(i, 13, cityName)
        ws.write(i, 18, dt.datetime.today(),style1)#缴纳月份
        ws.write(i, 22, dt.datetime.today(),style1)#缴纳月份
        ws.write(i, 23, listJson[1])  # 手机号
        ws.write(i, 24, '否')#是否开通员工自助


        # 在当地缴过    没有在当地缴过
        #社保缴纳状态及社保电脑号
        if listJson[7]=="在当地缴过":
            JNStatus="是"
        if listJson[7]=="没有在当地缴过" or listJson[7]=="未在当地缴过" :
            JNStatus="否"
        if listJson[7]=="--":
            JNStatus = ""
        if listJson[8]=="--" :
            listJson[8]=""
        # print("aa")
        # print(JNStatus)
        ws.write(i, 27,JNStatus)
        ws.write(i, 28, listJson[8])

        #公积金缴纳状态及公积金账号

        if listJson[11]=="在当地缴过":
            JNSStatus="是"
        if listJson[11]=="没有在当地缴过" or listJson[11]=="未在当地缴过" :
            JNSStatus="否"
        if listJson[11]=="--":
            JNSStatus = ""
        if listJson[13]=="--":
            listJson[13] = ""
        # print(listJson[11])
        ws.write(i, 25,JNSStatus)#公积金
        ws.write(i, 26, listJson[13])

        #个人的其他信息（性别、学历、民族）
        ws.write(i, 29, listJson[0])
        ws.write(i, 30, listJson[2])
        ws.write(i, 31, listJson[3])


    def GetRows(self,fileName):
        readbook = xlrd.open_workbook(fileName)
        sheet=readbook.sheet_by_index(0)
        nrows=sheet.nrows
        return nrows

    #读取excel的内容，社保
    def ReadExcel(self,i):
        readbook = xlrd.open_workbook(r'D:\\autoAPI\\fileName.xls')
        sheet=readbook.sheet_by_index(0)
        # i=3
        username=sheet.cell(i,0).value #姓名
        card=sheet.cell(i,2).value #身份证
        phone=sheet.cell(i,23).value #手机号
        hktype=sheet.cell(i,14).value #户籍类型
        social_name = sheet.cell(i, 16).value  # 社保类型
        base = sheet.cell(i, 17).value #基数
        #获取社保是否缴纳
        #是指的是否缴纳社保
        isSJN=sheet.cell(i,11).value
        if isSJN=="缴纳":
            isSJN=1
        else:
            isSJN = 0
        socialStatus=sheet.cell(i,27).value #社保缴纳状态
        socialAcct = sheet.cell(i, 28).value #社保账号
        csocialType=sheet.cell(i, 26).ctype
        if csocialType==2:
            socialAcct=int(socialAcct)

        #是否缴纳公积金
        isFJN=sheet.cell(i,19).value
        if isFJN=="缴纳":
            isFJN=1
        else:
            isFJN = 0

        #性别
        yg_gender=sheet.cell(i,29).value
        if yg_gender=="男":
            yg_gender=1
        elif yg_gender=="女":
            yg_gender = 2
        else:
            yg_gender = 0

        #公积金规则
        fund_rule=sheet.cell(i,20).value

        #公积金基数
        fund_base=sheet.cell(i,21).value

        fundStatus=sheet.cell(i,25).value #公积金缴纳状态
        fundAcct = sheet.cell(i, 26).value #公积金账号
        fundType=sheet.cell(i, 28).ctype
        if fundType==2:
            fundAcct=int(fundAcct)
        cityname=sheet.cell(i, 13).value #城市名称

        ygID=sheet.cell(i, 32).value

        ygDetailinfo=[]
        ygDetailinfo.append(card)
        ygDetailinfo.append(hktype)
        ygDetailinfo.append(social_name)
        ygDetailinfo.append(base)
        ygDetailinfo.append(socialStatus)
        ygDetailinfo.append(socialAcct)
        ygDetailinfo.append(cityname)
        ygDetailinfo.append(fundStatus)
        ygDetailinfo.append(fundAcct)

        ygDetailinfo.append(isSJN)
        ygDetailinfo.append(isFJN)
        ygDetailinfo.append(fund_rule)
        ygDetailinfo.append(fund_base)
        ygDetailinfo.append(username) #获取姓名
        ygDetailinfo.append(phone)
        ygDetailinfo.append(yg_gender) #性别

        ygDetailinfo.append(ygID)#员工编号

        # print(ygDetailinfo)
        return ygDetailinfo


# 这里是调试代码

# header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36","Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"}
# method = "post"
# url = "https://guanli.mayihr.com/public/afs"
# data = "{'username':'13469968124','password':'mayihr1234'}"
#
# cityCode = 1
# yg_name = ""
# iDisplayStart = ""
# user_id = ""
# user_uid = ""
# op_status = ""
# yg_status = "1"
# iDisplayLength = ""
#
# parms={"city":cityCode,"yg_status":yg_status,"yg_name":yg_name,"sub_status":"","iDisplayStart":iDisplayStart,"is_daiguan":"","user_uid":user_uid,"user_id":user_id,"op_status":op_status,"yg_status":yg_status,"iDisplayLength":iDisplayLength}
# baseUrl1 = "https://guanli.mayihr.com/HalfAuto/"
# baseUrl2 = "https://guanli.mayitest.cn/HalfAuto/"
# # socialDataOperation  社保   fundDataOperation  公积金
# kz = "socialDataOperation"
# # baseUrl=baseUrl1+kz
#
#
#
# we=writeExcel(header)
# cookie=we.getCookie(method,url,data)
# aaData=[]
# aaData=we.getSocialorFund(parms,baseUrl1,kz,cookie)


#excel中的内容是从第3行开始的
# i = 3
#打开需要拷贝的excel的内容
#old_excel=xlrd.open_workbook(gConst['xls']['C:\\liyanfile\\1.xlsx'], formatting_info=True)
# old_excel = xlrd.open_workbook('D:\\autoAPI\\1.xlsx', 'formatting_info=True')
# # 将操作对象拷贝变成可写的workbook对象
# new_excel = copy(old_excel)
# # 获取第一个excel的sheet内容
# ws = new_excel.get_sheet(0)
#
# for listJson in aaData:
#     name=listJson[2]
#     print(name)
#     p1=r"(?<=target='_blank'>).+(?=</a>)"
#     pattern1=re.compile(p1)
#     kfname=pattern1.findall(name)#提取姓名
#     strName="".join(kfname)#这个是把列表转化为字符串
#     kfCard=pattern1.findall(listJson[7])#提取身份证信息
#     strCard="".join(kfCard)#转化为字符串格式
#     we.writeExcel(listJson,cityCode,i,ws,kz,strName,strCard)
#     i=i+1
# new_excel.save('D:\\autoAPI\\fileName.xls')
# card=we.ReadExcel()
#
# print(card)






























