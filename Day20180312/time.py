# __author : "Flouis"
# date : 2018/3/12

import time

# print(help(time))

# print timestamp:
# print('timestamp:',time.time())                                  *****

# time.sleep(3)             # 延迟：让CPU停止当前程序                 *****
# print(time.clock())       # 计算CPU执行的时间

# print(time.gmtime())      # 世界标准时间————结构化时间              ***

# print(time.localtime())   # 本地时间                              *****

# print(help(time.strftime))  # strftime(format[, tuple]) -> string
# 格式化时间：2018-03-12 22:53:52
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))       ******

# 跟strftime(format,tuple)的作用刚好相反的方法：strptime(string,format)
# print(help(time.strptime))  # strptime(string, format) -> struct_time
# st = time.strptime('22:59:47 2018/03/12','%H:%M:%S %Y/%m/%d')
# print(st)
# print(st.tm_year)
# wday = st.tm_wday + 1
# print('今天是这周的第',wday,'天')
# yday = st.tm_yday + 1
# print('今天是今年的第',yday,'天')

# time.ctime(时间戳)，没有时间戳的话默认就是当前时间戳
# print(time.ctime(3600))     # Thu Jan  1 09:00:00 1970
# print(time.ctime())         # Mon Mar 12 23:22:44 2018

# 将格式化时间转化为时间戳：
# print(help(time.mktime))        # mktime(tuple) -> floating point number
print(time.mktime(time.localtime()))

import datetime

print(datetime.datetime.now())