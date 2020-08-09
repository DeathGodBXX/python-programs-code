import inspect


# 装饰器工厂函数，传递参数, 限制调用函数，如果没有参数，不加限制
def call_stack_check(valid_func_list=None):
    # 装饰函数(装饰器)
    def decorate(func):
        # 装饰器附加功能
        def wrap(*args, **kwargs):
            if valid_func_list:
                stack = inspect.stack()
                call_func = stack[1].function
                if call_func not in valid_func_list:
                    raise Exception(f'不在{valid_func_list}中')
                else:
                    print(f'在{valid_func_list}中')
                    result = func(*args, **kwargs)
            return result

        return wrap

    return decorate


@call_stack_check(['jump'])
def foot_up():
    print('双脚离地')

# 上述定义等价于下面的定义
# def foot_up():
#     stack = inspect.stack()
#     call_func = stack[1].function
#     if call_func != 'jump':
#         print('不是jump函数调用')
#     else:
#         print('是jump函数调用', '双脚离地')


def jump():
    print("既然跳舞，肯定要跳起来")
    foot_up()


def dance():
    print("开始跳舞")
    jump()


try:
    dance()
except Exception as e:
    print(e)
