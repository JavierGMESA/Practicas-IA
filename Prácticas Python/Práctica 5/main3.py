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

objetivo = busquedaAnchuraNoRepetidos1()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaAnchuraNoRepetidos2()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaProfundidadNoRepetidos1()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaProfundidadNoRepetidos2()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

#HAY UNA MEJORA MUY CONSIDERABLE SOBRE TODO EN LA BUSQUEDA DE PROFUNDIDAD

