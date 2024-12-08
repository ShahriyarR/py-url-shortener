from pyurlshortener.service.counter import ThreadUnsafeCounter


def test_counter_increment_and_value():
    counter = ThreadUnsafeCounter()
    # the counter starts from 0
    assert counter.value() == 0

    counter.increment()
    counter.increment()
    assert counter.value() == 2
