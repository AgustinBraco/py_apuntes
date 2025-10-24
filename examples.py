# Try - Except
teams = {"River": "Monumental", "Boca": "Bombonera"}

try:
    stadium = teams["San Lorenzo"]
    print(stadium)
except KeyError: # ValueError para inputs
    print("The team doesn't exist")  # 1 -> The team doesn't exist


# Funciones y llamadas
def get_stadium(team_name: str) -> str:
    return teams.get(team_name, "unknown")


def show_team_info(team_name: str):
    stadium = get_stadium(team_name)
    (
        print("No team info.")  # 3 -> No team info.
        if stadium == "unknown"
        else print(f"{team_name} plays at {stadium}")  # 2 -> River plays at Monumental
    )
    return (
        "No team info." if stadium == "unknown" else f"{team_name} plays at {stadium}"
    )


show_team_info("River")  # -> River plays at Monumental
show_team_info("Racing")  # -> Racing plays at Unknown

# Desempaquetado
team_info = ("River", "Monumental", 1901)
name, stadium, founded = team_info
print(
    f"{name} was founded in {founded} and plays at {stadium}."
)  # 4 -> River was founded in 1901 and plays at Monumental.

# Bucle + lógica básica
teams_info = [
    ("River", "Monumental", 1901),
    ("Boca", "Bombonera", 1903),
    ("Huracán", "Ducó", 1927),
]

for name, stadium, founded in teams_info:
    print(
        f"{name} was founded in {founded} and plays at {stadium}."
    )  # 5 -> River was founded in ...


# Funciones - Diccionarios - Lista de tuplas - Bucle - Desempaquetado - Try
## Funciones
def is_adult(age):
    return False if age < 18 else True


def sex(value):
    return "Male" if value == "M" else "Female"


## Diccionario
validations = {"is_adult": is_adult, "sex": sex}

## Lista
items = [
    ## Tuplas
    ("is_adult", 85),
    ("is_adult", 2),
    ("sex", "F"),
    ("sex", "M"),
    ("is_bigger", 1761193193),
]

## Bucle
for item in items:
    ## Desempaquetado
    validation, value = item

    # Try
    try:
        ## Funcion en diccionario
        result = validations[validation](value)
        print(result)  # -> True False Female Male
    except KeyError:
        print(f"No existe la validación {validation}")  # -> No existe la validación
