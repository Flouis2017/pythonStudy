# __author : "Flouis"
# date : 2018/03/24

import configparser

# 创建一个配置文件：
cp = configparser.ConfigParser()
# cp['DEFAULT'] = {
#     'username' : 'Administrator',
#     'password' : 'admin123'
# }
# cp['BASIC_INFO'] = {
#     'name' : 'Flouis',
#     'gender' : 'M',
#     'age' : 24
# }
# cp['OCCUPATIONAL_INFO'] = {
#     'profession' : 'Software Engineering',
#     'current_company' : 'Pactera',
#     'salary' : 'RMB5000/month'
# }
# cp['OTHER_INFO'] = {
#     'nation' : 'China',
#     'native_place' : 'Xianyou Fujian',
#     'hobbies' : 'Music/Foreign Language/Coding'
# }
# print(type(cp))
# configfile = open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini','a')
# configfile.flush()
# cp.write(configfile)
# configfile = open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini')
# lines = configfile.readlines()
# for x in lines:
#     print(x)
# configfile.close()

# 读取配置文件的内容：
cp.read(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini')
# print(cp.sections())
# print(cp.defaults())
#
# print(cp['OTHER_INFO']['nation'])

# 遍历configparser对象（本质是一个字典）时，默认会把DEFAULT的节点带上
# for key in cp['OCCUPATIONAL_INFO']:
#     print(key)

# 删除节点后重写文件：
# cp.remove_section('OTHER_INFO')
# cp.write(open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini','w'))

# 添加节点后重写文件：
# cp['OTHER_INFO'] = {
#     'nation' : 'China',
#     'native_place' : 'Xianyou Fujian',
#     'hobbies' : 'Music/Foreign Language/Coding'
# }
# cp.write(open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini','w'))

# 判断是否存在某个节点：
# print(cp.has_section('OTHER_INFO'))

# 更改某个节点下的某个键对应的值：
# cp.set('DEFAULT','username','admin')
# cp.write(open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini','w'))

# 删除某个节点下的某个键值对：
cp.remove_option('OTHER_INFO','native_place')
cp.write(open(r'C:\Users\Administrator\Desktop\temporary\Flouis\example.ini','w'))

