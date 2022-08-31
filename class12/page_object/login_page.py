'''
    LoginPage:实现登录页面的对象的封装,以便于流程需要时进行调用


'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from class12.base.base_page import BasePage

# 封装登录页面
class LoginPage(BasePage): # 继承BasePage页面
    # 页面url:每一个不同的页面对象,对应的都是不同的页面,就会有不同的url
    url = BasePage.url + '?s=/index/user/logininfo.html'

    # 页面关联元素
    user1 = (By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/a[1]')
    user = (By.NAME, 'accounts') # 将元素变成一个元组,传入到basepage
    pwd = (By.NAME, 'pwd')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 页面元素的操作行为

    def login(self, username, password):
        self.open()
        # self.click(self.user1)
        self.input_(self.user, username)
        self.input_(self.pwd, password)
        self.click(self.button)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    uesr = '1520147747'
    pwd = 'zpepc@001'
    lp.login(uesr, pwd)



