import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar, Any, Tuple
from .monad import Monad

S = TypeVar("S")
V = TypeVar("V")
V2 = TypeVar("V2")


class State(Monad, Generic[S, V]):
    val: Callable[[S], Tuple[V, S]]

    def __init__(self, state_func: Callable[[S], Tuple[V, S]]) -> None:
        super().__init__(val=state_func, meta=None)

    def run(self, input_state: S) -> Tuple[V, S]:
        return self.val(input_state)

    def map(self: "State[S, V]", func: Callable[[V], V2]) -> "State[S, V2]":
        def new_state_func(state: S) -> Tuple[V2, S]:
            val, new_state = self.run(state)
            return func(val), new_state
        return State(new_state_func)

    def bind(self: "State[S, V]", func: Callable[[V], "State[S,V2]"]) -> "State[S, V2]":
        def new_state_func(state: S) -> Tuple[V2, S]:
            val, new_state = self.run(state)
            return func(val).run(new_state)

        return State(new_state_func)
