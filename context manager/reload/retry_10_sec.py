from tenacity import retry, stop_after_delay


@retry(stop=stop_after_delay(10))
def test_retry():
    print('等待重试....')
    raise Exception


test_retry()

