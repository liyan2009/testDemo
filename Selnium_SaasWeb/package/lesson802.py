#! python3
# coding:utf-8
import requests

url="http://www.baidu.com"
par={"wd":"测试网速"}
r=requests.get(url,params=par)
#获取当前返回内容按照什么方式编码
print(r.encoding)
print(r.status_code)
#先按照指定的编码编码，然后进行解码
print(r.text.encode("ISO-8859-1").decode("utf-8"))

