#!python3
#coding:utf-8

import configparser
import  os
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import  MIMEMultipart
# import codecs

#获取对应文件夹
proDir=os.path.split(os.path.realpath(__file__))[0]

#获取上级目录
curDir=os.path.dirname(proDir)
#获取配置文件夹所在的路径
configPath=os.path.join(curDir,"config\\config.ini")

class ReadConfig:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath,encoding="utf-8-sig")

    def get_email(self,name):
        value=self.cf["EMAIL"][name]
        return value


    def get_http(self,name):
        # value=self.cf.get("testServer",name)
        value=self.cf["testServer"][name]
        return value


# rc=ReadConfig()
#
# email=rc.get_email("mail_host")
# print(email)

'''
conf=configparser.ConfigParser()
conf.read("C:\\Users\\liyan\\PycharmProjects\\Selnium_SaasWeb\\config\\config.ini",encoding="utf-8-sig")
sections=conf.sections()
lists=conf.items("EMAIL")

mail_host=conf.get("EMAIL","mail_host")
mail_user=conf.get("EMAIL","mail_user")
mail_pwd=conf.get("EMAIL","mail_pwd")
mail_port=conf.get("EMAIL","mail_port")
receiver=conf.get("EMAIL","receiver")
# 从config文件中读取有多种方式
# subject=conf.get("EMAIL","subject")
subject=conf["EMAIL"]["subject"]
content=conf.get("EMAIL","content")
print('主题',subject)

#这里发送的邮件不带附件
msg=MIMEText(content)
msg['Subject']=subject
msg['From']=mail_user
msg['To']=receiver

smtp = smtplib.SMTP( mail_host ,port=mail_port)
smtp.login(mail_user,mail_pwd)
smtp.sendmail(mail_user,receiver,msg.as_string())


# #发送带附件的邮件
# sendFile=open("D:\\autoAPI\\cookie.txt","r").read()
# attr=MIMEText(sendFile,"base64","utf-8")
# attr["content-Type"]="application/octet-stream"
# attr["content-Disposition"]="attachment;filename='cookie.txt'"
#
# msgRoot=MIMEMultipart("related")
# msgRoot["Subject"]="我的邮件内容"
# msgRoot.attach(attr)
#
# smtp=smtplib.SMTP(mail_host,port=25)
#
# smtp.login(mail_user,mail_pwd)
# smtp.sendmail(mail_user,receiver,attr.as_string())

smtp.quit()
print("邮件发送完毕")

'''


