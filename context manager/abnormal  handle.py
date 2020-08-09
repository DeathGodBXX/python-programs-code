# 指明异常来源
# try:
#     print(1/0)
# except Exception as exc:
#     raise RuntimeError('Something bad happened') from exc

# try:
#     print(1/0)
# except Exception as exc:
#     raise RuntimeError('Something bad happened').with_traceback(None)

# 关闭异常上下文关联
try:
    print(1/0)
except Exception as exc:
    raise RuntimeError('Something bad happened') from None
finally:
    raise ValueError('value is wrong') from None
