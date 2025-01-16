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
   jornadasIda = [] 
   jornadaAnteriorLocales = [] 

   for _ in range(len(equipos) - 1):
       jornada = generarJornada(equipos, jornadaAnteriorLocales)
       jornadasIda.append(jornada) 

       jornadaAnteriorLocales = [partido[0] for partido in jornada]

       equipos.insert(1, equipos.pop())  

   return jornadasIda

def generarJornadasVuelta(jornadasIda):
   jornadasVuelta = []
   for jornada in jornadasIda:
       jornadaVuelta = [(visitante, local) for local, visitante in jornada]
       jornadasVuelta.append(jornadaVuelta)

   return jornadasVuelta

def mostrarJornadas(jornadas):
   numeroJornada = 1
   for jornada in jornadas:
       print(f"Jornada {numeroJornada}:")
       for local, visitante in jornada:
           print(f"{local} vs {visitante}")
       print()
       numeroJornada += 1

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