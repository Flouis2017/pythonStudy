# __author : "Flouis"
# date : 2018/3/3

s = (x*2 for x in range(5))
print(s) # <generator object <genexpr> at 0x0000026493DA1D00>

# 加了两个下划线的都是Python 2的内部方法，一般不直接使用
#print(s.__next__()) # 0

# 在Python 3中使用next访问生成器中的元素
#print(next(s))
#print(next(s))

#for i in s:
#    print(i)
    
# 生成器就是一个可迭代对象(Iterable)
# 可迭代对象都有一个优点——内存效率高，因为每次迭代完成，都会将上一次迭代的内存回收。
# 那么什么是可迭代对象？
# 答：对象中有iter方法对象都是可迭代对象

# 生成器一共有两种创建方式：
# 第一种是通过()来创建
# 第二种是通过yield关键字来创建的

def foo():
    print('abc')
    yield 1
    
    print('def')
    yield 2
    
foo() # <Nothing>
print(foo())
g = foo()
print(g)

next(g)
print( next(foo()) )
next(g)

print('============================sent()============================')
def bar():
    print('abc')
    count = yield 1
    
    print(count)
    yield 2
    
b = bar()
# b.send(<arg>)等效于next(b)，都是进入生成器中的方法。
# 但是使用send()时，得加参数，如果是第一次进入生成器，这个参数必须是None
b.send(None)        # abc

# send(<arg>)方法的好处就是可以传递参数
b.send('xyz')       # xyz



