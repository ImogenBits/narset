from __future__ import annotations
from typing import Iterable

class Token:
    pass

class Lit(Token):
    def __init__(self, s: str) -> None:
        if len(s) != 1:
            raise ValueError
        super().__init__()
        self.s = s
    
    def tokens(self, s: str) -> Iterable[Lit]:
        for c in s:
            yield Lit(c)

class Num(Token):
    def __init__(self, num: int) -> None:
        super().__init__()
        self.num = num
