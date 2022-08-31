import unittest
from class11.key_word.keyword_web import WebKeys
from ddt import ddt,file_data

@ddt
class Demo(unittest.TestCase):
    def setUp(self) -> None:
        self.wk = WebKeys('Chrome')
        self.wk.driver.maximize_window()
    def tearDown(self) -> None:
        pass

    # 实现电商登录
    @file_data('./data/login.yaml')
    def test_01(self,**kwargs):
        self.wk.open(kwargs['url'])
        self.wk.click(**kwargs['button1'])
        self.wk.input(**kwargs['username'])
        self.wk.input(**kwargs['password'])
        self.wk.click(**kwargs['button2'])
        self.wk.wait(kwargs['sleep'])
        el = self.wk.assert_wait(**kwargs['assert'])
        self.wk.quit()
        self.assertTrue(el)

if __name__ == '__main__':
    unittest.main()