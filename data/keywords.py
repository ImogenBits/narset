from __future__ import annotations

from narset.cost import Cost
from narset.tokenizer import Word, Num

KWArgs = Cost | Num | Word

keywords = {
    "vigilance": [],
    "flying": [],
    "ward": [Cost],
}
