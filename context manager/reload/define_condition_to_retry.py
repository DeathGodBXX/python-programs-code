from tenacity import retry, stop_after_attempt, retry_if_result, wait_fixed


def is_false(value):
    return value is False


@retry(stop=stop_after_attempt(7), wait=wait_fixed(1), retry=retry_if_result(is_false))
def test_retry():
    print('等待重试....')
    return False


test_retry()
