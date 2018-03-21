# __author : "Flouis"
# date : 2018/03/15

import os
import time

# 返回当前工作目录（路径）
# print(os.getcwd())

# C:\Users\Administrator\Desktop\temporary\Flouis

# 改变当前工作目录，加上r——让转义符失效
# 如果跳转的目录（路径）不存在，则会异常报错
os.chdir(r'C:\Users\Administrator\Desktop\temporary\Flouis')
# print(os.getcwd())

# 递归生成文件夹（目录）
# os.makedirs(r'test\abc')

# 递归删除空目录————只能移除空目录，一个目录里面如果有内容就无法删除了
# os.removedirs(r'test') # 如果是这么删除的话是会报错的，因为当前路径下的test目录下还有一个abc目录，test目录不为空，无法删除。
# os.removedirs(r'test\abc')

# 生成单级目录
# os.mkdir('test')

# 删除单级空目录
# os.rmdir('test')

# 列出指定目录下的所有文件和子目录，包括隐藏文件，返回一个列表对象
# print( os.listdir(r'C:\Users\Administrator\Desktop\temporary') )

# 删除一个文件————注意不是文件夹（目录）
# os.remove(r'C:\Users\Administrator\Desktop\temporary\Flouis\test.txt')

# 创建一个文件————注意不是文件夹（目录）
# f = open('test.txt','a') # 使用'w'的模式创建，如果名字一样，会清空之前文件中的内容。

# 重命名文件名
# os.rename('test2.txt','test3.txt')

# 获取文件/目录信息————返回一个元组对象
'''tmp_txt_file = os.stat(r'D:\JavaScript\jquery-3.0.0\www.jq22.com.txt')
print(tmp_txt_file)
print('该TXT文件大小为：',tmp_txt_file.st_size,'byte')
st = time.localtime(tmp_txt_file.st_mtime)
last_modified_time = time.strftime('%Y/%m/%d %H:%M:%S',st)
tmp_list = ['一','二','三','四','五','六','日']
last_modified_time = last_modified_time.replace(' ',' 星期'+tmp_list[st.tm_wday]+' ')
print('该TXT文件的修改时间为：',last_modified_time)'''

# 输出操作系统特定的路径分隔符：
# print(os.sep) # \

# 输出用于分割文件路径的字符串：
# print(os.pathsep) # ;

# 输出字符串指示当前操作系统：
# print(os.name) # win是用nt来代表，Linux是用posix来代表

# 获取系统的环境变量，返回一个字典对象：
# print(os.environ)

# 返回绝对路径
# print(os.path.abspath('test.txt')) # C:\Users\Administrator\Desktop\temporary\Flouis\test.txt

# 将指定路径分割成目录名(文件夹)和文件名二元组进行返回
# print(os.path.split(r'Flouis\test.txt')) # ('Flouis', 'test.txt')

# 返回os.path.split(path)二元组中的第一个元素
# print(os.path.dirname(r'Flouis\test.txt'))

# 返回os.path.split(path)二元组中的第二个元素
# print(os.path.basename(r'Flouis\test.txt'))

# 如果指定路径存在返回True，否则返回False
# 注意指定路径必须是一个绝对路径
# print(os.path.exists(r'C:\Users\Administrator\Desktop\temporary\Flouis\test2.txt'))

# 判断指定路径指向的是否是一个存在的文件，是：True，否：False
# print(os.path.isfile(r'C:\Users\Administrator\Desktop\temporary\Flouis\test.txt'))

# 判断指定路径指向的是否是一个存在的目录，是：True，否：False
# print(os.path.isdir(r'C:\Users\Administrator\Desktop\temporary\Flouis\test.txt'))

# 返回路径所指向的文件或目录的最后存取时间——时间戳：
print(os.path.getatime(r'C:\Users\Administrator\Desktop\temporary\Flouis'))

# 返回路径所指向的文件或目录的最后修改时间——时间戳：
print(os.path.getmtime(r'C:\Users\Administrator\Desktop\temporary\Flouis'))
