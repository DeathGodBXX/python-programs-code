"""
上下文管理器
只要存在__enter__和__exit__方法就能实现上下文管理器功能
enter实现进入管理器所需要的操作
exit实现退出管理器会发生的操作，可以添加异常处理信息，这样不会显得臃肿
如果return True,告诉管理器已被捕捉，不需要抛出，直接后续执行
"""


class Resource:
    def __enter__(self):
        print('in __enter__')
        return self  # 注意一定要返回实例对象，成为上下文管理器

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('in __exit__')
        return True

    def operator(self):
        print('in operator')
        1/0


with Resource() as f:
    f.operator()
