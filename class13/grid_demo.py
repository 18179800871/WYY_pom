# 基于grid来实现driver的调用
import threading
from time import sleep

from selenium import webdriver
from selenium.webdriver import Remote

def visit(driver):
    driver.get('http://www.baidu.com')
    sleep(3)
    driver.quit()

#定义一个线程租
th = []
driver = webdriver.Chrome()
# 定义所有节点
hosts = {
    '子节点的设备地址1/wd/hub': 'Chrome',
    '子节点的设备地址2/wd/hub': 'Chrome'

}
# 读取所有节点,生成各个节点的webdriver对象,执行自动化
for host,browser in hosts.items():

    print(host + '============' + browser)
    driver = Remote(
        command_executor=host,
        desired_capabilities={
            'platform':'Windows',
            'browserName':browser
        }
    )

    # 添加线程
    th.append(threading.Thread(target=visit, args=[driver]))

for t in th:
    t.start()






