
# smtp是一种简单的邮件传输协议
# smtplib:封装了smtp协议
import smtplib
# 发送文本的包
from email.mime.text import MIMEText
from email.header import Header
# smtplib.SMTP()
'''
    邮箱163:smtp.163.com
    qq邮箱:smtp.qq.com  端口:SSL:465或普通:587
'''
# 创建邮箱服务器连接,smtplib.SMTP_SSL(邮箱连接地址,端口号)smtp.xx.com

con = smtplib.SMTP_SSL('smtp.qq.com', '465') # 增加了一个安全机制
# 登录邮箱
# 163的用户名和密码直接填写就行,如果是QQ邮箱,用户名邮箱号,密码授权码
con.login(user='1520147747@qq.com', password='sticzwhuilxlffbh')
# 发送者账号
sender = '1520147747@qq.com'
# 接受者账号
recevier = ['3093198971@qq.com', '1520147747@qq.com']

# 准备发送的_text邮件正文   _subtype= 文本类型 文本 html base64(二进制),plain默认纯文本格式  _charset 编码格式
message = MIMEText(_text='邮件正文', _subtype='plain', _charset='utf-8')
# 设置头部内容
# 设置头部标题
message['Subject'] = Header('文本标题', 'utf-8')
# 发件人
message['From'] = Header('沈华明1,<1520147747@qq.com>',  'utf-8')
# 收件人
message['To'] = Header('沈华明2',  'utf-8')
# 发送邮件
con.sendmail(sender, recevier, message.as_string())
htmlClod = '''
        html文本

'''
# 发送html文件
message = MIMEText(_text=htmlClod, _subtype='html', _charset='utf-8')

# 发送附件邮件 text文件, excel文件, pdf文件




