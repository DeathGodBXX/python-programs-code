"""出现特定错误，重试"""
from tenacity import retry,retry_if_exception_type
from requests import exceptions


@retry(retry=retry_if_exception_type(exceptions.Timeout))
def test_retry():
    print('等待重试.....')
    raise exceptions.Timeout


test_retry()









