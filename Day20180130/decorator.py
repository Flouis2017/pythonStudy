# __author : "Flouis"
# date : 2018/1/30

import time

def foo():
    time.sleep(2)
    print('asdf')

def bar():
    time.sleep(3)
    print('qwer')

def show_time(f):
    start_time = time.time()
    f()
    end_time = time.time()
    spend_time = end_time - start_time
    print('Spended time:',spend_time)
    
# show_time(foo)
# show_time(bar)

# 通过上述的show_time方法固然可以达到显示执行时间的效果，但是这里有个需求就是调用原来的方法实现同样的功能。
# 换句话说——在不改变foo原本方法体的前提下(间接地)对foo方法进行功能的扩充，怎么做？——使用闭包！

def show_time2(f):
    
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        spend_time = end_time - start_time
        print('Spended time:',spend_time)
        
    return inner

foo = show_time2(foo)
foo()   # 结果和上面直接调用show_time(foo)一致。

# 这里inner()方法(函数)和show_time2(f)方法构成闭包结构，inner()就是一个闭包。
# show_time2(f)就是一个闭包方法(函数)，也称为装饰器——因为通过这个闭包方法可以在不改变其他方法原本方法体
# 的前提下对其他方法进行功能的扩充。

# 为了代码更优雅，Python专门提供了装饰器的注解：

@show_time2 # 就等价于 kau = show_time2(kau) 这句话
def kau():
    print('相変わらず')
    time.sleep(1)

kau()



    