from collections.abc import Iterator, Sequence
from typing import overload, TypeVar, Callable, Iterable
import functools
import itertools


T = TypeVar("T")


@overload
def reduce(function: Callable[[T, T], T]) -> Callable[[Iterable[T]], T]: ...


@overload
def reduce(function: Callable[[T, T], T], sequence: [Iterable[T]]) -> T: ...


def reduce(function, sequence=None):
    if sequence is None:
        return functools.partial(functools.reduce, function)
    return functools.reduce(function, sequence)


@overload
def map(function: Callable) -> Callable: ...


@overload
def map(function: Callable, sequence: Sequence): ...


def map(function, sequence=None):
    if sequence is None:
        return functools.partial(map, function)
    return map(function, sequence)


class sequence(Callable):
    def __init__(self, *funcs: Callable):
        super().__init__()
        self.funcs = funcs

    def __call__(self, val):
        reduce(lambda fn1, fn2: fn2(fn1(val)),
               self.funcs)
