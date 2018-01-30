# __author : "Flouis"
# date : 2018/1/30

# 和其他解释型语言类似，Python也可以像JavaScript那样把方法名作为参数传入
# 另一个方法中——原理就是解释型语言是弱类型的，一切都是对象。
# 所以，在Python、JavaScript这些语言里会出现使用方法来赋值的情况。
# 这种用法有个专有名称——高阶函数。

def f(arg):
    print( str(arg) )
    
a = f('OK')
a

def foo(f):
    print( f('Wow!') )
    
foo(f)