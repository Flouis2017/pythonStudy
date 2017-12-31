# -*- coding:utf-8 -*-
# __author : "Flouis"
# date : 2017/12/31

# 编码/解码格式在Python2中默认是ASCII码，在3之后的版本中是Unicode
s='特斯拉'
print(s)

s_to_gbk=s.encode('gbk')
print(type(s_to_gbk),s_to_gbk)
print(s_to_gbk.decode('gbk'))





