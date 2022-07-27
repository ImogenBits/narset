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






def tokenize(text: str) -> list[list[Token]]:
    out: list[list[Token]] = []
    for line in text.splitlines():
        line_out = []
        out.append(line_out)
        for word in nltk.word_tokenize(line):
            if word.isdigit():
                line_out.append(Num(int(word)))
            elif word in Sym.symbols:
                line_out.append(Sym(word))
            else:
                line_out.append(Word(word))
    return out
