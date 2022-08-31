# 日志：log  他是一种可以追踪程序运行所发生事件的一种发发  通过调用日志可以记录程序发生了什么
# 作用：了解程序运行情况 判断程序是否则正常；分析和定位程序错误问题
# 日志等级： 反映问题的错误严重程度
'''
debug：调试  开发用于调试代码 1级别
info:表示程序正常运行  2级别
warning:警告  程序有问题，但是不影响程序正常运行  不要提bug  3级别
error: 错误 代表程序有问题   要提bug 4级别
critical:严重的 临街的 程序出现了严重问题 程序将要崩溃  5级别
'''

# python中日志怎么用

# 引入logging   logging模块的作用：生成日志，设置日志路径，日志等级，日志回滚等等
import logging
# 日志格式：2020-10-30 16:24:59,090 excel_excutor.py INFO  excute_web  内容
fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
# 设置日志级别
logging.basicConfig(level=logging.INFO,format=fmt,filename='Log/log1.log')

logging.debug('debug模式')
logging.info('info模式')
logging.warning('warning模式')
logging.error('error模式')
logging.critical('critical模式')
