'''
    unittest测试框架的应用
        1.类名继承:unittest.TestCase
        2.测试用例都必须以test开头
        3.用例的运行顺序:unittest中有默认的用例加载顺序:0-9, A-Z , a-z
        4.所有前置后置条件都有等级存在,class级别,method级别:前置与后置函数,有且只有一次
                    method级别前置后置:
                        与用例关联,每一条用例运行前都会执行前置,运行后会执行后置
                    class级别的前置后置:
                        1.必须定义装饰器
                        2.在开局只运行一次
        5.cls对象只在class级别的前置条件中调用,用例中调用使用self调用
        6.修改cls值,在全局生效,需要通过类名.对象进行赋值操作才可以生效,而通过self.对象赋值,只能在当前模块生效
'''

# 导入unittest框架
import unittest
from class07.key_word_web.keyword_web import WebKeys
from selenium import webdriver
from time import sleep


# 如何真正意义上的应用unittest框架:必须在类名继承unittest.TestCase
class UnitDemo(unittest.TestCase):
    # 前置条件
    # 后置条件
    # 测试用例:所有的测试用例必须以函数的形式存在,函数名称必须以test开头


    # class级别前置与后置条件
    @classmethod
    def setUpClass(cls) -> None:
        print('class级别的前置条件')
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        cls.title = None

    @classmethod
    def tearDownClass(cls) -> None:
        print('class级别的后置条件')
        print(cls.title)
        cls.driver.quit()

    # method级别
    def setUp(self) -> None:
        print('method前置条件')
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://www.baidu.com')
        pass

    def tearDown(self) -> None:
        print('method后置条件')
        # self.driver.quit()
        # 临时对None赋值
        print(self.title)
        #修改cls.title的值,在全局生效
        UnitDemo.title = self.driver.title




    def test_01(self):
        print('用例')

    def test_02(self):
        print('用例')
        self.assertGreaterEqual('123' ,'123' ,msg='断言失败') #两者对比断言
        self.assertIn('1','12',msg='断言失败') # 包含
        self.assertNotAlmostEqual(3.1111111,3.11111112,msg='断言失败')# 差距较小时成功
        a = '123'
        #当一个变量为空或者NOne或者false的时候,从布尔值考虑都属于false
        self.assertTrue(a,msg='失败') #判断是否存在



    #普通函数 :封装逻辑代码,以便于在测试用例中调用
    def login(self):
        print('普通函数')

# 要运行测试用例

if __name__ == '__main__':
    # unittest执行测试用例的行为
    unittest.main()




'''

    Skip装饰器:通过@unittest.skip进行调用
    总计有四种不同的skip装饰器
        1.@unittest.skip 无条件跳过该用例
        2.@unittest.skipuf :当if为真时  跳过
        3.@unittest.skipUnLess :当条件为假时  跳过
        4.@unittest.expectedFailure  :当测试用例执行失败时


'''
# import unittest
#
#
# class demo:
#     @unittest.expectedFailure
#     def test(self):
#         pass



















