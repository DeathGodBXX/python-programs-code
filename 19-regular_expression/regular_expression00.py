#\s匹配空白 ，空格，tab键
#\S匹配非空白    .匹配到任意字符,除了\n 贪婪匹配
# ctrl+f 查找


"""
正则表达式用以提取字符串

"""
import re
#re是python内置的库 regex

import re
# print(re.match('six.star.cn','six star.cn').group())
# print(re.match('[hHab]','Hello Python').group()) #[]中任一字符，第一个匹配到的
# print(re.match('[0123456789]','77hello Python').group())
# print(re.match('[0123456789]hello Python','77hello Python').group())#匹配不到，两个7
# print(re.match('[0123456789]hello Python','7hello Python').group())
# print(re.match('[0-35-9]Hello Python','7Hello Python').group())
#匹配0到3，5到9
# *,匹配前一个字符出现0到无限次，可有可无
# +，匹配前一个字符出现1次到无限次
#？，匹配前一个字符出现0次或1次
# print(re.match('[A-Z][a-z]*','MM').group())
# print(re.match('[A-Z][a-z]*','Mabst').group())

# print(re.match('[1-9]\d?$|100','10').group())
#$表示以前一个字符结尾，|表示或者

# print(re.match(r'<([a-zA-Z]*)>\w*</\1>','<html>hh</html>').group())
#把需要匹配的文本用括号分组，再后续部分，可以用\1代替前面分组中匹配到的字符

#(?P<name>) 取别名  (?P=name)使用别名
# print(re.match(r'<(?P<name>[a-zA-Z]*)>\w*<(?P=name)>','<html>hh<html>').group())

# r是转义\


# ret = re.search(r'\d+','阅读次数9999，人数89')
# print(ret.group())

#不从头开始匹配，只要文本中能够匹配到，就匹配到；只匹配一次

# ret = re.findall(r'\d+','python=9999,re=3474,ok=8880')
# print(ret)


data = '今天天气很好'
# print(re.match('.*?天',data).group())
print(re.match('.*天', data).group())

#*前面尽可能多匹配，？前面尽可能少的匹配







