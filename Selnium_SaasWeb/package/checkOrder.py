#! python3
# -*- coding:utf-8 -*-
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

def CheckOrderInfo(orderID,uid):
    #这边要审核的订单信息
    checkUrl="http://guanli.mayitest.cn/order/payinfo/order_id/260555/uid/8351"
    return  None ;