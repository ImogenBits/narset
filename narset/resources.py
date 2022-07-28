from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

@dataclass
class Mana:
    generic: int = 0
    white: int = 0
    blue: int = 0
    black: int = 0
    red: int = 0
    green: int = 0
    colorless: int = 0
    variables: Literal["X"] | None = None

