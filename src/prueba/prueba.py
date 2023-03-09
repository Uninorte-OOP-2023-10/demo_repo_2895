import random as rnd

#from __future__ import annotations
from user.person import Person

class Test:

    def __init__(self, nombre: str, edad: int) -> None:
        self.id = rnd.randint(0, 9)
        self.person = Person(nombre, edad)
