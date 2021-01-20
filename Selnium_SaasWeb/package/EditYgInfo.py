#! python3
# -*- coding:utf-8 -*-
import requests,json,re #使用json，正则表达式
from package.writeExcel import writeExcel

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
baseUrl = "https://guanli.mayitest.cn"
method="post"
Rurl="https://guanli.mayitest.cn/public/afs"
data="{'username':'13469968124','password':'mayihr1234'}"
we = writeExcel(header)
ycookies=we.getCookie(method,Rurl,data)
print(ycookies)
editUrl="http://guanli.mayitest.cn/yg/editPost"

#读取excel的内容
fileName = r'D:\\autoAPI\\fileName.xls'
rowCount = we.GetRows(fileName)
i=3
while (i < rowCount):
    ygDetailinfo=we.ReadExcel(i)
    # print(ygDetailinfo)
    # print(ygDetailinfo[16])
    data={"yg_id":ygDetailinfo[16],"yg_name":ygDetailinfo[13],"yg_gender":ygDetailinfo[15],"yg_phone":ygDetailinfo[14],"id_type":1,"yg_identity":ygDetailinfo[0],"idcard_expire_date":"",
          "yg_email":"","tax_type":1 ,"yg_xueli":5,"yg_nation":1}
    r=requests.post(editUrl,data, cookies=ycookies,headers=header)
    print(r.status_code)
    print(r.text)
    i = i + 1;