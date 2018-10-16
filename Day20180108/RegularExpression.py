# __author : "Flouis"
# date : 2018/1/8

import re

regStr = r'no*b'
print(re.match(regStr, 'anoobdfw'))
print(re.search(regStr, 'anoobdfw'))

regStr = r'-?([1-9]+\d*)|([0][.]\d*)|([1-9]+\d*[.]\d*)' 
print(re.match(regStr, '-01234'))
print(re.search(regStr, '-01234'))
    
# 使用re.findall(regstr,str)，以regstr为正则式提取str中所有的字符串，返回一个列表：
s = 'adsff00.2ji3.14ji0943uyt'
resultList = re.findall(r'-?(\d+\.?\d*)', s)
print(resultList)

s = '直到世界的尽头。'
resultList = re.findall(r'.*世界.*',s)
print(resultList)
resultList = re.findall(r'.世界.',s)
print(resultList)

s = '直到世界的尽头。你好，明天。'
pattern = re.compile('[\u4e00-\u9fa5]*')
resultList = re.findall(pattern,s)
print(resultList)
resultList = pattern.findall(s)
print(resultList)


print(pattern.finditer(s))
for i in pattern.finditer(s):
    print(i.group())


print(re.finditer(pattern,s))
for i in re.finditer(pattern,s):
    print(i.group())

iterator = pattern.finditer(s)
print(iterator)
resultList = []
while True:
    try:
        # print(next(iterator).group())
        temp = next(iterator).group()
        if temp != '':
            resultList.append(temp)
    except StopIteration:
        break
print(resultList)


    