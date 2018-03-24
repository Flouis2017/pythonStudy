# __author : "Flouis"
# date : 2018/03/22

import hashlib

# md5 algorithm
m = hashlib.md5()
# print(m)
m.update('123456'.encode('utf8'))
print(m.hexdigest())

m.update('Flouis'.encode('utf8'))
print(m.hexdigest())

m2 = hashlib.md5()
m2.update('123456Flouis'.encode('utf8'))
print(m.hexdigest())

s = hashlib.sha256()
s.update('helloworld'.encode('utf8'))
print(s.hexdigest())

