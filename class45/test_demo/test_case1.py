import pytest
'''
    pytest默认寻找当前路径下的所有文件与子文件夹以test开头的文件夹,文件,函数作为识别对象
    pytest默认不输出任何打印信息,如果要看打印信息,需要在运行时添加-s的指令
    多条函数在main函数中用,号分隔,在命令行用空格分隔
'''

'''
    在class中前置后置函数的运行顺序等级
    setup class
    setup method
    setup
    teardown
    teardown method
    teardown class
'''
'''
    markers = @pytest.mark.webui      装饰器@pytest.mark.的配置
    pytset.ini文件配置 必须在根目录下
    python_files = 文件名*.py test.py   读取文件命名
    python_classse = class名         指定运行类名
    testpaths =  ./               指定读取测试用例的路径
    python_functions = 指定名称         修改用例开头名称
    log_cli = True                      测试用例的运行结果显示的更完善
    addopts = -s -v --html=./report/report.html --self-contained-html                      添加运行指令
    
'''
'''
    @pytest.mark.parametrize  pytest中的数据驱动
    所有的数据最后都会形成一个list的格式传递到用例中



'''

# 前置与后置条件

def setup_function(): # 类级别
    print('function')


def teardown_function():
    print('tfunction')

def setup_module():# 模块级别
    print('module')


def teardown_module():
    print('tmodule')



def test_02(xuzhu):
    print('test_02')

def test_01(xuzhu01):
    assert xuzhu01 == 1, '失败'



# pytest中class对象的定义:建议以test开头
class TestDemo():
    def test_d1(self):
        print('test1')
    def test_d2(self):
        print('test2')






# pytest运行主入口:
if __name__ == '__main__':
    pytest.main(['-s', '-v', '-rA', '-q', 'test_case1.py::test_02' ])














































