def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'开始执行{func.__name__}')
        func(*args, **kwargs)
        print('执行结束')

    return wrapper


@decorator
def add(x, y):
    print(f'{x}+{y}={x + y}')


add(20, 30)
