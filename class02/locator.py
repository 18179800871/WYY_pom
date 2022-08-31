'''八大元素定位'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
1.id: 类似于身份证的身份证号码,但是为了避免重复,定位前校验一下
2.name: 类似于身份证的名字,容易出现重名的情况,定位前校验一下
3.link text: 一般用于定位a标签,超链接,通过text来进行定位
4.partial link text: 和link text一样的,但是模糊查询例如登录  搜索登(登)
5.classname: 通过class属性查找元素 ,只查找一个元素,当class有多个元素值,输入一个即可 除非无奈,不可使用
6.tagname:通过标签名进行元素查找,一般用于下拉列表框的值
    像后台系统新增后,下拉列表值变动了
7.cssselector: 基于class样式进行查找,有自己的固定表达式,类似于xpath,作为应用广度仅次于xpath的定位方式
    一般遇到伪元素 使用
8.xpath:定位界的万金油 唯一解决不了的是伪元素
    类似于文件系统,根据路径查找元素
    相对路径,绝对路径
    xpath 定位不推荐class属性进行定位
    xpath的函数:
    contains:通过模糊查找的元素的属性,继而查找到这个元素
    写法: //*[contains(@id,'search')] 
    //*[contains(@元素,'元素名称')] 
'''
driver = webdriver.Chrome()
driver.get('http://172.30.15.127/health/maintaincewarning')
driver.find_element_by_id('')
#tag_name定位写法
driver.find_elements_by_tag_name('') #elenents用于查找多个元素,结果会返回一个list集合
#复制selector
driver.find_element_by_css_selector('')
driver.implicitly_wait(10)
WebDriverWait.until()
WebDriverWait.until_not()