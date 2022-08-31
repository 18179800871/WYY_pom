from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php')
'''登录'''
driver.find_element_by_link_text('登录').click()
# #输入账号密码
driver.find_element(by='xpath' , value='//*[@name = "accounts"]').send_keys('1520147747')
driver.find_element(by='xpath' , value='/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('zpepc@001')
driver.find_element(by='xpath' , value='/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

#搜索iphone6
WebDriverWait(driver, 10, 0.5).until(lambda el:driver.find_element(by='id' , value='search-input') , message='未定位到元素')
driver.find_element(by='xpath' , value='//*[@id="search-input"]').send_keys('苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G')
driver.find_element(by='id' , value='ai-topsearch').click()


# #获取新的句柄
# sleep(2)
#点击选择手机
driver.find_element(by='xpath' , value='/html/body/div[4]/div/ul/li/div/a/img').click()
#点击物品加入到购物车
handles = driver.window_handles
#切换到新打开的句柄
driver.switch_to.window(handles[1])
# 将物品加入到购物车
driver.find_element(by='xpath' , value='/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]').click()
sleep(1)
driver.find_element(by='xpath' , value='/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[1]/img').click()
sleep(1)
driver.find_element(by='xpath' , value='/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[1]').click()

driver.find_element(by='xpath' , value='/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button').click()

WebDriverWait(driver , 10 , 0.5).until(lambda  el:driver.find_element(by='xpath' , value='//*[@id="common-prompt"]/p') , message='加入失败')
driver.quit()





