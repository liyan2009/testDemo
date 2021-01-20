#! python3
# -*-coding:utf-8 -*-


import  requests
from package.test_api import testApi
import re
from bs4 import BeautifulSoup


baseUrl="http://guanli.mayihr.com"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest"}

#以最简单的方式获取cookie
method="post"
Rurl="/public/afs"
data="{'username':'13469968124','password':'mayihr1234'}"  #这里是键值对的方式，字典
ta=testApi(method,baseUrl+Rurl,eval(data)) #一定要注意这里字符串的转化
rs=ta.testInterface
cookie=rs.cookies.get_dict()
print(cookie)

#查询正式库中的社保状态及社保账号
# ygUID="yg/detail/id/376235"
def getPhone(ygUID):
    baseurl="https://guanli.mayihr.com/"
    reqUrl=baseurl+ygUID
    # print(reqUrl)
    rs=requests.get(reqUrl,headers=header,cookies = cookie)
    html=rs.text
    soup=BeautifulSoup(html,'html.parser')
    content=soup.find_all("div", attrs={"class": "col-sm-8 left"},limit=3)
    # print(content)
    contentSocial = soup.find_all("div", attrs={"class": "col-sm-4 left"},limit=9)
    #这里是获取社保缴纳状态和社保账号
    socialStatus=contentSocial[1].get_text().strip()
    socialAcct = contentSocial[3].get_text().strip()
    #这里获取公积金缴纳状态和社保账号
    fundStatus=contentSocial[6].get_text().strip()
    fundAcct = contentSocial[8].get_text().strip()
    # print("社保状态："+socialStatus+"社保账号："+socialAcct+"公积金状态："+fundStatus+"公积金账号："+fundAcct)
    #提取手机号
    strPhone=content[2].get_text().strip()
    # print(strPhone)
    return strPhone,socialStatus,socialAcct,fundStatus,fundAcct

ygUID="yg/detail/id/376235"
aa=getPhone(ygUID)
print(aa[0])