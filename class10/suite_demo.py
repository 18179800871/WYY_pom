'''

    unittest测试套件(可以理解为一个list集合)
    unittest中的一大特色 测试套件与测试运行器
    默认在框架中所有的用例都会全部执行,切实依照unittest的规则来进行排序执行的
    例如
       冒烟测试
        针对特定的流程执行测试
    应用一定是根据unittest来执行的
    套件的运行是一定需要通过运行器啦进行操作的,默认的运行器是TextTestRunner(),
    运行套件时,用例的顺序是基于套件在添加用例时的顺序来定的
    测试运行器:支持外部的第三方运行器,例如HTMLTestRunner
    HTML无法通过pip安装,本身是针对2 版本的python啦进行实现的

'''
# from HTMLTestRunner import HTMLTestRunner #导入包
from HTMLTestReportCN import HTMLTestRunner
import os
import unittest

# 添加用例到套件执行

# 创建套件
suite = unittest.TestSuite()
# 添加用例到套件中:添加单个测试用例
# suite.addTest(UnitDemo('test_01'))
# suite.addTest(UnitDemo('test_02'))
# # suite.addTest(UnitDemo('test_03'))

# 批量添加用例到套件
# cases = [UnitDemo('test_01'),UnitDemo('test_02')]
# suite.addTests(cases)

# 批量添加测试用例:直接添加一整个unittest类(通过Testcas对象添加)
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
# 通过类名添加
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo'))
# 通过文件名来进行添加
# 首先定义用例获取路径
case_dir = './'
# 基于路径来用例,组合成套件 常用方法
disciver = unittest.defaultTestLoader.discover(start_dir=case_dir , pattern='unit*.py')
# # 运行套件
# runner = unittest.TextTestRunner()
# runner.run(disciver)

#运行HTMLTestRunner生成测试报告
# 设置保存路径
report_path = './report/'
#报告的文件名称
report_file = report_path + 'report1.html'
# 判断保存路径是否存在
if not os.path.exists(report_path):
    os.mkdir(report_path)
with open(report_file , 'wb') as file:
    runner = HTMLTestRunner(stream=file,title='第一份测试报告',description='这是测试报告的描述',tester='沈华明')
    runner.run(disciver)
