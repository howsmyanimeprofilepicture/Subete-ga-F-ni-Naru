from typing import overload, TypeVar, Callable, Iterable, Union
import functools


T = TypeVar("T")
U = TypeVar("U")


@overload
def _map(function: Callable[[T], U]) -> Callable[[Iterable[T]],
                                                 Iterable[U]]: ...


@overload
def _map(function: Callable[[T], U], sequence: Iterable[T]) -> Iterable[U]: ...


def _map(function, sequence=None):
    if sequence is None:
        return functools.partial(map, function)
    return map(function, sequence)
