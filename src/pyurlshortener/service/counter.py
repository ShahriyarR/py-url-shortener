class ThreadUnsafeCounter:

    def __init__(self):
        self._counter: int = 0

    def increment(self):
        self._counter += 1

    def value(self):
        return self._counter
