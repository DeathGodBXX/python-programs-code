"""嵌套的上下文管理器"""
import contextlib


@contextlib.contextmanager
def nest_manager(name):
    print(f'enter,my name is {name}')
    yield
    print(f'exit,my name is {name}')


# with nest_manager('aa'):
#     with nest_manager('bb'):
#         print('in main')

with nest_manager('aa'), nest_manager('bb'):
    print('in main')
