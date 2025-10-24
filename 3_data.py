# Identificar tipos de datos
## type(string) -> muestra el tipo

## "" -> cadena -> str
## 0 -> entero -> int
## 0.0 -> decimal -> float
## {clave:valor} -> diccionario -> dict
## {clave, clave} -> conjunto -> set
## [] -> lista -> list
## (item) -> tupla -> tuple

# Resumen por tipo de dato
## str:
## Acceso por índice: name[0]
## Métodos: upper(), replace()
## Concatenar: "Hola "+name

## int:
## Operaciones matemáticas: 'a + 5', 'a * 2'

## float:
## Operaciones matemáticas: 'x / 2', 'x * 3'

## dict:
## Acceso: item["property"]
## Agregar/Actualizar: item["property"]="new_value"
## Eliminar: del() o pop()
## Iterar: for key, value in dict.items()

## set:
## Agregar: add()
## Eliminar: remove()
## Comprobar: 3 in numbers
## Operaciones: union(), intersection()

## list:
## Acceso: numbers[0]
## Agregar: append()
## Eliminar: remove()
## Ordenar: sort()
## Iterar con for

## tuple:
## Acceso: point[0]
## Iterar con for
## Inmutable (no se puede modificar)


# Ejercicios nivel inicial:
## Dado un diccionario {team: founded_year}, obtener el equipo más antiguo.
teams_founded = {
    "River Plate": 1901,
    "Boca Juniors": 1905,
    "Racing Club": 1903,
    "Independiente": 1905,
    "San Lorenzo": 1908,
    "Huracán": 1908,
}

oldest_team = min(teams_founded, key=teams_founded.get)  # type: ignore
print(f"The oldest team is {oldest_team}, founded in {teams_founded[oldest_team]}.")


## Dada una lista de tuplas (team, goals), encontrar el máximo y mínimo.
team_goals = [
    ("River Plate", 58),
    ("Boca Juniors", 52),
    ("Racing Club", 49),
    ("Independiente", 40),
    ("San Lorenzo", 46),
    ("Huracán", 35),
]

max_goals_team = max(team_goals, key=lambda item: item[1])
min_goals_team = min(team_goals, key=lambda item: item[1])

print(f"{max_goals_team} is max. {min_goals_team} is min.")

## Dada una lista de nombres, eliminar duplicados sin usar set().
team_names = [
    "River Plate",
    "Boca Juniors",
    "Racing Club",
    "River Plate",
    "San Lorenzo",
    "Boca Juniors",
    "Huracán",
    "Racing Club",
]

unique_team_names = []

for team in team_names:
    if team not in unique_team_names:
        unique_team_names.append(team)

print(unique_team_names)

## Crear una función que reciba una lista de equipos y devuelva solo los que tengan más de 100 años.
teams_years = [
    ("River Plate", 1901),
    ("Boca Juniors", 1905),
    ("Racing Club", 1903),
    ("Defensa y Justicia", 1935),
    ("Tigre", 1902),
    ("Arsenal", 1957),
]

from datetime import date


def older_than_100(teams_list: list) -> list:
    teams_older = []
    for team, founded in teams_list:
        current_year = date.today().year
        team_years = current_year
        # founded
        # team_years = current_year - founded ???
        if team_years > 100:
            teams_older.append((team, founded))

    return teams_older

    # current_year = date.today().year
    # return [(team, founded) for team, founded in teams_list if current_year
    ## founded > 100]


print(older_than_100(teams_years))


## Crear un diccionario que agrupe equipos por ciudad.
teams_cities = {
    "River Plate": "Buenos Aires",
    "Boca Juniors": "Buenos Aires",
    "Racing Club": "Avellaneda",
    "Independiente": "Avellaneda",
    "San Lorenzo": "Buenos Aires",
    "Rosario Central": "Rosario",
    "Newell's Old Boys": "Rosario",
    "Talleres": "Córdoba",
    "Belgrano": "Córdoba",
}

cities_dict = {}

for team, city in teams_cities.items():
    if city not in cities_dict:
        cities_dict[city] = []
    cities_dict[city].append(team)

print(cities_dict)

# Ejercicios nivel medio:
