from __future__ import annotations
from tokenizer import tokenize
import tokenizer
from concepts import Mana, Card, Cost

def parse_mana(mana_str: str) -> Mana:
    tokens = tokenize(mana_str)
    if len(tokens) != 1:
        raise RuntimeError
    mana: Mana = Mana()
    for t in tokens[0]:
        if not isinstance(t, tokenizer.Mana):
            continue
        match t.entry:
            case "W":
                mana.white += 1
            case "U":
                mana.blue += 1
            case "B":
                mana.black += 1
            case "R":
                mana.red += 1
            case "G":
                mana.green += 1
            case "X":
                mana.variables = "X"
            case _:
                mana.generic += int(t.entry)
    return mana

def parse_power(pow_str: str) -> int:
    if pow_str.isdigit():
        return int(pow_str)
    else:
        return 0


def parse_card(card_json: dict) -> Card:
    name = card_json["name"]
    mana_cost = Cost(mana = parse_mana(card_json["mana_cost"]))
    typeline = card_json["type_line"]
    abilities = []
    power = parse_power(card_json["power"]) if "power" in card_json else 0
    toughness = parse_power(card_json["toughness"]) if "toughness" in card_json else 0
    text = card_json["oracle_text"]
    unparsed_text = text

    return Card(name, mana_cost, typeline, abilities, power, toughness, text, unparsed_text)

