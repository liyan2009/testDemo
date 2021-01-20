#! python3
# -*- coding:utf-8 -*-

import urllib.request
import http.cookiejar
from urllib import parse

'''这个模块主要是模拟登陆，把保存的cookie文件夹中'''

#cookie的文件路径
cookie_file='D:\\autoAPI\\intoCookie.txt'
#声明一个CookieJar对象实例来保存cookie
cookie=http.cookiejar.MozillaCookieJar(cookie_file) #这个是保存在文件中
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
handler=urllib.request.HTTPCookieProcessor(cookie)
# 通过CookieHandler创建opener
opener=urllib.request.build_opener(handler)

url="https://guanli.mayihr.com/public/afs"
login_data={}
login_data["username"]="13469968124"
login_data["password"]="mayihr1234"
# 使用urlencode方法转换标准格式
logingpostdata = parse.urlencode(login_data).encode('utf-8')
userAgent=" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
head = {'User-Agnet': userAgent, 'Connection': 'keep-alive'}

print(logingpostdata)
request=urllib.request.Request(url=url,data=logingpostdata,headers=head)


response = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    #读取cookie中的内容
    print('%s=%s' % (item.name, item.value))

