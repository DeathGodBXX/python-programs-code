def hot_dry_noodle(c):
    def b():
        c()
        print('热干面最好吃,',end='')

    return b


def stewed_noodle(c):
    def b():
        c()
        print('烩面太难吃.')

    return b


@stewed_noodle
@hot_dry_noodle
def province():
    print('河南省,', end='')


province()
