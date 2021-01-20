import smtplib
from email.mime.text import MIMEText  # MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件
from email.mime.application import MIMEApplication
from email.header import Header

smtpserver = 'smtp.163.com'
user = 'liyan_happy2009@163.com'
password = 'yanzi852745'
sender = 'liyan_happy2009@163.com'
receiver = '277817066@qq.com'

subject = '我测试内容'

att = MIMEApplication(open("D:\\autoAPI\\cookie.txt", 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename="D:\\autoAPI\\cookie.txt")

f = open('D:\\autoAPI\\cookie.txt', 'rb')
mail_body = f.read()
f.close()
msg = MIMEText(mail_body, 'html', 'utf-8')

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(msg)
msgRoot.attach(att)

smtp = smtplib.SMTP_SSL()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()