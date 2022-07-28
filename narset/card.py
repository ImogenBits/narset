from __future__ import annotations
from dataclasses import dataclass

from narset.cost import ManaCost

@dataclass
class Card:
    name: str
    mana_cost: ManaCost
    
