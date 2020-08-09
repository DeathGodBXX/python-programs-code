from tenacity import retry, stop_after_delay, stop_after_attempt, wait_fixed


@retry(stop=(stop_after_delay(10) | stop_after_attempt(7)), wait=wait_fixed(1))
def test_retry():
    print('等待重试.....')
    raise Exception


test_retry()
