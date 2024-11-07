from busquedaAlum3 import *

objetivo = busquedaAnchura()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

#objetivo = busquedaProfundidad()
#if objetivo:
#    print("Se ha alcanzado una solución")
#else:
#    print("No se ha alcanzado ninguna solución")

#PARECE QUE NO SE ENCUENTRA SOLUCIÓN EN LA BÚSQUEDA EN PROFUNDIDAD,
#AUNQUE LO QUE OCURRE REALMENTE ES QUE SE ESTARÁN GENERANDO CICLOS
#QUE GENERAN BUCLES INFINITOS Y QUE, POR TANTO, NO HAYA PROGRESO

objetivo = busquedaAnchuraNoRepetidos()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaProfundidadNoRepetidos()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

