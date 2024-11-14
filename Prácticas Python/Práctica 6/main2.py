from busquedaAlum3Piezas import *

#ESTE PRIMERO HACE UN BUCLE INFINITO
objetivo = BusquedaHeuristicaVoraz()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = BusquedaHeuristicaVorazNoRepetidos()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")