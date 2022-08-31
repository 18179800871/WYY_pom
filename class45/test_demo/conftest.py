'''
这是pytest中setup和teardown的配置文件 注意,文件名称一定是conftest,不能是其他的
scope参数定义的4种等级 默认是(function)
    session: 在本次session级别中只执行一次
    module: 在模块级别中只执行一次
    class: 在类级别中只进行一次
    function: 在函数级别中执行 ,每有一个函数就执行一次
调用@pytest.fixture(scope='参数定义的等级')



'''




import pytest
# 预制函数:用于前期的数据准备
# 定义一个基本的setup和teardown
@pytest.fixture()
def xuzhu():
   print('虚竹生病了')

@pytest.fixture()
def xuzhu01():
    return 1
