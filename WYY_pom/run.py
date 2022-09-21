from common.sendMail import send_main
import datetime
import time
from common.HTMLTestRunner import HTMLTestRunner
import os
import unittest
suite = unittest.TestSuite()
case_dir = './'
# 基于路径来用例,组合成套件 常用方法
disciver = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='unit*.py')
# 设置保存路径
report_path = './report/'
#报告的文件名称
report_file = report_path + time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time())) + 'report1.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)
with open(report_file , 'wb') as file:
    runner = HTMLTestRunner(stream=file, verbosity=1, title='AI中台接口测试报告', description='AI中台场景大黄蜂与卖货宝接入接口与大脑片区新增修改',
                            is_thread=False, retry=1, save_last_try=True)
    runner.run(disciver)
# send_main(report_file, mail_to=['1520147747@qq.com', 'shm147256@164.com'])
