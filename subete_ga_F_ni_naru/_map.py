from typing import overload, TypeVar, Callable, Iterable, Union
import functools


T = TypeVar("T")
U = TypeVar("U")


@overload
def _map(function: Callable[[T], U]) -> Callable[[Iterable[T]], Iterable[U]]:
    """
    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> [*F.map(lambda x: x>2, [1,2,3,4,5,])]
    [False, False, True, True, True]
    >>> [*F.map(lambda x: x>2)([1,2,3,4,5,])]
    [False, False, True, True, True]
    ```
    """


@overload
def _map(function: Callable[[T], U], sequence: Iterable[T]) -> Iterable[U]: ...


def _map(function, sequence=None):
    if sequence is None:
        return functools.partial(map, function)
    return map(function, sequence)
