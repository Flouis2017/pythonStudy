# __author : "Flouis"
# date : 2018/1/23


if True:
    x = 1
print(x)

def f():
    print('before')
    a = 100
    print('after')

# Python的四作用域：built-in > global > enclosing > local
x = int(2.9) # 内置变量
# print(x)
g = 0; # 全局变量


def outer():
    o_count = 1 # enclosing (嵌套变量)
    print('o_count:',o_count)
    def inner():
        i_count = 2 # local variable (局部变量)
        print('i_count:',i_count)
    # print(i_count) # 找不到i_count，因为超出了作用域。
    inner()

outer()


# 方法参数不仅可以变量/对象，还可以传方法：
def square(n):
    return n * n

def foo(a,b,fct):
    return fct(a) + fct(b)

print ( foo(2,3,square) )