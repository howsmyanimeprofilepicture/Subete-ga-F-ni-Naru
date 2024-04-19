from typing import overload, Callable, Iterable, TypeVar, Union
from ._curry import curry

T = TypeVar("T")


@overload
def filter(condition: Callable[[T], bool], seq: Iterable[T]) -> Iterable[T]:
    """

    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> res = F.filter(lambda x: x>2, [1,2,3,4,5,])
    >>> [*res]
    [3, 4, 5]
    ```

    `filter` is a currying function, so you can also use it as follows:

    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> greater_than_2 = F.filter(lambda x: x>2)
    >>> res = greater_than_2([1,2,3,4,5,])
    >>> [*res]
    [3, 4, 5]
    ```
    """


@overload
def filter(condition: Callable[[T], bool]) -> Callable[[Iterable[T]], Iterable[T]]: ...


@curry(2)
def _filter(condition: Callable[[T], bool], seq: Iterable[T]) -> Iterable[T]:

    for s in seq:
        if condition(s):
            yield s
    return


filter = _filter
