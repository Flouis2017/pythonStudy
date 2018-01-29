# __author : "Flouis"
# date : 2018/1/23


def f():
    print('go lang')
    # return None

# 【注意】：Python中的空值是None，和Java中的null是一个概念。
# 在Python中不写return，默认是return None
a = f()
print(a)

def add(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

num_arr = [1, 2, 3, 4, 5]
print( add( num_arr ) )


# 如果返回多个对象/数据，那么Python会自动封装为一个元组进行返回，例子如下：
def f():
    return 1,'Flouis',[1,2,3]

print( f() )
# console result：(1, 'Flouis', [1, 2, 3])





