from __future__ import annotations

from narset.cost import Cost
from narset.parser import Lit, Num

KWArgs = Cost | Num | Lit

keywords = {
    "vigilance": [],
    "flying": [],
    "ward": [Cost],
}
