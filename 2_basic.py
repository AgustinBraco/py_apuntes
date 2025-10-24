# Convenciones
UpperCamelCase = "Clases"
UPPER_SNAKE_CASE = "Constantes"
lower_snake_case = "Resto"

# Tipos de datos
entero: int = 10  ## Número entero
decimal: float = 10.1  ## Número decimal
texto: str = "10"  ## Cadena de texto
lista: list = [1, 2]  ## Lista ordenada y modificable
tupla: tuple = (1, 2)  ## Colección ordenada e inmutable
conjunto: set = {1, 2, 3}  ## Colección desordenada sin elementos repetidos
diccionario: dict = {1: 1}  ## Pares clave:valor
booleano: bool = True  ## Verdadero o falso
nulo: None = None  ## Nulo o sin valor

# Info / Help
actions = dir(int)  # -> ['__add__',...]
print(actions)


# Funciones
## Argumentos - Parametros
def foo(arguments: str) -> str:
    print(arguments)
    return arguments


foo("parameters")  # -> parameters


## Condicional ternario
def is_adult(age):
    return False if age < 18 else True


def sex(value):
    return "Male" if value == "M" else "Female"


## Valores por defecto
def default1(a=1, b=2):
    print(a, b)
    return a, b


def default2(a, b, c=2):
    print(a, b, c)
    return a, b, c


default1()  # -> 1, 2
default1(3, 4)  # -> 3, 4
default2(1, 2, 3)  # -> 1, 2, 3
default2(1, 2)  # -> 1, 2, 2
default2(1, 2, c=5)  # -> 1, 2, 5


## Multiples argumentos
def arguments1(*args, **kwargs):
    print(args, kwargs)
    return args, kwargs


def arguments2(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
    return a, b, args, kwargs


arguments1(1, a=1)  # -> (1) {'a': 1}
arguments1(1, 2, a=3)  # -> (1, 2) {'a': 3}
arguments1(1, 2, 3, 4, a=5, b=6)  # -> (1, 2, 3, 4) {'a': 5, 'b': 6}

arguments2(1, 2, 3, 3, 3, method="POST")  # -> 1, 2 (3, 3, 3) {'method': 'POST'}
arguments2(0, 0, 10, 100, 2, rol="user")  # -> 0, 0 (10, 100, 2) {'rol': 'user'}

## Llamadas
from typing import Callable


def foo1(text: str) -> str:
    print(text)
    return text


def foo2(foo1: Callable) -> str:
    print("Foo2")
    foo1("Foo1")
    return "Foo2"


foo2(foo1)  # -> Foo2 Foo1

# Desempaquetado
x, y, z = (1, 200, 2.2)
print(x, y, z)  # -> 1 200 2.2

names = ["Juan", "Jose"]
name1, name2 = names
print(name1, name2)  # -> Juan Jose

user = {"first_name": "Juan", "last_name": "Perez"}
first_name = user["first_name"]
last_name = user["last_name"]
print(first_name, last_name)  # -> Juan Perez

# Try - Except
validations = {"is_adult": is_adult, "sex": sex}

try:
    result = validations["is_before"](1761193193)
    print(result)
except KeyError:
    print("No existe la validación")  # -> No existe la validación

# Archivos
## Abrir y cerrar
with open("./files/file.csv", "r") as csv:
    for row in csv:
        print(row.strip())  # -> name,age Juan,20 Jose,12

# Abrir
csv = open("./files/file.csv", "r")

for row in csv:
    print(row.strip())  # -> name,age Juan,20 Jose,12

# Cerrar
csv.close()
