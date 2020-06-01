def factory(active=True):  # 装饰器工厂函数，接受装饰器的参数
    def hot_dry_noodle(c):  # 装饰器
        def b(args):  # 这是未被装饰的函数的参数，类型和个数必须一致
            c(args)
            if active:
                print('热干面最好吃')
            else:
                print('gabage，连热干面都没有')

        return b

    return hot_dry_noodle


@factory()
def province(args):
    print(args, end='')


@factory(active=False)
def province01(args):
    print(args, end='')


if __name__ == '__main__':
    province('河南省')
    province01('湖北省')
