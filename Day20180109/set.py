# __author : "Flouis"
# date : 2018/1/9

# Python中只能用关键字set进行集合的声明定义：
s = set('Hello,world.')
print(s) # {'H', ',', 'l', '.', 'r', 'd', 'w', 'e', 'o'}

#s = set(['abc','asdf','abc'])
#print(type(s))
#mylist = list(s)
#print(mylist)

# 可哈希——就是不可变且能被唯一标识的意思。
# set和list可以看成是两个极端——set:无序不可重复，list:有序可重复
# 因为无序所以set就不能像list那样进行切片操作，也不能进行索引相关操作
# 但set可以使用for或迭代器进行遍历操作，也有判断是否某一元素在set中的in操作，当然这些对list都是有的。

print(',' in s)

iterator = iter(s)
#for i in iterator:
#    print(i,end=' ')

while True:
    try:
        print(next(iterator),end=' ')
    except StopIteration:
        break

print()
s.add('yum')
print(s)

s.clear()
print(s)

