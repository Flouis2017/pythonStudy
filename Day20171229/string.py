# __author : "Flouis"
# date : 2017/12/29

# 字符串String操作
# 首先要说明的是在Python中没有字符的概念，只有字符串的概念，这个和JavaScript一样。

# 1.重复输出某个字符串
string='hello'
print(string*2)

# 2.使用[]将字符串转化为一个列表
print(string[2:])

# 3.in判断字符串是否包含某个子串
print('el' in string)

# 4.字符串拼接
string2 = " world!"

# 效率低，不推荐使用：
string3 = string + string2
print(string + string2)

# 效率高，推荐使用：
string3=''.join([string,string2])
print(string3)

# Python字符串内置方法：
# 1.统计子串的个数：
string = 'asdfrqwejkl;zxcvasdf'
print(string.count('as'))

# 2.将字符串首字母大写：
print(string.capitalize())

# 3.---------------asdfrqwejkl;zxcvasdf---------------
print(string.center(50,'-'))

# 4.判断是否以某个子串结尾：
print(string.endswith('df'))

# 5.判断是否以某个子串开头：
print(string.startswith('asd'))

# 6.字符串分割：
result=string.split(';')
print( type( result ) )
print(result)

# 7.find方法，查找第一个子串的位置：
result_index=string.find('a')
print(result_index)

# 8.格式化输出：
string2='hello {name}'
print(string2.format(name='Flouis'))


# 9.判断是否是只包含数字的字符串：
string3 = '01234'
print(string3.isdecimal())
string3 = ''.join(['a',string3])
print(string3.isdecimal())

# 10.判断字符串是否包含字母或数字：
print(string3,' isalnum:',string3.isalnum())
print('123 isalnum:','123'.isalnum())
print('asdf isalnum:','asdf'.isalnum())

# 11.判断是否为一个整数的字符串：
print('1230'.isdigit())
print('01230'.isdigit())
print('123.123'.isdigit())


# 12.判断字符串全部为小写：
print('abc'.islower())
print('Abc'.islower())

# 13.判断字符串是否全部为大写：
print('ABC'.isupper())
print('aBC'.isupper())

# 14.大小写互转：
print('My'.lower())
print('My'.upper())
print('abc'.swapcase())
print('ABC'.swapcase())

# 15.去掉前后空格和换行：
print('\tHello,world!\n')
print('\tHello,world!\n'.strip())

# 16.字符串替换：
string='usb_kingston'
print(string.replace('u','myu'))
print(string.replace('kingston','histon'))


