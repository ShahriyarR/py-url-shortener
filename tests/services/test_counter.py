from pyurlshortener.service.counter import ThreadUnsafeCounter


def test_counter_increment_and_value():
    counter = ThreadUnsafeCounter()
    # the counter starts from 0
    assert counter.get_counter() == 1000

    counter.increment_counter()
    counter.increment_counter()
    assert counter.get_counter() == 1002
