'''
    基类:提供给所有页面的基本调用工具类

'''
from selenium import webdriver

# 定义基类
class BasePage:
    # driver = webdriver.Chrome()
    # 构造函数
    url = 'http://39.98.138.157/shopxo/index.php'
    def __init__(self, driver):
        self.driver = driver



    '''
        在基类中定义的元素操作行为及driver操作行为
    '''
    # 访问uri
    def open(self):
        self.driver.get(self.url)

    # # 退出
    # def quit(self):
    #     self.driver.quit()

    # 元素 定位  以元组的形式来传递  加*是解析为元组
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

















