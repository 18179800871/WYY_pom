import  unittest

from ddt import ddt,data,file_data
from selenium import webdriver

from class06.chrome_options import Options
from  class12.page_object.login_page import LoginPage
from class12.page_object.product_page import ProductPage

'''
    如果不希望用例产生关联,那就不同的流程,用不同的测试用例,将需要的页面对象实例化
    如果想要快速实现整个流程的覆盖测试,则通过一套driver实现

'''

@ddt
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().options_conf())
        cls.lp = LoginPage(cls.driver)
        cls.pg = ProductPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_01_login(self,**kwargs):
        self.lp.login(kwargs['user'], kwargs['pwd'])

    def test_02_addcart(self):
        self.pg.addcart()



if __name__ == '__main__':
    unittest.main()
