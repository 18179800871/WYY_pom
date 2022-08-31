# 引入logging模块
import logging

class DemoLog:
    def txt_log(self):
        # 创建日志器
        logging.basicConfig()
        logger=logging.getLogger('logger')
        # 设置日志级别
        logger.setLevel(logging.DEBUG)
        # 创建一个格式器
        formator=logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')
        # 创建一个处理器  输出文件中
        fh=logging.FileHandler('Log/log2.log',encoding='utf-8')
        # 创建一个处理器 输出到控制台
        sh=logging.StreamHandler()
        # 把文本处理器加载到日志器中
        logger.addHandler(fh)
        # 把控制台加载到日志器
        logger.addHandler(sh)
        # 把格式器放入控制台
        sh.setFormatter(formator)
        # 把格式器放入到文本控制器
        fh.setFormatter(formator)
        return logger

# logger.debug('debug模式')
# logger.info('info模式')
# logger.warning('waning模式')
# logger.error('error模式')
# logger.critical('critical模式')

    def test(self,a,b):
        try:
            sum=a+b
            self.txt_log().info('正确计算{}+{}'.format(a,b))
            return sum
        except Exception:
           self.txt_log().error('错误计算{}+{}'.format(a,b))
a=DemoLog().test(1,2)
# print(a)





# 1.函数的方法  要不把日志信息生成在控制台要么就是生成在文本里面。还需要改底层代码 加utf-8
# 2.四大组件的方法 日志信息同时生成在控制台 也能生成在文本里面

# 需要1个日志器：入口  日志信息输出到控制台  创建一个控制台处理器  控制台加载到日志器
# 格式丑  需要创建一个格式器  把格式器给控制台
# 创建一个文本处理器    文本处理器加载到日志器  文本格式丑  引用格式器  引用来的格式器给文本器

# 关系：一个日志器 对应多个处理器（输出到控制台，输出到文本） 一个处理器对应格式器