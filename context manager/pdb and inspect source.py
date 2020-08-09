def div(x, y):
    print(x/y)
    1 / 0


div(1, 2)

# python -i "pdb and inspect source.py"
# import pdb
# pdb.pm()
# l 显示错误附近的源码
# 输入源码进行调试

# import inspect
# inspect.getsource(div) 获取函数div的源码
