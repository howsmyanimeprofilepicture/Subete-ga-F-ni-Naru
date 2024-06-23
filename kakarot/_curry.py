from typing import overload, TypeVar, Callable, Iterable, Any,  Union
import functools

T = TypeVar("T")
U = TypeVar("U")


class CurryFunc:
    def __init__(self, func: Callable[[Any], T], num_args: int) -> None:
        self._func = func
        self.num_args = num_args

    def __call__(self, *args, **kwds) -> Union[Callable, T]:
        current_num_args = len(args) + len(kwds)
        if current_num_args < self.num_args:

            return CurryFunc(
                func=functools.partial(self._func, *args, **kwds),
                num_args=self.num_args-current_num_args
            )
        else:
            return self._func(*args, **kwds)


def curry(num_args: int) -> Callable[[Callable], CurryFunc]:
    """
    creates the currying function.

    Examples:
    ```python
    >>> import kakarot
    >>>  @kakarot.curry(num_args=3)
    ... def maru(x, y, z):
    ...     return x * y + z
    >>> maru(y=2)(1, 3)   # equivalent to maru(1, 3, y=2)
    TypeError: maru() got multiple values for argument 'y'
    >>> maru(y=2)(x=1, z=3) # equivalent to maru(y=2, x=1, z=3)
    5
    >>> maru(1)(2)(1) # equivalent to maru(1, 2, 1)
    3
    >>> maru(1, 2)(y=1) # equivalent to maru(1, 2, y=1)
    TypeError: maru() got multiple values for argument 'y'
    ```

    """
    return (lambda func: CurryFunc(func, num_args))
