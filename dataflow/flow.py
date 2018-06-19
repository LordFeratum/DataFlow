class Flow:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def from_enumerable(data):
        return Flow(data)

    def __rshift__(self, method):
        return method(self._data)
