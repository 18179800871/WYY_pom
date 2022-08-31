import unittest

'''
    ddt的使用:
        1.在需要调用DDT模块的类名处,通过装饰器声明

'''
# 导入ddt的包
from ddt import ddt ,data,unpack,file_data

# ddt驱动文件内容,除去yaml之外,其他的文件都需要自行定义函数来驱动.
# 打开文件,获取内容
def readFile():
    list = []
    file = open('./data/demo.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        # print(line)
        list.append(line)
    return list
@ddt
class UintDdt(unittest.TestCase):

    # 测试用例:都是基于函数进行管理,就意味着,可以设置形参
    '''
        在ddt的数据驱动中如果data装饰器设置有多个值,name就会运行多个测试用例
        data装饰器解析机制,
            @data('数据1','数据2')
            基于 , 来解析数据,获得,数据1,数据2两个不同的字符串data会认为本次用例会执行两次
            一次传入数据1
            一次传入数据2
        例如登录:
            多组不同数据,执行同一个用例
        如果单次需要传入多个数据,就需要对数据内容进行打包 列表与元组 list  元组 字典数据不可
        ubpack与data的解析机制是一样的,都是依照同样的规则进行内容解析
        只是unpack解析的是data已经解析之后的数据内容
           data解析之后确定用例的执行次数
           uppack只是将本次执行的数据进行解析
        2.ddt驱动文件内容,除去yaml之外,其他的文件都需要自行定义函数来驱动
            读写文件内容进行数据驱动其本质还是驱动的数据
        3.yaml文件是唯一一种可以和ddt模块完美搭配的文件格式
            file_data专门解析yaml数据

    '''

    #
    # @data(['沈华明',18] ,['沈华明1',19]) # 数据传入
    # @unpack #数据分层
    # def test_01(self,name,age):
    #     print(name)
    #     print(age)
    # @data(*readFile())
    # def test_02(self, name):
    #     print(name)
    @data(['沈华明','18'],['虚竹','13']) # 第一次拆分
    @unpack # 第二次拆分,解析data解析后的数据
    def test_01(self,name,age):
        print(name,age)
        print(name,age)

    @data(*readFile()) # 读取文件 *解包操作,将一个列表中的数据拆分为多个
    def test_02(self,name):
        print(name)
    # 读取列表
    @file_data('./data/ddt_yaml.yaml')
    def test_03(self,name):
        print(name)

    @file_data('./data/ddt_yaml_dict.yaml')
    def test_03(self, **kwargs): # 读取字典
        print(kwargs)



if __name__ == '__main__':
    unittest.main()
    # print(readFile())








