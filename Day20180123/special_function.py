# __author : "Flouis"
# date : 2018/1/23


# 阶乘：
def factorial(n):
    res = 1
    while n > 0 :
        res = res * n
        n = n - 1
    return res

res = factorial(4)
print(res)

# 递归方法进行阶乘：
def factorial2(n):
    # 结束递归的条件：
    if n==1:
        return 1
    return n*factorial2(n-1)

print(factorial(4))

# 递归执行效率较低，而且递归算法都能够用循环实现。