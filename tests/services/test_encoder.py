from pyurlshortener.service.counter import ThreadUnsafeCounter
from pyurlshortener.service.encoder import decode, encode


def test_global_counter_and_encoder():
    counter = ThreadUnsafeCounter()
    counter.increment_counter()
    val = counter.get_counter()
    assert encode(val) == "g9"


def test_decoder():
    assert decode("g9") == 1001
