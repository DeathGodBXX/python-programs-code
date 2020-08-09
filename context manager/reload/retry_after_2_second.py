from tenacity import retry, wait_fixed


@retry(wait=wait_fixed(2))
def test_retry():
    print('等待重试....')
    raise Exception


test_retry()















