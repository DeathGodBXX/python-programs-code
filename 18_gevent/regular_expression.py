# import re
# data = re.match(r'bobo','bobo,bobo,你真傻逼') #正则表达式的规范，匹配内容
# print(data)
# data = re.match(r'sisi','bobo,bobo,你真傻逼')
# print(data)


import re

"""
爬虫
"""
# 反斜杠只匹配一位数字
# data = re.match(r'陆小凤传奇\d','陆小凤传奇11')
# print(data)
# demo = data.group() #提取匹配成功的数据
# print(demo)


# 只要匹配到123456中一个就返回
# data = re.match(r'陆小凤传奇[123456]','陆小凤传奇5')
# print(data)
# demo = data.group() #提取匹配成功的数据
# print(demo)

# 都是匹配一个字符
# data = re.match(r'陆小凤传奇[1-6a-d]','陆小凤传奇a')
# print(data)
# demo = data.group() #提取匹配成功的数据
# print(demo)

# \w 匹配a-z,A-Z,0-9,_ 匹配范围过大，也能匹配汉字
# data = re.match(r'陆小凤传奇\w','陆小凤传奇帅')
# print(data)
# demo = data.group() #提取匹配成功的数据
# print(demo)

# 多个字符，无法规定数据类型，后面的大括号的数值指示前面数据出现的次数
# 单个字符可以指定数据类型，\d{m},表示m个整形数，\d{m,n}表示m到n个整形数据都可以


data = re.match(r'陆小凤传奇\d{1,2}', '陆小凤传奇11,陆小凤传奇8')
data1 = re.match(r'陆小凤传奇\d{1,2}', '陆小凤传奇8,陆小凤传奇11')
print(data)
print(data1)  # 开头开始匹配，结尾多余也没关系
demo = data.group()  # 提取匹配成功的数据
demo1 = data1.group()  # 提取匹配成功的数据
print(demo)
print(demo1)

# 看哪个在前，就先匹配到哪个。。
