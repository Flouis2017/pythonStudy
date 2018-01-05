# __author : "Flouis"
# date : 2018/1/5
import os
import shutil

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
# file_path = 'C:/Users/Administrator/Desktop/Pactera/test.docx'
file_path = 'C:/Users/Administrator/Desktop/Pactera/test2.txt'

# 向文件追加数据，如果该文件不存在则进行创建：
#file = open(file_path,'a+')
#stringList = ['\n这一路上走走停停 顺着少年漂流的痕迹\n',
#              '迈出车站的前一刻 竟有些犹豫\n',
#              '不禁笑这近乡情怯 仍无可避免\n',
#              '而长野的天 依旧这么暖 风吹起了从前\n',
#              '从前初识这世间 万般流连 看着天边似在眼前\n',
#              '也甘愿赴汤蹈火去走它一遍\n',
#              '如今走过这世间 万般流连 翻过岁月不同侧脸\n',
#              '措不及防闯入你的笑颜\n']
#stringData = '\n'.join(stringList)
#file.write(stringData)
#file.close()

# 读取文件中的数据，使用r+模式:
file = None
#try:
#    file = open(file_path,'r+')
#    readResult = file.read()
#    print(readResult)
#except Exception as e:
#    print(e)
#finally:
#    if file != None:
#        file.close()
file_path = 'C:/Users/Administrator/Desktop/Pactera/mytest.txt'
#if os.path.exists(file_path):
#    file = open(file_path,'r+')
##    一次性读取全部数据：
#    readResult = file.read()
#    print(readResult)
#    dataList = readResult.split('\n')
#    print(len(dataList))
#else:
#    print('文件不存在！')
#if file != None:
#    file.close()

# 创建一个目录(文件夹)：
#file_path = 'C:/Users/Administrator/Desktop/Pactera/test'
#flag=False
#try:
#    os.makedirs(file_path)
#    flag=True
#except Exception as e:
#    print(e)
#if flag:
#    print('创建文件目录成功！')
#else:
#    print('创建文件目录失败！')

# 【面白いこと】：在Python中文件目录(文件夹)如果已经存在了，是不允许创建的，会异常报错，
# 但是文件却不会,顶多就是格式化掉重新创建，但不会出现异常报错。这点和Java正好相反！

# 将文件(夹)拷贝到指定目录下：
dir_path = 'C:/Users/Administrator/Desktop/Pactera/Flouis'

#copyfile(arg1,arg2)方法只能用于复制单个文件，
#前参数为原文件绝对路径，后参数为拷贝生成的文件的绝对路径，进行覆盖复制
#try:
#    shutil.copyfile(file_path,dir_path+'/test.txt')
#except Exception as e:
#    print(e)

#copydir(arg1,arg2)方法只能用于复制单个目录，arg2必须不存在，如果原先agr2路径已经有目录存在了，则会报错。
#previous_dir_path = 'C:/Users/Administrator/Desktop/Pactera/test'
#later_dir_path = 'C:/Users/Administrator/Desktop/Pactera/Flouis/test'
#try:
#    shutil.copytree(previous_dir_path,later_dir_path)
#except Exception as e:
#    print(e)

#copy(arg1,arg2)用的是最经常的文件(夹)复制操作：
#arg1是文件路径，arg2是目录路径，表示将某个文件复制到某个目录下：
#try:
#    shutil.copy(file_path,dir_path)
#except Exception as e:
#    print(e)

#move(arg1,arg2)剪切操作：
#arg1是文件(目录)路径，arg2是文件目录路径，文件目录下不能有重复名字的文件(目录)，否则无法进行该操作：
try:
    shutil.move(file_path,dir_path)
    shutil.move('C:/Users/Administrator/Desktop/Pactera/test',dir_path)
except Exception as e:
    print(e)




    
    





