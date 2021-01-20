#! python3
# -*- coding:utf-8 -*-

import  requests
from package.test_api import testApi
import re
from package.writeExcel import writeExcel

'''修改测试环境中员工的详细信息'''
'''1、查询社保状态和账号并写入excel 2、读取excel的内容  3、然后修改测试库的信息'''

# baseUrl="https://guanli.mayitest.cn"
# header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest"}

#以最简单的方式获取cookie
# method="post"
# Rurl="/public/afs"
# data="{'username':'13469968124','password':'mayihr1234'}"  #这里是键值对的方式，字典
#
# ta=testApi(method,baseUrl+Rurl,eval(data)) #一定要注意这里字符串的转化
# rs=ta.testInterface
# cookie=rs.cookies.get_dict()

#修改员工详情(这个是针对测试环境中没有的员工)
def Edit(baseUrl,header,cookie):
    we=writeExcel(header)
    fileName = r'D:\\autoAPI\\fileName.xls'
    rows = we.GetRows(fileName)
    i=3
    print(rows)
    while(i<rows):
        params = we.ReadExcel(i)
        # print("测试场景")
        # print(params)
        if params[4]=="--":
            i = i + 1
            continue

        yg_id, uid = Select(params[0],baseUrl,header,cookie)

        #这里主要是修改减员数据
        # ygIDs=[325841]
        # uids=[178231]
        # yg_id=ygIDs[i-3]
        # uid=uids[i-3]
        # print(ygIDs)
        # print(yg_id)


        #户口类型
        if params[1] == "本地城镇":
            yg_hk_type = 1
        elif params[1] == "本地农村":
            yg_hk_type = 2
        elif params[1] == "外地城镇":
            yg_hk_type = 3
        elif params[1] == "外地农村":
            yg_hk_type = 4
        elif params[1] == "外籍人员":
            yg_hk_type = 5


        #社保缴纳规则
        social_rule=""
        if params[2] == "非深户+医疗一档": #深圳的缴纳规则
            social_rule = 64
        elif params[2] == "非深户+医疗二档":
            social_rule = 65
        elif params[2] == "非深户+医疗三档":
            social_rule = 66
        elif params[2] == "深户+医疗一档":
            social_rule = 63
        elif params[2] == "五险":  #上海的缴纳规则
            social_rule = 54
        elif params[2] == "五险（外农）":
            social_rule = 232
        elif params[2] == "外农缴纳规则":
            social_rule = 55
        elif params[2] == "广州社保规则":  #广州的缴纳规则
            social_rule = 74
        elif params[2] == "城保": #北京的缴纳规则
            social_rule = 60
        elif params[2] == "农保":
            social_rule = 61

        # print("sss"+params[4])
        #社保缴纳状态
        if params[4] == "在当地缴过":
            status = 1
        elif params[4] == "未在当地缴过":
            status = 2


        #公积金缴纳状态
        if params[7] == "在当地缴过":
            fstatus = 2
        elif params[7] == "未在当地缴过":
            fstatus = 3

        #城市编码
        if params[6] == "深圳":
            yg_city=45
        elif params[6] == "天河区":
            yg_city = 1000
        elif params[6] == "上海市":
            yg_city = 20
        elif params[6] == "海淀":
            yg_city = 1
        elif params[6] == "朝阳":
            yg_city = 17
        elif params[6] == "海淀5+5":
            yg_city = 1015



        #社保账号
        yg_social_acc=""
        if params[5] != "--":
            yg_social_acc =params[5]
        # print(yg_social_acc)
        #公积金账号
        yg_fund_acc=""
        if params[8] != "--":
            yg_fund_acc =params[8]

        #社保和公积金是否外包
        is_pay_social=0
        if params[9]==1:
            is_pay_social=1

        is_pay_fund=0
        if params[10]==1:
            is_pay_fund=1

        Frule=""
        if params[11]=="北京公积金缴纳规则5+5":
            Frule=237
        if params[11]=="广州公积金规则":
            Frule=73
        if params[11]=="个人和公司各缴5%":
            Frule = 58
        if params[11]=="深圳公积金12+12":
            Frule = 236
        if params[11] == "上海公积金":
            Frule = 57
        if params[11] == "北京公积金缴纳规则":
            Frule = 56
        if params[11] == "北京公积金缴纳规则12+12":
            Frule = 239
        url = "/yg/editSocialPost"
        aa = {
            "yg_id": yg_id,
            "yg_city": yg_city,  # 城市编码  手工修改
            "yg_hk_type": yg_hk_type,  # 户口类型
            "yg_pay_type": 1,  # 员工付款类型  固定
            "yg_is_social": params[9],  # 是否缴纳社保
            "yg_social_self": params[3],  # 社保基数
            "social_rule": social_rule,  # 社保规则
            "is_pay_social": is_pay_social,  # 是否外包 固定
            "social_status": status,  # 社保状态
            "yg_social_acc": str(yg_social_acc),  # 社保账号
            "social_number": str(yg_social_acc),  # 社保账号
            "street_personnel": 1,  # 街道人员 固定
            "yg_is_fund": params[10],  # 是否缴纳公积金
            "yg_fund_self": params[12],  # 公积金基数
            "social_start": "2018-12",  # 社保起始月份 固定
            "fund_start": "2018-12",  # 公积金起始月份 固定
            "fund_rule": Frule,  # 公积金规则 固定
            "is_pay_fund": is_pay_fund,  # 是否公积金外包 固定
            "fund_status": fstatus,  # 公积金状态
            "yg_fund_acc": str(yg_fund_acc),  # 公积金账号
            "registration_number": "",  # 转出登记号 固定
            "uid": uid}  # 公司的UID  手工进行修改

        r = requests.post(baseUrl + url, headers=header, cookies=cookie, data=aa)
        # print()
        # EditInfo(yg_name, yg_phone, yg_identity, yg_id, yg_gender)
        # print(params[13],params[14],params[0],yg_id,params[15])
        # --------------------------------------------------- #
        # EditInfo(params[13],params[14],params[0],yg_id,params[15])
        # ---------------------------------------------------#
        # print(r.text)
        i=i+1
        # print(i)
        # print(baseUrl)
        # print(uid+yg_id)


#字符串的提取
def ZfcTQ(str):
    p1=r"(?<=<a href=').+(?=target='_blank'>)"
    pattern1=re.compile(p1)
    tqID=pattern1.findall(str)#提取姓名
    tqYgID="".join(tqID).replace("\'","").split("/")[4]#提取字符串中的ID号
    return tqYgID


#根据身份证ID查询ygID
def Select(cardID,baseUrl,header,cookie):
    #根据身份证号查询员工信息ygID
    url = "/Yg/ygList/"
    dd={"keyword":cardID,"is_search":1}
    r=requests.get(baseUrl+url,headers=header,cookies=cookie,params=dd)
    str= r.json()
    count=len(str["aaData"])
    if count==1:
        a = str["aaData"][0]
    else:
        a = str["aaData"][count-1]
    ygID=ZfcTQ(a[0])
    Uid=ZfcTQ(a[1])
    # print(ygID+Uid)
    return ygID,Uid

#根据身份证ID查询ygID
def SelectYG(cardID,mheader,vvcookie,baseUrl):
    #根据身份证号查询员工信息ygID
    url = "/Yg/ygList/"
    dd={"keyword":cardID,"is_search":1}
    # print(cardID)
    r=requests.get(baseUrl+url,headers= mheader,cookies =vvcookie,params=dd)

    str= r.json()
    # print(str)
    count=len(str["aaData"])
    if count==1:
        a = str["aaData"][0]
    else:
        a = str["aaData"][count-1]
    # print(a)
    return a

#提取规则
def ZfcTQUrl(str):
    p1=r"(?<=<a href=').+(?=target='_blank'>)"
    pattern1=re.compile(p1)
    tqID=pattern1.findall(str)#提取姓名
    tqYgID="".join(tqID).replace("\'","")#提取字符串中的ID号
    return tqYgID


#修改个人信息部分(姓名，性别，手机号，身份证，学历)
def EditInfo(yg_name,yg_phone,yg_identity,yg_id,yg_gender):
    url="/yg/editPost"
    data={"yg_name":yg_name,
          "yg_phone":yg_phone,
          "yg_id":yg_id,
          "yg_gender":yg_gender,
          "id_type":1,
          "yg_identity":yg_identity}
    r = requests.post(baseUrl + url, headers=header, cookies=cookie, data=data)
    #获取返回的结果，是成功还是失败
    print("jinru")
    print(r.text)
    print("修改个人身份信息成功")

# bb=SelectYG("142429199301232111",header,cookie)
# print(bb)

#获取正式环境员工的社保缴纳状况及账号信息
#http://guanli.mayitest.cn/yg/editSocial/id/338078
#提取社保缴纳状态及电脑号
#https://guanli.mayitest.cn/yg/detail/id/338078
#
# Edit()
# print("结束")


baseUrl="https://guanli.mayitest.cn"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest"}

#以最简单的方式获取cookie
method="post"
Rurl="/public/afs"
data="{'username':'13469968124','password':'mayihr1234'}"  #这里是键值对的方式，字典

ta=testApi(method,baseUrl+Rurl,eval(data)) #一定要注意这里字符串的转化
rs=ta.testInterface
cookie=rs.cookies.get_dict()


# print("aaaa")
# Edit(baseUrl,header,cookie)
# print("bbb")
