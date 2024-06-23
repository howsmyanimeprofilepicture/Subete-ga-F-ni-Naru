# from ._filter import _filter as filter
# from ._find import _find as find
from typing import overload, Callable, Iterable, TypeVar, Union
from ._curry import curry

T = TypeVar("T")


@overload
def find(condition: Callable[[T], bool], seq: Iterable[T]) -> Iterable[T]:
    """

    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> F.find(lambda x: x>2, [1,2,3,4,5,])
    3
    ```

    `find` is a currying function, so you can also use it as follows:

    ```python
    >>> import subete_ga_F_ni_naru as F
    >>> greater_than_2 = F.filter(lambda x: x>2)
    >>> greater_than_2([1,2,3,4,5,])
    3
    ```
    """


@overload
def find(condition: Callable[[T], bool]) -> Callable[[Iterable[T]], Iterable[T]]: ...


@curry(2)
def _find(condition: Callable[[T], bool], seq: Iterable[T]) -> Union[T, None]:

    for s in seq:
        if condition(s):
            return s
    return None


find = _find
