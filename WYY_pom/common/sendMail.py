# -*- coding:utf-8 -*-
# 作者：NoamaNelson
# 日期：2021/3/4 11:16
# 文件名称：sendMain.py
# 作用：封装邮件服务模块

import time
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email
import os


def send_main(file_path, mail_to='152014774@qq.com'):
    mail_from = '1520147747@qq.com'
    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    # msg = email.MIMEMultipart.MIMEMultipart()
    msg = MIMEMultipart()

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    # 读入文件内容并格式化
    data = open(file_path, 'rb')
    # file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()

    # email.Encoders.encode_base64(file_msg)
    encoders.encode_base64(file_msg)

    # 设置附件头
    basename = os.path.basename(file_path)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    msg.attach(file_msg)
    print(u'msg 附件添加成功')

    msg1 = MIMEText(mail_body, "html", 'utf-8')
    msg.attach(msg1)

    if isinstance(mail_to, str):
        msg['To'] = mail_to
    else:
        msg['To'] = ','.join(mail_to)
    msg['From'] = mail_from
    msg['Subject'] = u'网易云测试WEBUI测试报告'
    msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S')

    print(msg['date'])

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com',)
    smtp.login('1520147747@qq.com', 'sticzwhuilxlffbh')  # 登录账号和密码（密码为之前申请的授权码）
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')

# if __name__=='__main__':
#     send_main(r'D:\Automation\WYY_pom\report\report1.html')
