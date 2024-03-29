from selenium import webdriver

'''
#配置ChromeOPtions:一般作为一个专门的配置类进行存放
#特殊场景下的浏览器配置是需要自行查找资料,但是查找的时候要记得查看代码:
    新版本: driver = webdriver.Chrome(options = options)
    老版本: driver = webdriver.Chrome(chrome_options = options)
    因为老版本的option是配置,配置参数是chrome_options,而新版本的参数是options


    常用的浏览器配置项
    1.去掉黄条警告
    2.窗体最大化
    3.无头模式
    4.读取本地缓存
    5.禁用密码管理窗体
'''
class Options:
    def options_conf(self):
        #创建options对象
        options = webdriver.ChromeOptions()
        #去掉默认的自动化提示:不去掉一般不会有任何影响,但是在特殊情况下,黄条可能会遮挡到页面的内容
        options.add_experimental_option('excludeSwitches' , ['enable-automation'])
        #窗体最大化
        options.add_argument('start-maximized')

        '''
        加载本地缓存,让利浏览器变成一个有缓存的模式
        1.通过指令查找Chrom浏览器的缓存地址 chrome://version
            个人资料路径
        2.通过传入本地缓存,用来实现缓存的获取, 参数 --user-data-dir=
        3.在调用本地缓存时,要先关闭所有正在应用的浏览器,
        4.因为需要加载本地缓存,所有在启动浏览器之后,运行脚本的第一条指令,速度会非常缓慢,
            如果要提速,就手动输入一个随便一个进行访问,就可以提速了
        5.不推荐使用,如果你非要绕过登录来实现后续行为,则添加
        6.最廉价的验证码机制出来手段,仅限登录部分
        '''
        options.add_argument(r'--user-data-dir=C:\Users\1520147747\AppData\Local\Google\Chrome\User')

        ##添加配置去掉密码管理弹窗
        prefs = {"":""}
        prefs["credentials_enable_service" ] = False
        prefs["profile.password_manager_enadled"] = False
        options.add_experimental_option("prefs" , prefs)

        #无头模式 :Headless模式,无界面运行,会尽可能的降低CPU的使用率,整体及其的资源使用率下降
        # options.add_argument('--headless')
        #隐身模式/无痕模式
        options.add_argument('incognito')
        #指定窗口大小
        options.add_argument('-windows-size=700,1080')

        return options
if __name__ == '__main__':
    #生成浏览器配置
    options = Options().options_conf()
    #配置webdriver
