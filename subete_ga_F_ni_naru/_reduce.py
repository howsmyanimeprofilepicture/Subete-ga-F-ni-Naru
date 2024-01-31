from typing import overload, TypeVar, Callable, Iterable
import functools

T = TypeVar("T")


@overload
def reduce(function: Callable[[T, T], T]) -> Callable[[Iterable[T]], T]: ...


@overload
def reduce(function: Callable[[T, T], T], sequence: [Iterable[T]]) -> T: ...


def reduce(function, sequence=None):
    if sequence is None:
        return functools.partial(functools.reduce, function)
    return functools.reduce(function, sequence)
