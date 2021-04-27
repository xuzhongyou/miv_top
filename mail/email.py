import psutil
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate
'''
Todo:
    1.  MIMEText传入一个html
'''
table_header = ['Name','Server_name','GPUs','Time','Running_time']

def write_table(table_header,table_data,fmt='html'):
    return tabulate(table_data, headers=table_header, tablefmt=fmt)

# text，html 都是由tabulate转换后得到string
def send_mail(text,html,email_title,sender,receiver=[],pwd='',host_server='smtp.qq.com'):
    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender, pwd)
    msg = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])
    msg["Subject"] = Header(email_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = ','.join(receiver)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()