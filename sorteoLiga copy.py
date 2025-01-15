def obtenerEquipos():
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
    return list(equipos.keys())  

def generarJornada(equipos, jornadaAnteriorLocales):
    jornada = []  
    mitad = len(equipos) // 2  

    for i in range(mitad):
        local = equipos[i]  
        visitante = equipos[-i-1]  

        if local in jornadaAnteriorLocales:
            local, visitante = visitante, local

        jornada.append((local, visitante))  

    return jornada

def generarJornadasIda(equipos):
    nombresEquipos = equipos[:]  
    jornadasIda = []  
    jornadaAnteriorLocales = []  

    for _ in range(len(nombresEquipos) - 1):  # Generamos una jornada por cada iteración
        jornada = generarJornada(nombresEquipos, jornadaAnteriorLocales)
        jornadasIda.append(jornada)  

        # Actualizamos los equipos que fueron locales en esta jornada
        jornadaAnteriorLocales = [partido[0] for partido in jornada]

        # Rotamos los equipos para evitar que jueguen siempre contra los mismos
        nombresEquipos.insert(1, nombresEquipos.pop())  # Mueve el último equipo al segundo puesto

    return jornadasIda

def generarJornadasVuelta(jornadasIda):
    jornadasVuelta = []
    for jornada in jornadasIda:
        jornadaVuelta = [(visitante, local) for local, visitante in jornada]
        jornadasVuelta.append(jornadaVuelta)

    return jornadasVuelta

def mostrarJornadas(jornadas):
    jornada_numero = 1
    for jornada in jornadas:
        print(f"Jornada {jornada_numero}:")
        for local, visitante in jornada:
            print(f"{local} vs {visitante}")
        print()
        jornada_numero += 1

def main():
    # Entrada
    equipos = obtenerEquipos()

    # Procesamiento
    jornadasIda = generarJornadasIda(equipos)
    jornadasVuelta = generarJornadasVuelta(jornadasIda)

    # Salida
    print("Calendario de la Liga:")
    mostrarJornadas(jornadasIda + jornadasVuelta)  

if __name__ == "__main__":
    main()