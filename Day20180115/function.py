# __author : "Flouis"
# date : 2018/1/15
import time


def action(n):
    resStr = ''.join(['action ',str(n)])
    print(resStr)

    # filePath = 'C:/Users/Administrator/Desktop/temp/record.log'

    # 做日志记录：
    time_format = '%Y-%m-%d %X' # log_time with date 
    with open('record.log','a+') as file:
        current_time = time.strftime( time_format )
        resStr = ''.join([current_time,'  ','end action ',str(n),'\n'])
        file.write(resStr)

action(1)
action(2)
action(3)
