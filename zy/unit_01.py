import unittest
from selenium import webdriver
from class06.chrome_options import Options
# from class07.key_word_web import keyword_web
from selenium.webdriver.common.keys import Keys
class Unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://music.163.com/')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

        pass
    def setUp(self) -> None:
        self.driver.implicitly_wait(10)
        #登录
        iframe = self.driver.find_element(by='id' , value='g_iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(by='link text' , value='用户登录').click()

        iframe1 = self.driver.find_element(by='xpath' , value='//*[@id="g_iframe"]')
        self.driver.switch_to.frame(iframe1)
        self.driver.find_element(by='link text', value='选择其他登录模式').click()
        self.driver.switch_to.default_content()
        self.driver.find_element(by='id', value='j-official-terms').click()
        self.driver.find_element(by='link text', value='QQ登录')
        handles =self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.find_element(by='id' , value='nick_1520147747').click()

    def tearDown(self) -> None:

        print('用例结束')

    def test_01(self):
        self.driver.find_element(by='link_text' , value='我的音乐').click()

    def test_02(self):
        self.driver.find_element(by='name' , value='srch').send_keys('我的梦')
        self.driver.find_element(by='name' , value='srch').send_keys(Keys.ENTER)
        ar = self.driver.find_element(by='link_text' , value='我的梦 (Live)')
        assert ar == '我的梦 (Live)', '断言失败'





if __name__ == '__main__':
    unittest.main()