# __author : "Flouis"
# date : 2018/3/13

import time
import datetime

utc_datetime = '2018-12-31T22:53:52.233Z'

UTC_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
LOCAL_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

utc_datetime = datetime.datetime.strptime(utc_datetime,UTC_FORMAT)
print('Global standard time :',utc_datetime)

def getOffset():
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    return offset
# UTC时间转为本地时间：
def utc_to_local(utc_datetime):
    local_time = utc_datetime + getOffset()
    return local_time

local_datetime = utc_to_local(utc_datetime)
local_datetime = str(local_datetime)
print('Local Time (Beijing Time) :',local_datetime)
print(local_datetime[0:local_datetime.index('.')])

print('========================================================================================')

local_datetime = '2018-01-01 03:23:56.233'
local_datetime = datetime.datetime.strptime(local_datetime,LOCAL_FORMAT)

print('Local Time (Beijing Time) :',local_datetime)

# 本地时间转为世界标准时间：
def local_to_utc(local_datetime):
    utc_datetime = local_datetime - getOffset()
    return utc_datetime

utc_datetime = local_to_utc(local_datetime)

print('Global standard time :',utc_datetime)

utc_datetime = str(utc_datetime)
print()
utcTime = utc_datetime[0:utc_datetime.index('.')]
print(utcTime)
struct_time = time.strptime(utcTime,'%Y-%m-%d %H:%M:%S')
print(struct_time)
print(time.mktime(struct_time)) # time.mktime(time_tuple)只能取整的时间戳，因为上面time.strptime()方法会把毫秒及以下的数据省略
