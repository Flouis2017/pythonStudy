# __author : "Flouis"
# date : 2017/12/21

# for loop:

# 1.定长for循环：
for i in range(1,10):
    print(i,end=' ')
print()

# 最后整数是步长：
for i in range(1,11,2):
    print(i,end=' ')
print()

for i in range(1,101):
    if i % 2 == 1:
        print(i,end=' ')

print()

for i in range(1,10):
    if i<5:
        continue
    else:
        print(i,end=' ')

print()

# while循环
counter=0
length=10
while counter<=length:
    if counter<=length-1:
        print(counter,end=' ')
    else:
        print(counter)
    counter += 1


