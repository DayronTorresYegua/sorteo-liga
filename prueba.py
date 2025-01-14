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

    return equipos

def generar_jornada(equipos, jornada_anterior_locales):
    
    mitad_lista = len(equipos) // 2
    partidos_jornada = []

    for i in range(mitad_lista):
        equipo_local = equipos[i]
        equipo_visitante = equipos[-i - 1]

        if equipo_visitante in jornada_anterior_locales:
            equipo_local, equipo_visitante = equipo_visitante, equipo_local

        partidos_jornada.append((equipo_local, equipo_visitante))

    return partidos_jornada


def generar_jornadas_ida(equipos):
 
    nombres_equipos = list(equipos)  
    jornadas_ida = [] 
    jornada_anterior_locales = []  
    for _ in range(len(nombres_equipos) - 1):  
        jornada = generar_jornada(nombres_equipos, jornada_anterior_locales)
        jornadas_ida.append(jornada)  

        jornada_anterior_locales = [partido[0] for partido in jornada]  

        nombres_equipos.insert(1, nombres_equipos.pop()) 

    return jornadas_ida  


def generar_jornadas_vuelta(jornadas_ida):
   
    jornadas_vuelta = []
    for jornada in jornadas_ida:
        jornada_vuelta = [(visitante, local) for local, visitante in jornada]
        jornadas_vuelta.append(jornada_vuelta)

    return jornadas_vuelta


def mostrar_jornadas(jornadas):

    for i, jornada in enumerate(jornadas, 1):
        print(f"Jornada {i}:")
        for local, visitante in jornada:
            print(f"{local} vs {visitante}")
        print()

def main():
    # Entrada
    equipos = obtenerEquipos()

    # Procesamiento
    jornadas_ida = generar_jornadas_ida(equipos)

    jornadas_vuelta = generar_jornadas_vuelta(jornadas_ida)

    # Salida
    print("Jornadas de Ida:")
    mostrar_jornadas(jornadas_ida)

    print("Jornadas de Vuelta:")
    mostrar_jornadas(jornadas_vuelta)


# Ejecutar el programa
if __name__ == "__main__":
    main()
