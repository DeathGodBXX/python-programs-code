"""利用函数实现上下文管理器功能"""
import contextlib


@contextlib.contextmanager
def open_file(file):
    # __enter__方法
    print('opening file')
    f = open(file, 'w')

    # 实现异常处理
    # yield
    try:
        yield f
    except Exception:
        print('throw exception')
    finally:
        # __exit__方法
        print('close file')
        f.close()


with open_file('info.txt') as f:
    f.write("I'm handsome,everyone likes me\n")
