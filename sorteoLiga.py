diccionarioEquipos = {
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

def generarCalendario(diccionarioEquipos):
    jornadas = []
    nombresEquipos = list(diccionarioEquipos.keys())
    numeroEquipos = len(nombresEquipos)

    numeroJornadas = len(nombresEquipos) -1
    mitad = len(nombresEquipos) // 2

    for jornada in range(numeroJornadas):
        partidos = []
        for i in range(mitad):
            local = nombresEquipos[i]
            visitante = nombresEquipos[-i - 1]

            if jornada % 2 == 0:
                partidos.append((local,visitante))
            else:
                partidos.append((visitante,local))

        jornadas.append(partidos)
        


def main():
    # Entrada

    # Procesamiento

    # Salida
if __name__ == "__main__":
    main()