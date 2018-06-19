from itertools import chain, zip_longest
from functools import reduce

from .flow import Flow


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
