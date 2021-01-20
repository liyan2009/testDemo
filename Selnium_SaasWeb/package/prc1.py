#! python3
# -*- coding:utf-8 -*-

import json
import requests

import re


aa = 'afebb'
bb = '你'
print(len(aa))
print(len(bb))

name = "<a href='/yg/detail/id/559372' target='_blank'>李娇</a>"

p1 = r"(?<=target='_blank'>).+(?=</a>)"
pattern1 = re.compile(p1)
kfname = pattern1.findall(name)  # 提取姓名
strName = "".join(kfname)

print(strName)

#字符串转化
def better_change(json_str):
    return json.dumps(json_str,ensure_ascii=False)


head = { 'Connection': 'keep-alive','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',"X-Requested-With":"XMLHttpRequest"}
pwd=None
data={"username":"13469698124","password":pwd}
url="https://guanli.mayihr.com/public/afs"
ta = requests.post(url,data=data,headers=head)
print(ta.url)
# print(ta.status_code)

s =ta.json()
print(ta.json())
# a=None
# print(type(a))



