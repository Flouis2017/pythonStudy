
import re
# =======================================================================
pat = "ais"
string = "You raise me ais up"

# search(re, str)：搜索匹配str中re首次出现的下标元组
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(5, 8), match='ais'>

pat = "Ame"
rst = re.search(pat, string)
print(rst) # None (空指针)

pat = "\t"
string = '''asdf
qw	er'''
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(7, 8), match='\t'>

# =======================================================================
# 通用字符匹配
# pat = "\w" # 匹配任意一个字母、数字和下划线，\W则相反匹配
# pat = "\d" # 匹配任意一个十进制数，\D则相反匹配
# pat = "\s" # 匹配任意一个空白字符(注意：换行、制表符都算是空白字符)，\S则相反匹配
pat = "\w\dpython\w"
string = "asdf3python_zxcv"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(3, 12), match='f3python_'>

# =======================================================================
# 原子表 —— 平等匹配
pat = "a[bcd]e"
string = "wersacej"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(4, 7), match='ace'>

# =======================================================================
# 元字符(正则表达式中具有特殊含义的字符，如果要匹配本身需进行转义)：\ . ^ $ * ? + {}
'''
\: 转义字符
.: 匹配任意一个字符
^: 匹配字符串开始的位置
$: 匹配字符串结束的位置
*: 匹配之前字符出现任意次
?: 匹配之前字符出现或不出现
+: 匹配之前字符至少出现一次
{}:限定符，里面是自然数n或区间[n, m](m>=n)，含义：匹配之前字符出现n次或n~m次，
写成{n,}表示匹配之前字符至少出现n次
'''
pat = ".{3,}"
string = "aabtang"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(0, 7), match='aabtang'>

pat = "a{1,}"
rst = re.search(pat, string)
print(rst) # <_sre.SRE_Match object; span=(0, 2), match='aa'>

# =======================================================================
# 模式修正符
'''
I: 忽略大小写进行匹配
M: 进行多行匹配
L: 本地化识别匹配(暂时不学)
U: 使用Unicode字符集对匹配内容进行解析
'''
pat = "python"
string = "ahfjwnfebvPythonuiohop"
rst = re.search(pat, string)
print(rst) # None
# 忽略大小写进行匹配：
rst = re.search(pat, string, re.I)
print(rst) # <_sre.SRE_Match object; span=(10, 16), match='Python'>

# =======================================================================
# 贪婪模式和懒惰模式
# 贪婪模式的核心是尽可能多地匹配，懒惰模式则是尽可能少地匹配
# 贪婪模式关键符：*	懒惰模式关键符：?	例子如下：
greedy_pat 	= "p.*y"
lazy_pat	= "p.*?y"
string = "ilovepythonprogrammingpy"
rst = re.search(greedy_pat, string)
print(rst) # <_sre.SRE_Match object; span=(5, 24), match='pythonprogrammingpy'>
rst = re.search(lazy_pat, string)
print(rst) # <_sre.SRE_Match object; span=(5, 7), match='py'>
# 结果比较：贪婪模式匹配的内容更丰富，懒惰模式匹配的内容更精准

# =======================================================================
# 常用的正则表达式函数：re.match() / re.search() / 全局匹配函数 / re.sub() [暂时不学]
# re.match()和re.search()的区别是：re.match()从左第一个字符开始匹配，re.search()遍历匹配
string = "fjiwhdvbpasfeyyetwpy"
rst = re.match(lazy_pat, string)
print(rst) # None
# 全局匹配：
rst = re.compile(lazy_pat, re.I).findall(string)
print(rst) # ['pasfey', 'py']

# =======================================================================
print("===============================实例========================================")
print("实例1. 匹配超链接中的网址：")
pat = "[a-zA-Z]+://[\S]*\.com|cn"
string = '<a href="https://www.baidu.com/">asdf</a>'
print(string)
rst = re.compile(pat).findall(string)
print(rst)

import urllib.request
print("实例2. 爬取豆瓣阅读中的出版社")
pat = '<div class="name">(.*?)</div>'
# string = '<div class="name">博集天卷</div>'
# rst = re.compile(pat).findall(string)
# print(rst)
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf8")
rst = re.compile(pat).findall(str(data))
print(rst)

