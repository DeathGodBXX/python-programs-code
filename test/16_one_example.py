class Man:
    __instance = None

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Man)
        return cls.__instance

    def func(self):
        pass


man1 = Man('ok')
man2 = Man('else')
if id(man1) == id(man2):
    print('单例模式开启')
else:
    print('非单例模式')
