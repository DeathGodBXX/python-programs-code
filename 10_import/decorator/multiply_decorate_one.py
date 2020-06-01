def hot_dry_noodle(c):
    def b(args):
        c(args)
        print('热干面最好吃,',end='')

    return b


def stewed_noodle(c):
    def b(args):
        c(args)
        print('烩面太难吃.')

    return b


@stewed_noodle
@hot_dry_noodle
def province(args):
    print(args, ',', end='')
    print(province)


province('河南省')
