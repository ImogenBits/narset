from __future__ import annotations
from abc import ABC
from typing import Iterable

class Cost(ABC):
    def __add__(self, other: Cost) -> CombinedCost:
        return CombinedCost([self, other])


class CombinedCost(Cost):
    def __init__(self, costs: Iterable[Cost] | None = None) -> None:
        super().__init__()
        self.costs: set[BaseCost] = set()
        if costs is None:
            return
        else:    
            for c in costs:
                self.add(c)
    
    def add(self, other: Cost):
        if isinstance(other, CombinedCost):
            self.costs |= other.costs
        elif isinstance(other, BaseCost):
            self.costs.add(other)
        else:
            raise TypeError

    def __iadd__(self, other: Cost) -> CombinedCost:
        self.add(other)
        return self


class BaseCost(Cost, ABC):
    pass


class ManaCost(BaseCost):
    def __init__(self, ) -> None:
        super().__init__()
