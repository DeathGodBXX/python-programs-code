from tenacity import retry


@retry
def test_retry():
    """抛出异常，即时重试"""
    print('等待重试......')
    raise Exception


test_retry()





















