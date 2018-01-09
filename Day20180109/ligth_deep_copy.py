# __author : "Flouis"
# date : 2018/1/9

mylist = ['Flouis',23,'Software Engineering']

# 深拷贝的原理——在堆中开辟另一个存储空间，重新被另一个引用指向。
# 以下是最原始的做法：
mylist_backup = ['Flouis',23,'Software Engineering']
mylist[0] = 'Carl Lin'
print('mylist:',mylist)
print('mylist_backup:',mylist_backup)
#print(mylist==mylist_backup)
#print(mylist is mylist_backup)
print()

# 使用对象的copy()方法可以进行深拷贝。
mylist2 = mylist_backup.copy()
mylist2[1] = 24
print('mylist2:',mylist2)
print('mylist_backup:',mylist_backup)
#print(mylist2==mylist_backup)
#print(mylist2 is mylist_backup)
print()

# 所谓浅拷贝——就是直接将引用进行赋值，所以结果就是两个引用指向同一个堆空间，
# 这样造成的后果就是，改一个另一个也会跟着变掉。
mylist3 = mylist_backup
mylist3[2] = 'Translator'
print('mylist3:',mylist3)
print('mylist_backup:',mylist_backup)
#print(mylist3==mylist_backup)
#print(mylist3 is mylist_backup)
print()

str1 = 'abc'
str2 = 'abc'
print(str1==str2)
print(str1 is str2)

str1 = str('abcd')
str2 = str('abcd')
print(str1 == str2)
print(str1 is str2)



