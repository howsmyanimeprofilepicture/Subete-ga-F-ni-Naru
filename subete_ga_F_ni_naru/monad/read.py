import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Any, Tuple
from .monad import Monad

R = TypeVar("R")
V = TypeVar("V")
V2 = TypeVar("V2")


class Reader(Monad, Generic[R, V]):
    val: Callable[[R], V]

    def __init__(self, read_func: Callable[[R], V]) -> None:
        super().__init__(val=read_func, meta=None)

    def map(self: "Reader[R, V]", func: Callable[[V], V2]) -> "Reader[R, V2]":
        def new_read_func(r: R) -> V2:
            return func(self.val(r))
        return Reader(new_read_func)

    def bind(self: "Reader[R, V]", func: Callable[[V], "Reader[R,V2]"]
             ) -> "Reader[R, V2]":
        def new_read_func(r: R) -> V2:
            return func(self.val(r)).val(r)

        return Reader(new_read_func)
