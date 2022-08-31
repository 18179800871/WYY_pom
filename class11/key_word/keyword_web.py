'''

web端关键字驱动
    结构中属于逻辑代码层,主要目的是作为一个工具类的角色.
    在需要用到这些工具时,通过这个类实现
    原理
    大型超市-自家工具箱-动用工具
    selenium-关键字-web自动化
    工具箱中一般包含需要的常规操作行为
        输入.点击.启动等
    单独的工具类的存在是没有意义的,一定需要关联到实际应用,才能产生价值
'''
from time import sleep

from selenium import webdriver

# 生产一个浏览器(webdriver对象)
from selenium.webdriver.support.wait import WebDriverWait

'''
    getattr(class_name,function_name)函数 ,获取属性或者函数的方法
    从class_name对象获取名称为function_name的成员属性
    如果要获取class_name对象的函数,则需要在末尾添加一个()
    getattr(webdriver,'Chrome') = webdriver.Chrome
    getattr(webdriver,'Chrome')() = webdriver.Chrome()


'''

# 生成一个浏览器(webdriver对象):发反射机制

def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


# 定义工具类
class WebKeys:
    # # 定义driver
    # driver = webdriver.Chrome()
    #构造函数
    def __init__(self,type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    #访问URL
    def open(self,url):
        self.driver.get(url)

    # 退出
    def quit(self):
        self.driver.quit()
    # 单个元素定位
    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])
        #driver中定位元素有八种方法,

    # 多个元素定位
    def locators(self,**kwargs):
        return self.driver.find_elements(kwargs['name'],kwargs['value'])

    # 输入
    def input(self,**kwargs):
        el = self.locator(**kwargs)
        el.clear()
        el.send_keys(kwargs['txt'])
    #点击
    def click(self,**kwargs):
        self.locator(**kwargs).click()

    #断言校验
    def assert_text(self,**kwargs):

        try:
            assert self.locator(**kwargs).text == kwargs['expect']
            return True
        except:
            return False


    # 显示等待 ,等待失败就会返回一个超市异常
    def assert_wait(self,**kwargs):
        try:
            return WebDriverWait(self.driver ,kwargs['txt'],0.5).until(
                lambda le: self.locator(**kwargs), message= '查找元素失败'
            )
        except:
            return False
    # 强制等待
    def wait(self,time_):
        sleep(time_)

    # 切换句柄
    # 不关闭标签页直接切换
    def switch_no_close(self,**kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 关闭当前标签页页面 在切换
    def switch_with_close(self,**kwargs):
        handles = self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 切换旧窗体
    def switch_to_old(self,**kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 获取元素属性,进行断言
    def assert_att(self,**kwargs):
        att = self.locator(**kwargs).get_attribute(kwargs['txt'])
        try:
            assert att == str(kwargs['expect']) #将excel获取到的数据 转换为str类型
            return True
        except:
            return False





















