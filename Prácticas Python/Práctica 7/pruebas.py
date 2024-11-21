import busquedaAlumPuzle8 as b1
import busquedaAlumPuzle15 as b2
import numpy as np

tablero1 = np.array(
    [
        [1, 3, 0], 
        [6, 2, 4], 
        [8, 7, 5]
])

tablero2 = np.array(
    [
        [6, 3, 1], 
        [8, 0, 4], 
        [7, 5, 2]
])

tablero3 = np.array(
    [
        [1, 2, 3, 4], 
        [5, 6, 15, 8], 
        [9, 10, 0, 12],
        [13, 14, 7, 11]
])

print("Pruebas del primer tablero")
b1.BusquedaHeuristicaVorazPiezasMalColocadas(tablero1)
b1.BusquedaHeuristicaVorazManhattan(tablero1)
b1.BusquedaAEstrellaPiezasNoColocadas(tablero1)
b1.BusquedaAEstrellaManhattan(tablero1)

print("Pruebas del segundo tablero")
b1.BusquedaHeuristicaVorazPiezasMalColocadas(tablero2)
b1.BusquedaHeuristicaVorazManhattan(tablero2)
b1.BusquedaAEstrellaPiezasNoColocadas(tablero2)
b1.BusquedaAEstrellaManhattan(tablero2)

print("Pruebas del tercer tablero")
b2.BusquedaHeuristicaVorazPiezasMalColocadas(tablero3)
b2.BusquedaHeuristicaVorazManhattan(tablero3)
b2.BusquedaAEstrellaPiezasNoColocadas(tablero3)
b2.BusquedaAEstrellaManhattan(tablero3)

#IMPORTANTE: RESPUESTAS A LAS PREGUNTAS
# b) ¿Son Admisibles ambas heurísticas?
# Ambas son admisibles pues generan un coste estimado menor o igual que es coste real siempre
# c) ¿Cuál es la heurística dominante?
# La de Distancias de Manhattan pues genera menos nodos. ESO SI, LA DISTANCIA DE MANHATTAN ES ADMISIBLE
# SI NO SE TIENE EN CUENTA EL HUECO COMO PIEZA MAL COLOCADA
# d) ¿En qué afecta el cambio de orden en los operadores (optimalidad, completitud, eficiencia,
# etc.)?
# En el número de nodos Generados (pues su orden puede conducir antes a otra solución), los nodos
# visitados y por lo primero también la longitud máxima