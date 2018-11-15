# __author : "Flouis"
# date : 2018/03/27

import re

# 在学习Python正则表达式之前，可以回顾下Python有关匹配搜索的内置函数：
# tmp_str = 'hello world'
# print( tmp_str.find('lo') )
# print( tmp_str.replace(' ',',') )
# print( tmp_str.split(' ') )

# find/replace/split都是跟匹配有关的内置函数，但是这种匹配是(完)全匹配，
# 也就是说匹配的内容是定死的。而正则表达式则可以进行全匹配或模糊匹配。

# tmp_str = 'book,blank,break,black,blink'
# reg = 'b.*k'
# print(re.findall(reg,tmp_str))
# reg = 'b.{2}k'
# print(re.findall(reg,tmp_str))

# from my_module import my_lib
# my_lib.print_multiplication_table()

# 元字符：

# .（通配符，默认情况下Python中“.”可以匹配除换行符以外的任意一个字符）
# pat = 'lo.w'
# test_str = '''hello
# world'''
# print( re.findall(pat, test_str) )
# test_str = 'hello\nworld'
# print( re.findall(pat, test_str) )
# test_str = 'hello world'
# print( re.findall(pat, test_str) )

# ^（首字符匹配）
# pat = '^w...d'
# test_str = 'hello world'
# print(re.findall(pat, test_str))
# test_str = 'world hello'
# print(re.findall(pat, test_str))

# $（尾字符匹配）
# pat = 'h...o$'
# test_str = 'hello world'
# print(re.findall(pat, test_str))
# test_str = 'world hello'
# print(re.findall(pat, test_str))

# 单限定符 []
pat = 'l[od]'
test_str = 'hello world'
print(re.findall(pat, test_str))

# 重复限定符 {}、*、?、+
# 如：'a{n}' 表示匹配a出现n次，'a{n,m}' 表示匹配a出现n次到m次
# {}本身是一个贪婪匹配，所以如果限定了匹配范围{n,m}，如果出现次数超过m次，匹配结果就是m次
pat = 'a{1,3}b'
test_str = 'aaaaab'
print(re.findall(pat, test_str)) # ['aaab']
# *可以改写为{0,} ?可以改写为{0,1} +可以改写为{1,}


