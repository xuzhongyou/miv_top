import psutil
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import time
def monitor():
    print('Start monitoring ------------------------- ')
    while(True):
        info = psutil.virtual_memory()
        info_dict ={}
        info_dict.setdefault('total',float(info.total)/(1024**3))
        info_dict.setdefault('available',int(info.available)/(1024**3))
        info_dict.setdefault('percent',float(info.percent))
        print('Monitoring---------------------------------',time.ctime())
        if info_dict['percent'] > 85:
            print('the csffm2 server is overloading-----------')
            mail_content = ''
            print(info_dict)
            for key in info_dict.keys():
                mail_content = mail_content+key+':\t'+str(info_dict[key])+'\n'
            mail_content = mail_content+'The server may be overloaded heavily, please pay more attention to memory.'
            print(mail_content)
            send_mail(mail_content)
            print("Start : %s" % time.ctime())
        time.sleep(200)


def send_mail(mail_content):
    sender_qq = '936214756'
    # pwd为qq邮箱的授权码
    pwd = 'lgkmzvgcovfgbfii'
    receiver = ['597372705@qq.com','936214756@qq.com',
                '52164500001@stu.ecnu.edu.cn','chenhe_Ashley@163.com'] #'936214756@qq.com'  #['936214756@qq.com',]#
    # 邮件的正文内容
    mail_content = mail_content
    # 邮件标题
    mail_title = 'server state'
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq + '@qq.com'

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = ','.join(receiver)
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

monitor()

# send_mail()

# for i in range(10):
#     send_mail(sender_qq=sender_qq, pwd=pwd, \
#               receiver=receiver, mail_title=mail_title, \
#               mail_content=mail_content)

