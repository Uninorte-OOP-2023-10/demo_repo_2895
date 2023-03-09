#from user.person import *

from prueba.prueba import Test

"""
def main():
    nombre = input('Digite su nombre: ')
    edad = int(input('Digite su edad: '))
    person1 = Person(nombre, edad)
    print(person1)

    nombre = input('Digite el nombre: ')
    edad = int(input('Digite la edad: '))
    telefono = int(input('Digite el telefono: '))
    friend1 = Friend(nombre, edad, telefono)
    print(friend1)
"""

def main():
    nombre = input('Digite su nombre: ')
    edad = int(input('Digite su edad: '))
    test1 = Test(nombre, edad)

    print(test1.person)
    

if __name__ == '__main__':
    main()