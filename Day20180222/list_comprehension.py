# __author : "Flouis"
# date : 2018/2/22

# 列表生成器/式，通过[f(x) 对x进行遍历操作的语句]来完成。

list_a = [1,3,4,5,7]

a = [x*2 for x in list_a]
print(a)

def f(x):
    return x*x*x

b = [f(n) for n in range(5)]
print( type(b) , b )
