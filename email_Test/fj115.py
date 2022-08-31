# 发送附件邮件
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
# 文本
from email.mime.text import MIMEText
# 创建邮箱服务器连接,smtplib.SMTP_SSL(邮箱连接地址,端口号)smtp.xx.com

con = smtplib.SMTP_SSL('smtp.qq.com', '465') # 增加了一个安全机制
# 登录邮箱
# 163的用户名和密码直接填写就行,如果是QQ邮箱,用户名邮箱号,密码授权码
con.login(user='1520147747@qq.com', password='sticzwhuilxlffbh')
# 发送者账号
sender = '1520147747@qq.com'
# 接受者账号
recevier = ['3093198971@qq.com', '1520147747@qq.com']




# 发送附件
# 实例化附件 相当于创建了一个信封
message = MIMEMultipart()
# 文件 rb读
content = open(r'D:\Automation\WEB _自动化\class10\report\report1.html', 'rb').read()
# 把读取出来的内容放在文本中 相当于信纸
file = MIMEText(content, 'base64', 'utf-8')
# 给信纸取名字
file['Content-Disposition'] = 'attachment;filename"name"'
# 把信纸放到信封中
message.attach(file)

# 设置头部内容
message['Subject'] = Header('附件标题', 'utf-8')
# 发件人
message['From'] = Header('沈华明1,<1520147747@qq.com>',  'utf-8')
# 收件人
message['To'] = Header('沈华明2',  'utf-8')
# 发送邮件
con.sendmail(sender, recevier, message.as_string())







