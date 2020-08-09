from tenacity import retry, stop_after_attempt, wait_fixed


# 使抛出的异常是Exception，而不是retryError,抛出原始错误
@retry(stop=stop_after_attempt(7), wait=wait_fixed(1), reraise=True)
def test_retry():
    print('等待重试....')
    raise Exception


test_retry()

