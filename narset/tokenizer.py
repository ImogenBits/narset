from __future__ import annotations
import nltk

class Token:
    pass

class Word(Token):
    def __init__(self, s: str) -> None:
        if len(s) != 1:
            raise ValueError
        super().__init__()
        self.s = s


class Num(Token):
    def __init__(self, num: int) -> None:
        super().__init__()
        self.num = num


class Sym(Token):
    symbols = {".", ",", "-", "—"}

    def __init__(self, sym) -> None:
        super().__init__()
        self.sym = sym

EM = Sym("—")


class Mana(Token):
    def __init__(self, entry: str) -> None:
        super().__init__()
        self.entry = entry



def tokenize(text: str) -> list[list[Token]]:
    out: list[list[Token]] = []
    for line in text.splitlines():
        line_out = []
        out.append(line_out)
        try:
            words = iter(nltk.word_tokenize(line))
            while True:
                word = next(words)
                if word.isdigit():
                    line_out.append(Num(int(word)))
                elif word in Sym.symbols:
                    line_out.append(Sym(word))
                elif word == "{":
                    line_out.append(Mana(next(words)))
                    next(words)
                else:
                    line_out.append(Word(word))
        except StopIteration:
            pass
    return out
