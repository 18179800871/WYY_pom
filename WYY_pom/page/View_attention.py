from selenium import webdriver
from selenium.webdriver.common.by import By
from common.pack_method import BasePage
from common.log import Logger
from common.chrome_options import Options
from common.creenshot import save_creenshot
import unittest

class View_attention(BasePage,unittest.TestCase):
    url = BasePage.url + '/#/user/follows?id=261236200'
    kj1 = (By.XPATH, '//*[@id="g_iframe"]')
    # view = (By.ID, 'follow_count')
    pepo = (By.LINK_TEXT, '肥皂菌丨珉珉的猫咪丨')
    asss = (By.XPATH, '//*[@id="head-oper"]/a[4]')

    def View(self):
        self.wait_(10)
        self.open()
        self.ad_ifarme(self.kj1)

        # self.click(self.view)
        self.click(self.pepo)
        sh = self.assert_text(self.asss,'未关注')

        try:
            self.assertEqual(sh, 'True','断言成功')
            Logger().get_logger().info('进入关注页面成功')
        except Exception:
            Logger().get_logger().info('进入关注页面失败')
            save_creenshot(self.driver)






if __name__ == '__main__':
    driver = webdriver.Chrome(options=Options().options_conf())
    lp = View_attention(driver)
    lp.View()
