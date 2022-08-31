import time
def save_creenshot(driver):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前时间
    pic_path = "../creenshot/"+now+'_screen.png'                           # 保存截图到指定路径
    # print(pic_path)
    driver.save_screenshot(pic_path)                                       # 调用python自带的截图功能