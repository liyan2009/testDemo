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
    def send_email(self,attach_xlsx,attach_jpg,sender,receiver,pwd,content,mailhost,subject,myname):
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



        #jpg图片附件
        # jpgpart = MIMEApplication(open(attach_jpg, 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='1.jpg')
        # msg.attach(jpgpart)

        #smtp = smtplib
        #smtp=smtplib.SMTP() #发送普通的内容用这个方法
        smtp = smtplib.SMTP_SSL() #发送有附件的必须要用这个方法
        # smtp.set_debuglevel(1)
        # print("成功")
        # smtp.connect('smtp.163.com')#链接服务器
        smtp.connect(mailhost)  # 链接服务器
        # print("成功")
        smtp.login(sender, pwd)#输入登录名+密码
        # print("成功")
        smtp.sendmail(sender,receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功email has send out !')


#测试代码
# se=SendEmail()
# sender='liyan_happy2009@163.com'
# receiver='277817066@qq.com'
# pwd='yanzi852745'
# content='我的家乡'
# mailhost='smtp.163.com'
# subject="hahha "
# se.send_email("C:/Users/liyan/PycharmProjects/Selnium_SaasWeb/result/report.html","D:\\autoAPI\\1.jpg",sender,receiver,pwd,content,mailhost,subject,"report.html")