# __author : "Flouis"
# date : 2017/12/21

# 进行格式化输出：
# %s = 字符串占位符
# %d = 整数占位符
# %f = 浮点数占位符

name = input('Name : ')

while True:
    age = input('Age : ')
    try:
        age = int(age)
        break
    except:
        print('please enter an Age with int type!')
        continue

job = input('Job : ')

while True:
    salary = input('salary : ')
    try:
        salary = float(salary)
        break
    except:
        print('please enter a Salary with float type!')
        continue

msg = '''
------------ info of %s ------------
Name : %s
Age : %d
Job : %s
Salary : %f
You will be retired in %s years
------------------------------------
''' % (name, name, age, job, salary, 65 - int(age))

print(msg)
