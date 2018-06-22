import asyncio

from .exceptions import NoEventLoopDefined


class Flow:
    def __init__(self, data, loop=None):
        self._loop = loop
        self._data = data

    @staticmethod
    def from_enumerable(data, loop=None):
        return Flow(data, loop=loop)

    @property
    def event_loop(self):
        return self._loop

    @event_loop.setter
    def event_loop(self, loop):
        self._loop = loop

    def __rshift__(self, method):
        if asyncio.iscoroutinefunction(method):
            if self._loop is None:
                raise NoEventLoopDefined()

            f = self._loop.run_until_complete(method(self._data))

        else:
            f = method(self._data)

        if isinstance(f, Flow):
            f.event_loop = self._loop

        return f
