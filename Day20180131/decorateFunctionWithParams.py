# __author : "Flouis"
# date : 2018/1/31

import time

# 显示执行时间的装饰器：
def show_time(f):
    def inner(a,b):
        start_time=time.time()
        f(a,b)
        end_time=time.time()
        print('Spended time:',end_time-start_time)
    return inner


# 显示执行时间的装饰器2——任意参数：
def show_time2(f):
    def inner(*a,**b):
        start_time=time.time()
        f(*a,**b)
        end_time=time.time()
        print('Spended time:',end_time-start_time)
    return inner


@show_time
def commonAdd(a,b):
    print(a+b)
    time.sleep(1)
    
#commonAdd(1,2)

# 在Python中接收任意参数使用*和**
# 其中*的参数会将每个单独元素存放在一个元组里面
# **的参数是会将每个等式元素存放在一个字典中
@show_time2
def add(*a,**kw):
    print('*a:',a)
    print('**kw:',kw)
    res = 0
    for i in a:
        res += i
    print(res)
    time.sleep(1)
        
#add(1,2,3,1,9,a='aesdf',b=24)


# 在装饰器注解中使用参数：
# 如有一个新的需求，在显示时间的装饰器中通过一个变量来判断是否进行日志记录，怎么做？
# 我们可以将装饰器做成一个闭包，即在外部在套上一个带参函数，然后在需要记录的时候在注解位置加上相应参数即可。

def log(flag=False):
    
    def show_time(f):
        
        def inner(*a):
            start_time=time.time()
            f(*a)
            end_time=time.time()
            print('Spended time:',end_time-start_time)
            if flag==True:
                print('日志记录')
        return inner
    
    return show_time

#@log()
flag=True
@log(flag)
def add2(*a):
    res=0
    for i in a:
        res+=i
    print(res)
    time.sleep(1)
    
add2(1,4,5,9)


# 【小结】：
# 闭包是Python——解释型语言特有的写法。
# 闭包的作用，最主要的就是为了在不改变原本方法体的前提下对方法进行功能扩充，这点和Java中的动态代理很像。
# 或者说就是Python中实现动态代理的一个手段——通过闭包。
# 因此，闭包函数/方法也称为装饰器。
# 为了使代码更优雅，更易于维护，所以推荐使用注解的形式来加载装饰器。
# 需要使用额外的参数时，只需要在原本的装饰器外部再套一个(一个就够，不要连环套，因为使用*和**就可以接收任意参数了)
# 装饰器(外部函数)即可，然后在需要的功能方法前进行最外部装饰器的注解，附上参数即可。
 
 




