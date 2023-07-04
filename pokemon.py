pokemons = [
    ["Nombre", "altura", "peso", "tipo", "debilidad", "evolucion"],
    ["Bulbasaur", 0.7, 6.9, "planta", "fuego", "Ivysaur"],
    ["Ivysaur", 1.0, 13.0, "planta", "fuego", "Venusaur"],
]

with open("pokemons.csv", "w") as archivo:
    for pokemon in pokemons:
        archivo.write(",".join(str(x) for x in pokemon) + "\n")


def buscar_pokemon(nombre="Invalido", tipo="Invalido", archivo="pokemons.csv"):
    pokemons = []
    found = []
    with open(archivo, "r") as archivo2:
        for linea in archivo2:
            linea = linea.strip().split(",")
            pokemons.append(linea)
    for pokemon in pokemons:
        if nombre == pokemon[0]:
            found.append(pokemon)
        if tipo == pokemon[3]:
            found.append(pokemon)

    if found:
        return print(found)
    else:
        return print("No se encontro el pokemon")


buscar_pokemon(tipo="planta")
