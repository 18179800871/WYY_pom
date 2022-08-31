#导入selenium包
from selenium import webdriver
#创建webdriver ,生成一个浏览器对象
driver = webdriver.Chrome()
driver.get('http://www.baidu.com') #必须加 http://
# 输入内容
driver.find_element_by_id('kw').send_keys('百度')
driver.find_element_by_id('su').click()
