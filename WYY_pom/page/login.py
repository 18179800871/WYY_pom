from selenium import webdriver
from selenium.webdriver.common.by import By
from common.pack_method import BasePage
from common.log import Logger
from common.chrome_options import Options
# 封装的网易云登录界面
class LoginPage(BasePage):
    # 页面关联元素
    logbut = (By.LINK_TEXT, '登录')
    qtbut = (By.XPATH, '//*[@id="otherbtn"]/a')
    agrbut = (By.ID, 'j-official-terms')
    qqbut = (By.LINK_TEXT, 'QQ登录')
    qq = (By.ID, 'img_out_1520147747')
    kj1 = (By.ID, 'ptlogin_iframe')
    def login(self):
        self.wait_(10)
        self.open()
        # 点击登录
        self.click(self.logbut)
        # 点击其他模式登录
        self.click(self.qtbut)
        # 点击同意服务
        self.click(self.agrbut)
        # 点击qq登录
        self.click(self.qqbut)
        # 切换句柄
        self.switch_no_close()
        self.ad_ifarme(self.kj1)
        # 点击齐全头像登录
        self.click(self.qq)

# if __name__ == '__main__':
#     driver = webdriver.Chrome(options=Options().options_conf())
#     lp = LoginPage(driver)
#     lp.login()

























