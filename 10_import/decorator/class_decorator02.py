class hot_dry_noodle():
    def __init__(self):
        pass

    def __call__(self, func):  # 类似于装饰器
        def b(args):
            func(args)
            print('热干面真好吃')

        return b


@hot_dry_noodle()
# 必须要加小括号 先初始化实例对象，即获得hot_dry_noodle()可调用对象,可调用函数
# 等价于f=hot_dry_noodle(),province = f(province),最后再调用province('args')
def province(args):
    print(args, ',', end='')


province('河南省')
