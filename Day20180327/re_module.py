# __author : "Flouis"
# date : 2018/03/27

import re

# 在学习Python正则表达式之前，可以回顾下Python有关匹配搜索的内置函数：
tmp_str = 'hello world'
print( tmp_str.find('lo') )
print( tmp_str.replace(' ',',') )
print( tmp_str.split(' ') )

# find/replace/split都是跟匹配有关的内置函数，但是这种匹配是(完)全匹配，
# 也就是说匹配的内容是定死的。而正则表达式则可以进行全匹配或模糊匹配。

tmp_str = 'book,blank,break,black,blink'
reg = 'b.*k'
print(re.findall(reg,tmp_str))
reg = 'b.{2}k'
print(re.findall(reg,tmp_str))


from my_module import my_lib
my_lib.print_multiplication_table()

