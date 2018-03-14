# __author : "Flouis"
# date : 2018/03/14

import random
# Very attention: we can not create a python file named 'random',because that would lead to
# clash with the random module built in.
from collections import Iterator,Iterable


# generate decimal from 0 to 1
print(random.random())          # 0.22964491481155092

# generate integer from section of [int1,int2]
print(random.randint(1,8))      # 1~8


# generate one element from argument of sequence object
print(random.choice('hello'))   # 'h'/'e'/'l'/'o'

print( random.choice( [ 'Flouis' , 24 , [1,2] ] ) )

l = [1,2,3,4,5,6]
# disorganize a sequence object:
random.shuffle(l)
print(l)

# return a random list with specified length
print(random.sample('world',2))  # ['r', 'd']

# return a ramdom integer from section of [int1,int2)
print(random.randrange(1,3))

print('===============================================================')

# print(ord('a'),ord('z')) # 97 122
# print(ord('A'),ord('Z')) # 65 90

# generate verification code：
def generate_code(length):
    code = ''
    for i in range(length):
        code_num = random.randrange(10)
        code_alphabet_upper = chr(random.randint(65,90))
        code_alphabet_lower = chr(random.randint(97,122))
        code += str(random.choice([code_num,code_alphabet_upper,code_alphabet_lower]))
    return code

verification_code = generate_code(5)

print(verification_code)