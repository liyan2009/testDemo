from http import cookiejar
from  urllib import request

if __name__=='__main__':
    #申明一个cookie对象
    cookie=cookiejar.CookieJar()
    #创建处理cookie的
    handler=request.HTTPCookieProcessor(cookie)
    #使用handler创建opener
    opener=request.build_opener(handler)
    response=opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name)
        print(item.value)

