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

    def map(self: "Just", func: Callable[[T], U]) -> "Just[U]":
        return Just(func(self.val), None)

    def bind(self: "Just", func: Callable[[T], "Just[U]"]) -> "Just[U]":
        return func(self.val)


class Writer(Monad, Generic[T]):
    def __init__(self, val: T, meta: Any) -> None:
        super().__init__(val, meta)

    def map(self: "Writer[T]", func: Callable[[T], U]) -> "Writer[U]":
        return Writer(func(self.val), self.meta)

    def bind(self: "Writer[T]", func: Callable[[T], "Writer[U]"]) -> "Writer[U]":
        new_writer: Writer[U] = func(self.val)
        return Writer(new_writer.val, self.meta + new_writer.meta)


class Nothing(Monad):
    def __init__(self) -> None:
        super().__init__(None, None)

    def map(self: "Nothing", func: Callable[[T], U]) -> "Nothing":
        return self

    def bind(self: "Nothing", func: Callable[[T], Monad[U]]) -> "Nothing":
        return self


class Left(Monad):
    def __init__(self, meta: Any) -> None:
        super().__init__(val=None, meta=meta)

    def map(self, func):
        return self

    def bind(self, func):
        return self


class Right(Monad, Generic[T]):
    def __init__(self, val: T) -> None:
        super().__init__(val, None)

    def map(self: "Right", func: Callable[[T], U]) -> "Right[U]":
        return Right(func(self.val))

    def bind(self: "Right", func: Callable[[T], "Right[U]"]) -> "Right[U]":
        return func(self.val)
