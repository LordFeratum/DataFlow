from itertools import chain, zip_longest, dropwhile, takewhile
from functools import reduce

from .flow import Flow
from .utils import (
    async_map, async_filter, async_reduce, async_dropwhile, async_takewhile
)


class Enum:
    @staticmethod
    def map(transform):
        def _map(data):
            return Flow(map(transform, data))
        return _map

    @staticmethod
    def flat_map(transform):
        def _flat_map(data):
            return Flow(chain.from_iterable(map(transform, data)))
        return _flat_map

    @staticmethod
    def filter(transform):
        def _filter(data):
            return Flow(filter(transform, data))
        return _filter

    @staticmethod
    def reduce(transform, start=None):
        def _reduce(data):
            _start = [] if start is None else start
            return Flow(reduce(transform, data, _start))
        return _reduce

    @staticmethod
    def grouper(n, fillvalue=None):
        def _grouper(data):
            args = [iter(data)] * n
            return Flow(zip_longest(*args, fillvalue=fillvalue))
        return _grouper

    @staticmethod
    def dropwhile(transform):
        def _dropwhile(data):
            return Flow(dropwhile(transform, data))
        return _dropwhile

    @staticmethod
    def takewhile(transform):
        def _takewhile(data):
            return Flow(takewhile(transform, data))
        return _takewhile

    @staticmethod
    def sort(key=None, reverse=False):
        def _sort(data):
            return Flow(sorted(data, key=key, reverse=reverse))
        return _sort


class AsyncEnum:
    @staticmethod
    def map(transform):
        async def _map(data):
            return Flow(await async_map(transform, data))
        return _map

    @staticmethod
    def flat_map(transform):
        async def _flat_map(data):
            return Flow(chain.from_iterable(await async_map(transform, data)))
        return _flat_map

    @staticmethod
    def filter(transform):
        async def _filter(data):
            return Flow(await async_filter(transform, data))
        return _filter

    @staticmethod
    def reduce(transform, start=None):
        async def _reduce(data):
            _start = [] if start is None else start
            return Flow(await async_reduce(transform, data, _start))
        return _reduce

    @staticmethod
    def dropwhile(transform):
        async def _dropwhile(data):
            return Flow(await async_dropwhile(transform, data))
        return _dropwhile

    @staticmethod
    def takewhile(transform):
        async def _takewhile(data):
            return Flow(await async_takewhile(transform, data))
        return _takewhile


class String:
    @staticmethod
    def split(split_by=" "):
        def _split(data):
            return Flow(data.split(split_by))
        return _split

    @staticmethod
    def join(join_by=""):
        def _join(data):
            return Flow(join_by.join(data))
        return _join

