def generarJornada(equipos):

    nombresEquipos = list(equipos.keys())
    numeroEquipos = len(nombresEquipos)

    mitad = len(nombresEquipos) //2

    partidos = []

    for i in range(mitad):
        local = nombresEquipos[i]
        visitante = nombresEquipos[- i - 1]
        partidos.append((local, visitante))

    return partidos

def mostrarJornada(jornada):
    for local, visitante in jornada:
        print(f"{local} vs {visitante}")

def main():
    # Entrada
    equipos = {
        "Real Betis": "Sevilla",
        "Sevilla FC": "Sevilla",
        "Real Madrid": "Madrid",
        "Atlético de Madrid": "Madrid",
        "FC Barcelona": "Barcelona",
        "Espanyol": "Barcelona",
        "Valencia CF": "Valencia",
        "Villarreal CF": "Villarreal",
        "Athletic Club": "Bilbao",
        "Real Sociedad": "San Sebastián",
        "Celta de Vigo": "Vigo",
        "Real Valladolid": "Valladolid",
        "Osasuna": "Pamplona",
        "Real Zaragoza": "Zaragoza",
        "Getafe CF": "Getafe",
        "Rayo Vallecano": "Madrid",
        "Deportivo Alavés": "Vitoria-Gasteiz",
        "Real Mallorca": "Palma de Mallorca",
        "Girona FC": "Girona",
        "UD Las Palmas": "Las Palmas",
    }

    # Procesamiento
    jornada = generarJornada(equipos)

    # Salida

    mostrarJornada(jornada)
if __name__ == "__main__":
    main()
