# 实现多线程应用
import threading
from time import sleep

from selenium import webdriver
'''
    threading模块都是基于Thread的调用来产生线程,从而实现对线程的处理
    通过start()方法啦启动线程,可以通过循环的方式来多线程启动
    threading.Thread 创建一个线程
    多线程中各个线程的运行,是不会依照默认的等待的行为,等到第一条线程运行完在运行第二条线程的
    线程在运行的时候,会存在两种情况
        1.每一条线程操作不同的对象,彼此相互不干扰
        2.每一条线程都在操作同一个对象,彼此之间会产生干扰,为了避免干扰,我们需要对线程进行上锁
    多线程调用用例进行并行处理,其本质就是调用了线程函数Thread(),只是因为在测试领域内,基本不存在锁的场景,
        
'''

# class Demo:

    # def func_01(self):
    #     print('01')
    #     sleep(3)
    #     print('等待3秒')
    # def func_02(self, name, value):
    #     print('02')
    # def run(self):
th = []
    #     # 通过threading模块来调用指定函数
    #     # th.append(threading.Thread(target=self.func_01)).start()
    #     # th.append(threading.Thread(target=self.func_02, args=['name', 'value'])).start()
    #     for i in range(0, 1):
    #         threading.Thread(target=self.func_01).start()
    #     for i in range(0, 1):
    #         threading.Thread(target=self.func_02, args=['name', 'value']).start()
    #
    #     for i in range(0, 1):
    #         threading.Thread(target=self.func_01).start()
    #         threading.Thread(target=self.func_02, args=['name', 'value']).start()

def visit(self):
    self.driver.get('http://www.baidu.com')
driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()

th.append(threading.Thread(target=visit , args=[driver])  )
th.append(threading.Thread(target=visit , args=[driver1])  )
th.append(threading.Thread(target=visit , args=[driver2])  )
threading.Thread(target=visit, args=[driver])

for i in th:
    i.start()


# if __name__ == '__main__':
#     f = visit()
#     f.
















