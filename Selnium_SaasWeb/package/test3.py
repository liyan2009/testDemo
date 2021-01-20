#! python3
# -*- coding:utf-8 -*-
import requests,json,re #使用json，正则表达式
import  xlwt #写excel
import  xlrd #读取excel
from xlutils.copy import copy  #修改excel
import datetime as dt
from bs4 import BeautifulSoup  #解析html及xml文件

import http.cookiejar
from package.test_api import testApi


#从txt文件中读取cookie
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36","Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"}

#这里是手工把cookie信息copy到txt的
'''
f=open(r'D:\\autoAPI\\cookie.txt','r')
cookies={}
for line in f.read().split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value
'''

'''
#加载cookie，这里是先把cookie文件，然后从文件中读取出来
cookie_file='D:\\autoAPI\\intoCookie.txt'
cookie=http.cookiejar.MozillaCookieJar(cookie_file)
mycookie={}
cookie.load(cookie_file,ignore_discard=True, ignore_expires=True)
for item in cookie:
    print('%s=%s' % (item.name, item.value))
    mycookie[item.name]=item.value
print('测试比对%s'%mycookie)
'''

#以最简单的方式获取cookie
method="post"
url="https://guanli.mayihr.com/public/afs"
data="{'username':'13469968124','password':'mayihr1234'}"  #这里是键值对的方式，字典

ta=testApi(method,url,eval(data)) #一定要注意这里字符串的转化
rs=ta.testInterface
ycookies=rs.cookies.get_dict()
print('打印的值%s' %ycookies)

#郭彤
# https://guanli.mayihr.com/HalfAuto/fundDataOperation/?city=20&yg_status=is_back&hk_type=&sub_status=&op_status=&is_daiguan=2&user_id=&yg_name=%E5%91%A8%E9%80%B8%E8%96%87
#参数信息配置
cityCode=1000
yg_name=""
iDisplayStart=""
user_id=""
user_uid=""
op_status=""
yg_status="1"
iDisplayLength="20"
#设置参数信息
parms={"city":cityCode,"yg_status":yg_status,"yg_name":yg_name,"sub_status":"","iDisplayStart":iDisplayStart,"is_daiguan":"","user_uid":user_uid,"user_id":user_id,"op_status":op_status,"yg_status":yg_status,"iDisplayLength":iDisplayLength,"is_daiguan":1}
baseUrl1="https://guanli.mayihr.com/HalfAuto/"
baseUrl2="https://guanli.mayitest.cn/HalfAuto/"
#socialDataOperation  社保   fundDataOperation  公积金
kz="fundDataOperation"
url=baseUrl1+kz
r=requests.get(url,headers=header,cookies = ycookies,params=parms)

print(r.url)
#str=r.content().decode('unicode_escape')
str=r.json()#转化为json格式
# #获取dict的键值对
# print(str.keys())
# #打印出获取的结果
print(r.json())
#打印出对应的值
print(str["aaData"])#提取所需要的list信息

#把读取的值写入到excel
def writeExcel(listJson,id,i,ws):
    ws.write(i, 0, strName)#姓名
    ws.write(i, 1, '身份证')
    ws.write(i, 2, strCard)#身份证
    ws.write(i, 4, '全职')
    style=xlwt.easyxf(num_format_str='yyyy/m/d')
    ws.write(i, 5, dt.date.today(),style)
    ws.write(i, 8, '10')
    ws.write(i, 10, '各缴')

    if id in(1,17,1015):#社保需要填的值
        if kz == "socialDataOperation":
            ws.write(i, 11, '缴纳')
            ws.write(i, 16, listJson[13])  # 规则
            ws.write(i, 17, listJson[15])  # 基数
            ws.write(i, 14, listJson[12])  # 户口类型
        else:        #公积金需要填的值
            ws.write(i, 19, '缴纳')
            ws.write(i, 20, listJson[14])  # 规则
            ws.write(i, 21, listJson[16])  # 基数
            ws.write(i, 14, listJson[13])  # 户口类型
        proviceName = '直辖市北京'
        if id==1:
            cityName='海淀'
        elif id==1015:
            cityName = '海淀5+5'
        else:
            cityName='朝阳'
    #如果是上海
    if id==20:
        if kz == "socialDataOperation":
            ws.write(i, 14, listJson[14])  # 户口类型
            ws.write(i, 11, '缴纳')
            ws.write(i, 16, listJson[15])  # 规则
            ws.write(i, 17, listJson[17])  # 基数
        else:
            ws.write(i, 14, listJson[13])  # 户口类型
            ws.write(i, 19, '缴纳')
            ws.write(i, 20, listJson[14])  # 规则
            ws.write(i, 21, listJson[16])  # 基数
        proviceName='直辖市上海'
        cityName='上海市'
    #这里是深圳
    if id==45:
        if kz == "socialDataOperation":
            ws.write(i, 14, listJson[13])  # 户口类型
            ws.write(i, 11, '缴纳')
            ws.write(i, 16, listJson[14])  # 规则
            ws.write(i, 17, listJson[16])  # 基数
        else:
            ws.write(i, 14, listJson[12])  # 户口类型
            ws.write(i, 19, '缴纳')
            ws.write(i, 20, listJson[13])  # 规则
            ws.write(i, 21, listJson[15])  # 基数
        proviceName='广东省深圳'
        cityName='深圳'
    #这个是广州
    if id==1000:
        ws.write(i, 14, listJson[11])  # 户口类型
        if kz == "socialDataOperation":
            ws.write(i, 11, '缴纳')
            ws.write(i, 16, listJson[12])  # 规则
            ws.write(i, 17, listJson[14])  # 基数
        else:
            ws.write(i, 19, '缴纳')
            ws.write(i, 20, listJson[12])  # 规则
            ws.write(i, 21, listJson[14])  # 基数
        proviceName='广东省广州'
        cityName='天河区'
    #西城
    if id==1008:
        if kz == "socialDataOperation":
            ws.write(i, 11, '缴纳')
            ws.write(i, 16, listJson[13])  # 规则
            ws.write(i, 17, listJson[15])  # 基数
            ws.write(i, 14, listJson[12])  # 户口类型
        else:        #公积金需要填的值
            ws.write(i, 19, '缴纳')
            ws.write(i, 20, listJson[14])  # 规则
            ws.write(i, 21, listJson[16])  # 基数
            ws.write(i, 14, listJson[13])  # 户口类型
        proviceName='直辖市北京'
        cityName='西城托管'


    style1=xlwt.easyxf(num_format_str='m-yy')
    ws.write(i, 12, proviceName)
    ws.write(i, 13, cityName)
    ws.write(i, 18, dt.datetime.today(),style1)#缴纳月份
    ws.write(i, 22, dt.datetime.today(),style1)#缴纳月份
    ws.write(i, 23, ygInfo[0]) # 手机号
    ws.write(i, 24, '否')  #缴纳月份
    # ws.write(i, 24, ygInfo[0])  # 社保缴纳状态
    ws.write(i, 25, ygInfo[1])  # 社保缴纳状态
    ws.write(i, 26, ygInfo[2])  # 社保账号
    ws.write(i, 27, ygInfo[3])  # 公积金缴纳状态
    ws.write(i, 28, ygInfo[4])  # 公积金账号

    #这里是把公积金信息给不上去

    if ygInfo[7]=="不缴":
        ws.write(i, 19, "") # 公积金是否缴纳
        ws.write(i, 20, "") # 公积金规则
        ws.write(i, 21, "")  # 公积金是否基数


    # ws.write(i, 19, ygInfo[7])  # 公积金是否缴纳
    # ws.write(i, 20, ygInfo[6])  # 公积金规则
    # ws.write(i, 21, ygInfo[5])  # 公积金是否基数


#提取手机号，社保状态和公积金状态,并写入到excel表中

def getPhone(ygUID):
    baseurl="https://guanli.mayihr.com/"
    reqUrl=baseurl+ygUID
    # print(reqUrl)
    rs=requests.get(reqUrl,headers=header,cookies = ycookies)
    html=rs.text
    soup=BeautifulSoup(html,'html.parser')
    content=soup.find_all("div", attrs={"class": "col-sm-8 left"},limit=3)
    # print(content)
    contentSocial = soup.find_all("div", attrs={"class": "col-sm-4 left"})
    #公积金状态是否缴纳
    contentFJN=soup.find_all("div", attrs={"class": "col-sm-4 left text-primary"})
    # print(contentFJN)
    fundWB=contentFJN[2].get_text().strip() #公积金缴纳
    contentFundRule=soup.find_all("div", attrs={"class": "col-sm-6 left"}) #公积金规则
    # print(contentSocial)
    # contentSocial = soup.find_all("div", attrs={"class": "col-sm-4 left"}, limit=9)
    #这里是获取社保缴纳状态和社保账号
    socialStatus=contentSocial[1].get_text().strip()
    socialAcct = contentSocial[3].get_text().strip()
    #这里获取公积金缴纳状态和公积金账号
    fundself=contentSocial[5].get_text().strip() #公积金基数
    fundStatus=contentSocial[6].get_text().strip() #公积金状态
    fundAcct = contentSocial[8].get_text().strip() #公积金账号
    #提取手机号
    strPhone=content[2].get_text().strip()
    fundRule=contentFundRule[0].get_text().strip()  #公积金规则


    #这里新增了公积金基数，公积金是否缴纳，公积金是否外包，公积金类型
    return strPhone,socialStatus,socialAcct,fundStatus,fundAcct,fundself,fundRule,fundWB


#excel中的内容是从第3行开始的
i = 3
#打开需要拷贝的excel的内容
#old_excel=xlrd.open_workbook(gConst['xls']['C:\\liyanfile\\1.xlsx'], formatting_info=True)
old_excel = xlrd.open_workbook('D:\\autoAPI\\1.xlsx', 'formatting_info=True')
# 将操作对象拷贝变成可写的workbook对象
new_excel = copy(old_excel)
# 获取第一个excel的sheet内容
ws = new_excel.get_sheet(0)

for listJson in str["aaData"]:
    name=listJson[2]
    p1=r"(?<=target='_blank'>).+?(?=</a>)"
    pattern1=re.compile(p1)
    kfname=pattern1.findall(name)#提取姓名
    strName="".join(kfname)#这个是把列表转化为字符串
    kfCard=pattern1.findall(listJson[7])#提取身份证信息
    strCard="".join(kfCard)#转化为字符串格式
    #提取员工的编号
    p2=r"(?<=<a href=').+(?=target='_blank'>)"
    pattern2 = re.compile(p2)
    url=pattern2.findall(name)
    ygID = "".join(url).replace("\'","")
    ygInfo=getPhone(ygID)
    writeExcel(listJson,cityCode,i,ws)
    i=i+1
new_excel.save('D:\\autoAPI\\fileName.xls')



































