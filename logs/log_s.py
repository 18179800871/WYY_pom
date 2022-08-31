import logging

# 基础版本
    # fmt = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
# logging.basicConfig(level=logging.INFO,format=fmt,filename='../Log/log1.log')
# logging.debug('debug')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')
#
# 进阶版本
# logger 日志器
# handlers 处理器
# formatters 格式器
#
'''
    函数的方法   要不把日志输出在控制台,要么输出在文件中,还需要改底层代码utf-8
    四大组件的方法 日志同时生成在控制台,也能生成在文本里面
    

'''
# 需要一个日志器: 入口 把日志信息输出到控制台, 创建一个控制台的处理器 控制台加载到处理器
# 创建一个格式器, 把格式器给控制台
# 创建一个文本处理器,文本处理器加载到日志器, 引用格式器, 引用来的格式器给文本器

# 创建日志器
logger = logging.getLogger('logger')

# 创建日志级别
logger.setLevel(logging.DEBUG)

# 创建一个处理器 输出到控制台
sh = logging.StreamHandler()

# 创建一个格式器
fmt = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')

# 创建一个处理器 输出到文本中
fh = logging.FileHandler('../logs/log2.log')

# 把文本处理器加载到日志中
logger.addHandler(fh)

# 把格式器放到控制台
sh.setFormatter(fmt)

# 把控制台加载到日志器
logger.addHandler(sh)

# 把格式器放入到文本控制器中
fh.setFormatter(fmt)

logger.debug('debug模式')
logger.info('info模式')
logger.warning('warning模式')
logger.error('waring模式')
logger.critical('critical模式')



















































