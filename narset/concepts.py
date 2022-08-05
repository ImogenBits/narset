from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from ability import Ability

mana_colors: dict[str, str] = {
    "W": "white",
    "U": "blue",
    "B": "black",
    "R": "red",
    "G": "green"
}

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

    def __str__(self) -> str:
        out = ""
        if self.variables is not None:
            out += self.variables
        if self.generic != 0:
            out += str(self.generic)
        for sym, color in mana_colors.items():
            out += sym * getattr(self, color)
        return out

@dataclass
class Cost:
    mana: Mana | None = None
    life: int | None = None
    actions: list[Action] = field(default_factory=list)

    def __str__(self) -> str:
        out = []
        if self.mana is not None:
            out.append(str(self.mana))
        if self.life is not None:
            out.append(f"{self.life} life")
        out += [str(a) for a in self.actions]
        return ", ".join(out)

class Action:
    pass

@dataclass
class TypeLine:
    supertypes: list[SuperType]
    types: list[CardType]
    subtypes: list[SubTypes]


class SuperType:
    pass

class CardType:
    pass

class SubTypes:
    pass


@dataclass
class Card:
    name: str
    mana_cost: Cost
    typeline: str
    abilities: list[Ability]
    power: int
    toughness: int
    text: str
    unparsed_text: str

    def __str__(self) -> str:
        return f"name: {self.name}\nmana cost: {self.mana_cost}\ntypes: {self.typeline}\nabilities: {self.abilities}\npower/toughness: {self.power}/{self.toughness}\ntext: {self.text}\nunparsed text: {self.unparsed_text}"

