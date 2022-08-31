'''
    1.从注册到用户信息修改
    2.从登录到山沟添加购物车
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from class06.chrome_options import Options
driver = webdriver.Chrome(options=Options().options_conf())
driver.implicitly_wait(10)
#实现注册操作
driver.get('http://39.98.138.157/shopxo/index.php')
''' 注册步骤步骤'''
#断言
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'))

#登录
'''登录步骤'''
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'))


'''元素悬停'''

from selenium.webdriver import ActionChains
driver.get('http://www.baidu.com')
#悬停操作 在执行过程中鼠标不能动
el = driver.find_element_by_xpath('')
action = ActionChains(driver)
action.move_to_element(el).perform()





































































