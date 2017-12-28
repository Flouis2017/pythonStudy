# __author : "Flouis"
# date : 2017/12/27


# Python中列表的概念等同于Java/C++的数组

arr = ['abc','def','ghi','jkl','xyz']
print(arr[0],end=' ' + str(len(arr)))
print()

# 列表的切片：
print(arr[1:]) # 从下标为1的元素取到最后一个元素
print(arr[1::2]) # 从下标为1的元素取到最后一个元素，步长为2
print(arr[1:-1]) # 从下标为1元素取到倒数第二个元素

# 列表新增元素——append：
arr.append('Flouis')
print(arr)
arr.append(2018)
print(arr)

# 列表新增元素到任意一个位置——insert：
# 注意：这个位置是相对的
arr.insert(-3,'xx')
arr.append('xx')
print(arr)

# 列表修改某个位置上的元素：
arr[1]='XML'
print(arr)

# 查询列表中特定元素的索引——取下标：
index = arr.index( 'Flouis' )
print('index of \'Flouis\' is ',end=str(index))
print()

# 列表按照内容删除元素——remove，如果有重复内容，只会删除第一个
arr.remove('xx')
print(arr)

# 列表按照索引删除元素——pop，无参数时候默认删除列表最后一个元素
arr.pop(2)
print(arr)
print( 'index of \'Flouis\' is ',end=str( arr.index('Flouis') ) )

# 【小结】：remove只能删除一个元素，比如例子列表arr中有两个'xx'元素，remove('xx')只能删掉最先出现的

print()
# 列表中某个元素出现的次数——count
print('The times of \'xx\' in arr list:',arr.count('xx'))

# 列表合并
a=[1,2,'Tom']
b=['Jack','Carl',100]
a.extend(b)
print('\n',end=str(a))
print()
print(a[a.index(100)])

# 列表反向
a.reverse()
print(a)

# 列表排序——sort方法：字符串按照ASCII码排序，数字默认从小到大
arr=[2,1,5,9,0]
arr.sort(reverse=True)
print(arr)


print (type(arr) is list)