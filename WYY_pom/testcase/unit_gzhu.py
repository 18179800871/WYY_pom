from common.log import Logger
from common.creenshot import save_creenshot
from page.login import LoginPage
from page.View_attention import View_attention
import unittest
from selenium import webdriver
from common.chrome_options import Options


class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().options_conf())
        cls.lp = LoginPage(cls.driver)
        cls.pg = View_attention(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
       cls.driver.quit()

    def test_01(self):
        self.lp.login()

    def test_02(self):
        self.pg.View()


# if __name__ == '__main__':
#     unittest.main()










