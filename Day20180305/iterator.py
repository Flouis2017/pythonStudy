# __author : "Flouis"
# date : 2018/3/5
from collections import Iterator,Iterable

# 生成器都是迭代器，但迭代器不一定是生成器
# iter()可以将可迭代对象强转成迭代器进行返回
# list,tuple,dict,string都是可迭代对象（iterable）
l = [1,2,2,4,5]
t = iter(l)
print(isinstance(l,list))
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))

print(isinstance(t,list))
print(isinstance(t,Iterable))
print(isinstance(t,Iterator))
# print(t)            # <list_iterator object at 0x000001DFF944D048>
# print(next(t))      # 1
# print(next(t))      # 2
# print(next(t))      # 2
# print(next(t))      # 4

# 什么是迭代器？
# 迭代器必要条件：1.有iter方法；2.有next方法

for x in t:
    print(x)

d = {'name':'Flouis','age':24}
for x in d:
    print(x)

