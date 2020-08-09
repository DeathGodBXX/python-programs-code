# class append():
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'调用{self.func.__name__}')
#         self.func(*args, **kwargs)
#
#
# @append
# def say(something):
#     print(f'say {something}')
#
#
# say('hello')


# class append():
#     def __init__(self):
#       "bugs since __init__ takes 1 positional argument but 2 were given"
#         ...
#
#     def __call__(self, func, *args, **kwargs):
#         print(f'调用{func.__name__}')
#         func(*args, **kwargs)
#
#
# @append
# def say(something):
#     print(f'say {something}')
#
#
# say('hello')

class decorate():
    def __init__(self, INFO="LOGGING"):
        self.info = INFO

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'{self.info}:{func.__name__} is running:')
            func(*args, **kwargs)
        return wrapper


@decorate(INFO='WARNING')
def say(something):
    print(f'say {something}')


say('good night')


# Conclude:
#      不带参数的类装饰器，init方法接收函数名，call实现装饰功能
#      带参数的类装饰器，init方法接收参数，call接收函数名，内部还有定义具有装饰功能的函数
#   总而言之，init接收最外层信息，call次之，最后内部实现装饰功能。
