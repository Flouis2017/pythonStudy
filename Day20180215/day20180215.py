# __author : "Flouis"
# date : 2018/2/15

def f():
    x = 1
    def inner():
        y = 2
        return x+y
    return inner

print( f() ) # <function f.<locals>.inner at 0x000002D9B74B28C8>
foo = f()
print( foo() ) # 3

