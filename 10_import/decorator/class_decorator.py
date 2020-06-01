"""
     让类的构造函数__init__()接受一个函数，然后重载__call__()并返回一个函数，也可以达到装饰器函数的效果。
"""
"""class decorator 和class decorator02区别在于把自由参数func放在哪里"""

class hot_dry_noodle():
    def __init__(self, func):
        self.func = func   # 初始化类似于装饰器

    # def __call__(self, args, **kwargs):  # 把类想成一个函数
    #     self.func(args)
    #     print('热干面真好吃')  # 可以在类里执行，不用返回

    # return self.func(args=args + '热干面真好吃', **kwargs)

    def __call__(self, args, **kwargs):
        print('热干面真好吃,', end='')
        return self.func(args)

    def __str__(self):
        pass


@hot_dry_noodle
# hot_dry_noodle(province)(args) 等价于 实例对象province=hot_dry_noodle(province)   call方法f(args) 左端项可能是自动补充的
def province(args):
    print('{}'.format(args), end='')


# province=hot_dry_noodle(province)


if __name__ == '__main__':
    province('河南省')
    # hot_dry_noodle(province)('湖南省')  # 看着像是对province再装饰了一次
    # print(type(province))
    # hot_dry_noodle('湖北省')  # 这是hot_dry_noodle的实例化对象
