# __author : "Flouis"
# date : 2018/1/30


# Closure(闭包)

# 在学习Closure之前有必要先复习一下enclosing和local作用域

def outer():
    x = 100         # -->outer方法对于x来说是local域，inner的话是enclosing域
                    # -->x有两种身份local变量对outer方法而言，enclosing变量对inner方法而言。
                    # -->即x是outer方法的local变量，inner方法的enclosing变量。
                    
    def inner():
        y = 'OOXX'  # -->inner方法本身也是outer的一个local变量，y只有一种身份就是inner方法的local变量
        return ( y + str(x) )
    return inner()  # -->注意，这里是返回一个值，不是一个方法名/对象，所以这里虽然在inner方法中调用到了enclosing变量x，但不是闭包

print( outer() )    # -->OOXX

# 闭包结构：

def outer2():
    x = 0
    def inner2():
        y = 1
        print(x+y)
    return inner2   # -->这里返回内部方法对象，即将方法当成一个变量来进行返回，而且在该内部方法中还
                    # -->调用到了enclosing变量，所以outer2-inner2构成了一个闭包结构。

f = outer2()    # 执行此行代码将inner2方法以“变量/对象”的形式传递给变量f
f()             # f此时就是一个方法了，所以f()实际上就等价于在执行inner2()

# 然而问题就出在当执行完f = outer2()这行代码后，即执行完了outer2这个方法体，那么x该变量就应该被回收了，
# 但是在执行f()=>等价于执行inner2方法体中的代码时，x这个本该消亡的变量却能被访问到。

# 所以，闭包与其说是一种代码结构，更恰当的说是一种现象。而且，解释型语言都有这种现象。

# 【小结】：构成闭包的必要表条件：
# ① 方法中有内部方法
# ② 方法中的local变量被内部方法调用/访问
# 此时内部方法就是一个闭包，外部方法就会成为闭包函数。


