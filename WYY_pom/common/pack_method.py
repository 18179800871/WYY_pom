'''
    基类:提供给所有页面的基本调用工具类

'''
import time
from time import sleep
from selenium import webdriver

# 定义基类
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # driver = webdriver.Chrome()
    # 构造函数
    # url = '输如固定头的URl'
    url = 'https://music.163.com/'
    def __init__(self, driver):
        self.driver = driver
    '''
        在基类中定义的元素操作行为及driver操作行为
    '''
    # 访问uri
    def open(self):
        self.driver.get(self.url)

    # 元素 定位  以元组的形式来传递  加*是解析为元组
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()
    # 断言校验
    def assert_text(self, loc, expect):
        try:
            assert self.locator(loc).text == loc(expect)
            return True
        except:
            return False

        # 获取元素属性,进行断言
    # def assert_att(self, loc, txt, expect):
    #     att = self.locator(loc).get_attribute(loc(txt))
    #     try:
    #         assert att == loc(expect)
    #         return True
    #     except:
    #         return False
        # 显示等待 ,等待失败就会返回一个超市异常
    def assert_wait(self, loc, txt):
        try:
            return WebDriverWait(self.driver, loc(txt), 0.5).until(
                lambda le: self.locator(loc), message='查找元素失败'
            )
        except:
            return False

    def wait(self,loc, txt):
        sleep(loc(txt))
# 切换句柄
    # 不关闭标签页直接切换
    def switch_no_close(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
# 关闭当前标签页页面 在切换
    def switch_with_close(self, loc):
        handles = self.driver.close()
        self.driver.switch_to.window(handles[1])
 # 切换旧窗体
    def switch_to_old(self, loc):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])


    # 切入框架
    def ad_ifarme(self, loc):
        ifarme = self.locator(loc)
        self.driver.switch_to.frame(ifarme)
    # 切出框架
    def out_ifarme(self,loc):
        ifarme = self.locator(loc)
        self.driver.switch_to.default_content(ifarme)
    # 返回上层框架
    def an_ifarme(self,loc):
        ifarme = self.locator(loc)
        self.driver.switch_to.parent_frame(ifarme)
    # 隐式等待等待
    def wait_(self,txt):
        self.driver.implicitly_wait(txt)



