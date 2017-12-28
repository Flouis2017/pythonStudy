# __author : "Flouis"
# date : 2017/12/28

# Python中字典(dict)的概念就等同于Java中Map——键值对
# 字典的键必须是不可变类型
# Python中字符串、整型和元组是不可变类型，列表和字典是可变类型


dictionary={'name':'Flouis','age':23,'company':'Pactera'}
print(type(dictionary))
print(dictionary)

# 对应操作：

# 1.查询元素：
print(dictionary['name'])
# 取出字典中所有的键：
print(list(dictionary.keys()))
# 取出字典中所有的值：
print(list(dictionary.values()))

# 遍历字典：
print(dictionary.items())

for item in dictionary.items():
    print(item,end=' ')
print()

# 效率高，建议使用：
for i in dictionary:
    print(i,dictionary[i],end='; ')
print()

# 效率低，不建议使用：
for k,v in dictionary.items():
    print(k,v,end='; ')
print()

# 2.增加元素：
dictionary['hobby']='Coding & Music & Dota2'
print(dictionary)

# setdefault方法是字典增加元素的一种，如果存在该键则不做添加操作，返回当前键对应的值；如果键不存在，则添加该键值对
x=dictionary.setdefault('University','FAFU')
print(x)

dictionary['friends']=[{'name':'Bear','age':28},{'name':'Robin','age':27}]
print(dictionary)

# 3.修改元素：
dictionary['age']=24
print(dictionary)

dictionary['friends'][0]['age']=29
print(dictionary)

for var in dictionary['friends']:
    if var['name'] == 'Bear':
        var['company'] = 'Pactera'

print(dictionary)

# 4.删除元素：
dictionary.pop('friends')
print(dictionary)

del dictionary['company']
print(dictionary)

# clear()方法清空字典内容：
dictionary.clear()
print(dictionary)

# 5.合并字典：
dictionary2={1:'123',2:'abc'}
dictionary.update(dictionary2)
print(dictionary)
print(sorted(dictionary.items(),reverse=True))


