from typing import Iterable, Callable, TypeVar
from ._curry import curry
T = TypeVar("T")


@curry(2)
def _filter(condition: Callable[[T], bool], seq: Iterable[T]) -> Iterable[T]:
    for s in seq:
        if condition(s):
            yield s
    return
