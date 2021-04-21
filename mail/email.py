import psutil
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

'''
Todo:
    1.  MIMEText传入一个html
'''

def send_mail(mail_content,email_title,sender,receiver=[],pwd='',host_server='smtp.qq.com'):
    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender, pwd)
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(email_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = ','.join(receiver)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()