"""
演示的模块的导入
"""
# 导入模块>>>全部导入
# import 模块#灰色表示还未使用
"""
import 模块名  as 新名称 #模块名冲突，换一个新名称，或者模块名过长
模块名.类名
模块名.函数名
模块名.变量
"""

"""
模块的局部导入
from 模块名 import 资源名
from 模块名 import 资源名1，资源名2
from 模块名 import *
"""
"""
演示运行的代码的程序管理==程序的入口
"""
# 包的导入
# import 10_import.demo1  #导入子模块，必须全名访问
# 10_import.demo1.demo1()

# import 10_import.demo1 #from 包  import 模块名，就利用模块名.函数名访问
# 10_import.demo1.demo1()

# from 10_import.demo1 import demo1 #from 包.模块 import 函数名 ，可以直接函数名调用
# demo1()

# import xx 后面只能写道模块，不能写到函数
# import xx.xx.xx 后面最多写到模块，不能写到函数
# from xx import xxx ,import后面能写到函数，包，模块等

# from 10_import import *
# demo1.demo1()

# from 1_type import type  #可以直接导入模块，不是函数也可以，在另一个。py中执行
# type

"""
关于导入模块，自己写的程序，自己也可以把它保存下来，以后需要的时候导入使用，例如下面所示。
我有个代码名称为 test1.py，它的所在路径为 D:\test 下面。那我只需要完成以下步骤就可以把它作为模块 import 到其他代码中了。
 1.import sys
 2.sys.path.append("D:\\test")
在 test2.py 中我们就可以直接 import test1.py 了。成功导入后，test1中 的方法也就可以在 test2 中进行使用

"""
# import sys
# print(sys.path)





