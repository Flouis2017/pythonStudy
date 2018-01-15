# __author : "Flouis"
# date : 2018/1/15


def action(n):
    resStr = ''.join(['action ',str(n)])
    print(resStr)

    # filePath = 'C:/Users/Administrator/Desktop/temp/record.log'

# 做日志记录：
    with open('record.log','a+') as file:
        resStr = ''.join(['end action ',str(n),'\n'])
        file.write(resStr)

action(1)
action(2)
action(3)
