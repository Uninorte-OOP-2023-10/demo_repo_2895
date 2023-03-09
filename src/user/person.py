class Person:

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'{self.nombre}, '
            f'{self.edad}'
            f')'
        )


class Friend(Person):

    def __init__(self, nombre: str, edad: int, telefono: int) -> None:
        super().__init__(nombre, edad)
        self.telefono = telefono
