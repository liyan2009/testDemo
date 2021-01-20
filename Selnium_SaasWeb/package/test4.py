#! python3
import  json

# -*- coding: utf-8 -*-
import requests ,bs4,json,re

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36","Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"}
'''从txt文件中读取cookie相关信息'''
f=open(r'D:\\autoAPI\\cookie.txt','r')
cookies={}
for line in f.read().split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value

cityCode=45
yg_name=""
sub_status=""
#设置参数信息
parms={"city":cityCode,"yg_status":"","yg_name":yg_name,"sub_status":sub_status}
baseUrl="https://guanli.mayihr.com/HalfAuto/"
kz="fundDataOperation"
url=baseUrl+kz
print(url)
r=requests.get(url,headers=header,cookies = cookies,params=parms)
#str=r.content().decode('unicode_escape')
str=r.json()#转化为json格式

print(r.json())









