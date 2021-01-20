#! python3
#! -*- coding:utf-8 -*-

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

'''
1、发送邮件，需要与邮件服务器建立连接
2、发邮件：发件人、收件人、主题、内容、附件
3、发送
4、2018-10-31 对发送邮件进行改造
'''
class SendEmail(object):
    def send_email(self,attach_xlsx,sender,receiver,pwd,content,mailhost,subject,myname,attach_jpg=""):
        msg = email.mime.multipart.MIMEMultipart() #邮件体对象

        msg['Subject'] = subject #邮件主题
        msg['From'] = sender   #邮件发送人
        msg['To'] =receiver    #邮件接收者


        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)

        # 发送带excel附件
        xlsxpart = MIMEApplication(open(attach_xlsx, 'rb').read())
        xlsxpart.add_header('Content-Disposition','attachment',filename=myname) #只有这里的文件名未参数化
        msg.attach(xlsxpart)

        smtp = smtplib.SMTP_SSL() #发送有附件的必须要用这个方法

        smtp.connect(mailhost)  # 链接服务器
        # print("成功")
        smtp.login(sender, pwd)#输入登录名+密码
        # print("成功")
        smtp.sendmail(sender,receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功 yyy ydfjdkgj email has send out !')