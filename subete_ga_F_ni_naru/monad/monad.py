import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Any, Tuple

T = TypeVar("T")
U = TypeVar("U")


class Monad(ABC, Generic[T]):
    def __init__(self, val: T, meta: Any) -> None:
        super().__init__()
        self.val = val
        self.meta = meta

    @abstractmethod
    def map(self, func: Callable) -> "Monad":
        ...

    @abstractmethod
    def bind(self, func: Callable) -> "Monad":
        ...

    def __lshift__(self: "Monad[T]", func: Callable[[T], U]) -> "Monad[U]":
        return self.map(func)

    def __eq__(self, other: "Monad") -> bool:
        return self.val == other.val

    def __ne__(self, other: "Monad") -> bool:
        return self.val != other.val

    def __repr__(self) -> str:
        return f"{self.__name__}(val={self.val}, meta={self.meta})"


class Just(Monad, Generic[T]):
    def __init__(self, val: T) -> None:
        super().__init__(val, None)

    def map(self: Monad, func: Callable[[T], U]) -> Monad[U]:
        return Just(func(self.val), None)

    def bind(self: Monad, func: Callable[[T], Monad[U]]) -> Monad[U]:
        return func(self.val)


class Nothing(Monad):
    def __init__(self) -> None:
        super().__init__(None, None)

    def map(self: Monad, func: Callable[[T], U]) -> Monad[T]:
        return self

    def bind(self: Monad, func: Callable[[T], Monad[U]]) -> Monad[T]:
        return self
