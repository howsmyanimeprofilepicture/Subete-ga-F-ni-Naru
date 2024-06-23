from typing import overload, TypeVar, Callable, Iterable, Any,  Union
import functools

T = TypeVar("T")
U = TypeVar("U")


class CurryFunc(Callable):
    def __init__(self, func: Callable[[Any], T], num_args: int) -> None:
        self._func = func
        self.num_args = num_args

    def __call__(self, *args, **kwds) -> Union[Callable, T]:
        return (functools.partial(self._func, *args, **kwds)
                if len(args) + len(kwds) < self.num_args else
                self._func(*args, **kwds))


def curry(num_args: int) -> Callable[[Callable], CurryFunc]:
    return (lambda func: CurryFunc(func, num_args))
