from selenium import webdriver
class Options:
    def options_conf(self):
        #创建options对象
        options = webdriver.ChromeOptions()
        #去掉默认的自动化提示:不去掉一般不会有任何影响,但是在特殊情况下,黄条可能会遮挡到页面的内容
        options.add_experimental_option('excludeSwitches' , ['enable-automation'])
        #窗体最大化
        options.add_argument('start-maximized')
        options.add_argument(r'--user-data-dir=C:\Users\1520147747\AppData\Local\Google\Chrome\User')

        ##添加配置去掉密码管理弹窗
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enadled"] = False
        options.add_experimental_option("prefs", prefs)

        # 无头模式 :Headless模式,无界面运行,会尽可能的降低CPU的使用率,整体及其的资源使用率下降
        options.add_argument('--headless')
        # 隐身模式/无痕模式
        options.add_argument('incognito')
        # 指定窗口大小
        options.add_argument('-windows-size=700,1080')

        # q去掉日志信息day
        options.add_argument('log-level=3')

        return options
if __name__ == '__main__':
    #生成浏览器配置
    options = Options().options_conf()
    #配置webdriver
    driver = webdriver.Chrome(options = options)









