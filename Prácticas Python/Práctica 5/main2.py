from busquedaAlum2 import *

objetivo = busquedaProfundidadLimitada(10)
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

objetivo = busquedaProfundidadLimitadaIterativa()
if objetivo:
    print("Se ha alcanzado una solución")
else:
    print("No se ha alcanzado ninguna solución")

#SE SOLUCIONA EL PROBLEMA DE LOS CICLOS INFINITOS

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

#NO SE OBTIENEN RESULTADOS REPETIDOS

