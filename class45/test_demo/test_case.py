import pytest
'''
    pytest默认寻找当前路径下的所有文件与子文件夹以test开头的文件夹,文件,函数作为识别对象
    pytest默认不输出任何打印信息,如果要看打印信息,需要在运行时添加-s的指令
    多条函数在main函数中用,号分隔,在命令行用空格分隔
    命令行运行pytest指令: 直接
    -S 打印运行的用例
    -V 用于详细显示日志信息
    -rA 测试结果的简单统计

pytest中的setup和teardown:    一般可以通过一个配置文件直接进行管理: 配置文件命名一定要是conftest.py
    pytest生成测试报告: pytest-html测试报告模块 如果需要集成到邮件,就需要添加指令--self-contained-html
    安装 pytest html模块
    输入命令 pytest --html=./report/report.html --self-contained-html
'''


def test_02(xuzhu):
    assert xuzhu == 1, '失败'

def test_01():
    print('test_01')



# pytest运行主入口:
if __name__ == '__main__':
    # 运行其他的用例
    pytest.main(['-s', 'test_case.py::test_01'])














































