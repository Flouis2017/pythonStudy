# __author : "Flouis"
# date : 2018/03/22
import datetime
import logging

today = datetime.datetime.now().strftime('%Y_%m_%d')
# print(type(today))

# logging basicConfig
'''logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a %Y/%m/%d %H:%M:%S',
                    filename='C:\\Users\\Administrator\\Desktop\\temporary\\Flouis\\'+today+'.log',
                    filemode='a+')'''



# priority:critical error warning info debug
# logging.debug('\t\t:debug message')
# logging.info('\t\t:info message')
# logging.warning('\t:warning message')
# logging.error('\t\t:error message')
# logging.critical('\t:critical message')

# 使用logger：既能将日志信息输出到文件中，又能输出到控制台
logger = logging.getLogger()

# 创建一个文件处理对象，用于将日志信息写入文件中：
fh = logging.FileHandler('C:\\Users\\Administrator\\Desktop\\temporary\\Flouis\\'+today+'.log')

# 再创建一个流处理对象，用于将日志信息输出到控制台：
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
# 设置日志级别：
logger.setLevel(logging.DEBUG)
logger.debug(': logger debug message')
logger.info(': logger info message')
logger.warning(': logger warning message')
logger.error(': logger error message')
logger.critical(': logger critical message')
