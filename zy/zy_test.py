from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://39.98.138.157/shopxo/index.php')
sleep(3)
'''注册'''
# driver.find_element(by='link_text' , value= '注册').click() #找不到元素
# driver.find_element_by_link_text('注册').click()
# #输入账号密码
# driver.find_element(by='xpath' , value='/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[1]/input').send_keys('1520147747')
# sleep(1)
# driver.find_element(by='xpath' , value='/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys('zpepc@001')
# #点击注册
# driver.find_element(by='xpath' , value='/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label/span/i[2]').click()
# driver.find_element(by='xpath' , value='/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
# driver.quit()


'''登录'''
driver.find_element_by_link_text('登录').click()
# #输入账号密码
driver.find_element(by='xpath' , value='/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input').send_keys('1520147747')
sleep(1)
driver.find_element(by='xpath' , value='/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('zpepc@001')
driver.find_element(by='xpath' , value='/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
driver.quit()
driver.f