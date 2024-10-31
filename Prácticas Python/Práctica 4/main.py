from busquedaAlum import *

objetivo = busquedaAnchura()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaProfundidad()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")
