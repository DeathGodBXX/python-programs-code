from tenacity import retry, stop_after_attempt, retry_if_result, wait_fixed


def return_last_value(retry_state):
    print('执行回调函数....')
    return retry_state.outcome.result()


def is_false(value):
    return value is False


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1),
       retry_error_callback=return_last_value, retry=retry_if_result(is_false))
def test_retry():
    print('等待重试....')
    return False


test_retry()

# 不要更换左侧的关键字参数
