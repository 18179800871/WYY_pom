import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Logger:
    def get_logger(self):
        # 创建日志对象
        logger = logging.getLogger('logger')
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 创建一个处理器 输出到控制台

            # 创建日志级别
            logger.setLevel(logging.DEBUG)

            # 创建一个处理器 输出到控制台
            sh = logging.StreamHandler()

            # 创建一个格式器
            fmt = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')

            # 创建一个处理器 输出到文本中
            fh = logging.FileHandler(os.path.join(BASE_DIR, 'log.log'))

            # 把文本处理器加载到日志中
            logger.addHandler(fh)

            # 把格式器放到控制台
            sh.setFormatter(fmt)

            # 把控制台加载到日志器
            logger.addHandler(sh)

            # 把格式器放入到文本控制器中
            fh.setFormatter(fmt)


        return logger


        # logger.info('this is info')
        # logger.warning('this is warning')
        # logger.debug('this is debug')
