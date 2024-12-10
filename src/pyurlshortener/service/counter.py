class ThreadUnsafeCounter:

    def __init__(self):
        self._counter: int = 1000

    @classmethod
    def create(cls):
        return cls()

    def increment_counter(self, key: str | None = None, amount: int = 1):
        self._counter += 1

    def get_counter(self, key: str | None = None):
        return self._counter
