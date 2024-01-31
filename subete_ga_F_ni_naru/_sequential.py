from typing import Callable
import functools


class Sequential(Callable):
    """implements a [composite function](https://en.wikipedia.org/wiki/Function_composition).

    .. math::

        g \odot f \odot h (x) = g(f(h(x)))


    Args:
        *funcs (Callable): the functions to be composed.


    Examples:

    ```py
    >>> import subete_ga_F_ni_naru as F
    >>> f = F.Sequential(
    ...     F.map(lambda x: x*2),
    ...     F.map(lambda x: x-1)
    ... )
    >>> [*f(range(5))]
    [-1, 1, 3, 5, 7]
    ```


    """

    def __init__(self, *funcs: Callable):
        super().__init__()
        self._funcs = funcs

    def __call__(self, val):
        return functools.reduce(lambda fn1, fn2: fn2(fn1(val)), self._funcs)
