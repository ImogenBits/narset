from __future__ import annotations

class Ability:
    pass

class Static(Ability):
    pass

class Spell(Ability):
    pass

class Triggered(Ability):
    pass

class Activated(Ability):
    pass

class Keyword(Ability):
    def __init__(self, text: str) -> None:
        super().__init__()
        
