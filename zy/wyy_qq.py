from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://music.163.com/')
driver.find_element_by_xpath('//a[@data-action="login"]').click()
sleep(1)
driver.find_element_by_link_text('选择其他登录模式').click()
driver.find_element_by_id('j-official-terms').click()
driver.find_element_by_link_text('QQ登录').click()
#当打开新的页面时,webdriver还是停留在第一个界面,
#每个标签页都有一个句柄->默认停留在最开始的句柄上
# 获取浏览器句柄
handles = driver.window_handles
#切换到第二个句柄
driver.switch_to.window(handles[1])
#点击齐全登录
# iframe窗体,是一个独立的窗体,
