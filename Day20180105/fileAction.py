# __author : "Flouis"
# date : 2018/1/5
import os
import traceback

# 使用os.startfile()函数/方法运行其他程序：
# os.startfile('C:\\Users\\Administrator\\Desktop\\temp\\Flouis\\wtf.txt')
# os.startfile('C:\\Users\\Administrator\\Desktop\\temp\\i.docx')

# 创建一个文件：
# 使用open方法，模式采用w/w+/a/a+，不能用r/r+。
# 这里稍微做下r/r+/w/w+/a/a+的区分：
# 1.r:只读操作，但首先文件必须存在，无法用于创建文件。
# 2.r+:读写操作，但首先文件必须存在，无法用于创建文件。
# 3.w:只写操作，若文件不存在则创建。
# 4.w+:读写操作，若文件不存在则创建。
# 5.a:增写操作，若文件不存在则创建。
# 6.a+:比上面多一个读操作，若文件不存在则创建。
# 使用w/w+和a/a+创建文件的区别：w/w+是格式化创建，而a/a+不是。
file_path = 'C:/Users/Administrator/Desktop/temp/test.docx'
file = open(file_path,'a+')
file.close()

# 创建一个目录(文件夹)：
file_path = 'C:/Users/Administrator/Desktop/temp/test'
flag=False
try:
    os.makedirs(file_path)
    flag=True
except Exception as e:
    print(e)
if flag:
    print('创建文件目录成功！')
else:
    print('创建文件目录失败！')

# 【面白いこと】：在Python中文件目录(文件夹)如果已经存在了，是不允许创建的，会异常报错，
# 但是文件却不会,顶多就是格式化掉重新创建，但不会出现异常报错。这点和Java正好相反！
