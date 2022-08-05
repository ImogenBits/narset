from __future__ import annotations
import json
from parser import parse_card


if __name__ == "__main__":
    with open("data/sample_cards.json") as f:
        cards_json = json.load(f)
    cards = [parse_card(c) for c in cards_json]
    for card in cards:
        print(f"{card}\n")
