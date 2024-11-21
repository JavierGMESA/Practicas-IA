from __future__ import annotations
from Puzle8_Alum import *


@dataclass
class Nodo:
    estado: tEstado
    operador: str
    costeCamino: int
    profundidad: int
    padre: Nodo


def nodoInicial() -> Nodo:
    return Nodo(estadoInicial(), None, 0, 0, None)

def nodoInicial2(tablero) -> Nodo:
    return Nodo(tEstado(tablero), None, 0, 0, None)

def f1(nodo: Nodo) -> int: #Para la búsqueda Voraz con Piezas mal colocadas
    return h1(nodo.estado)

def f2(nodo: Nodo) -> int: #Para la búsqueda Voraz con Distancias de Manhattan
    return h2(nodo.estado)

def f3(nodo: Nodo) -> int: #Para el A* con Piezas mal colocadas
    return nodo.costeCamino + h1(nodo.estado)

def f4(nodo:Nodo) -> int: #Para el A* con Distancias de Manhattan
    return nodo.costeCamino + h2(nodo.estado)

def expandir(nodo: Nodo) -> list:
    nodos: list
    nodos = []
    NUM_OPERADORES = ["8", "2", "4", "6"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            nuevo = Nodo(aplicaOperador(op, nodo.estado), op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
            nodos.append(nuevo)

    return nodos

def BusquedaHeuristicaVorazPiezasMalColocadas(tablero):
    objetivo = False
    raiz = nodoInicial2(tablero)
    abiertos = []
    cerrados = []
    sucesores = []
    generados = 0
    visitados = 0
    longitud = 0

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            visitados += 1
            sucesores = expandir(actual)
            generados += len(sucesores)
            for sucesor in sucesores:
                i = 0
                coincide = False
                while(i < len(cerrados) and not coincide):
                    coincide = (iguales(cerrados[i].estado, sucesor.estado) and (f1(cerrados[i]) <= f1(sucesor)))
                    i += 1
                if not coincide:
                    i = 0
                    while(i < len(abiertos) and f1(sucesor) >= f1(abiertos[i])):
                        i += 1
                    if(i == len(abiertos)):
                        abiertos.append(sucesor)
                    else:
                        abiertos.insert(i, sucesor)
            if(len(abiertos) > longitud):
                longitud = len(abiertos)
    if objetivo:
        print("Resultado de la búsqueda Voraz con Piezas mal colocadas")
        print(f"COSTE SOLUCION:  {actual.costeCamino}")
        print(f"Generados:       {generados}")
        print(f"Visitados:       {visitados}")
        print(f"Máxima Longitud: {longitud}")
    else:
        print("No se ha encontrado solución en la búsqueda Voraz con Piezas mal colocadas")

def BusquedaHeuristicaVorazManhattan(tablero):
    objetivo = False
    raiz = nodoInicial2(tablero)
    abiertos = []
    sucesores = []
    cerrados = []
    generados = 0
    visitados = 0
    longitud = 0

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            visitados += 1
            sucesores = expandir(actual)
            generados += len(sucesores)
            for sucesor in sucesores:
                i = 0
                coincide = False
                while(i < len(cerrados) and not coincide):
                    coincide = (iguales(cerrados[i].estado, sucesor.estado) and (f2(cerrados[i]) <= f2(sucesor)))
                    i += 1
                if not coincide:
                    i = 0
                    while(i < len(abiertos) and f2(sucesor) >= f2(abiertos[i])):
                        i += 1
                    if(i == len(abiertos)):
                        abiertos.append(sucesor)
                    else:
                        abiertos.insert(i, sucesor)
            if(len(abiertos) > longitud):
                longitud = len(abiertos)
    if objetivo:
        print("Resultado de la búsqueda Voraz con Distancias de Manhattan")
        print(f"COSTE SOLUCION:  {actual.costeCamino}")
        print(f"Generados:       {generados}")
        print(f"Visitados:       {visitados}")
        print(f"Máxima Longitud: {longitud}")
    else:
        print("No se ha encontrado solución en la búsqueda Voraz con Distancias de Manhattan")

def BusquedaAEstrellaPiezasNoColocadas(tablero):
    objetivo = False
    raiz = nodoInicial2(tablero)
    abiertos = []
    sucesores = []
    cerrados = []
    generados = 0
    visitados = 0
    longitud = 0

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            visitados += 1
            sucesores = expandir(actual)
            generados += len(sucesores)
            for sucesor in sucesores:
                i = 0
                coincide = False
                while(i < len(cerrados) and not coincide):
                    coincide = (iguales(cerrados[i].estado, sucesor.estado) and (f3(cerrados[i]) <= f3(sucesor)))
                    i += 1
                if not coincide:
                    i = 0
                    while(i < len(abiertos) and f3(sucesor) >= f3(abiertos[i])):
                        i += 1
                    if(i == len(abiertos)):
                        abiertos.append(sucesor)
                    else:
                        abiertos.insert(i, sucesor)
            if(len(abiertos) > longitud):
                longitud = len(abiertos)
    if objetivo:
        print("Resultado del algoritmo A* con Piezas mal colocadas")
        print(f"COSTE SOLUCION:  {actual.costeCamino}")
        print(f"Generados:       {generados}")
        print(f"Visitados:       {visitados}")
        print(f"Máxima Longitud: {longitud}")
    else:
        print("No se ha encontrado solución en el algoritmo A* con Piezas mal colocadas")

def BusquedaAEstrellaManhattan(tablero):
    objetivo = False
    raiz = nodoInicial2(tablero)
    abiertos = []
    sucesores = []
    cerrados = []
    generados = 0
    visitados = 0
    longitud = 0

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            visitados += 1
            sucesores = expandir(actual)
            generados += len(sucesores)
            for sucesor in sucesores:
                i = 0
                coincide = False
                while(i < len(cerrados) and not coincide):
                    coincide = (iguales(cerrados[i].estado, sucesor.estado) and (f4(cerrados[i]) <= f4(sucesor)))
                    i += 1
                if not coincide:
                    i = 0
                    while(i < len(abiertos) and f4(sucesor) >= f4(abiertos[i])):
                        i += 1
                    if(i == len(abiertos)):
                        abiertos.append(sucesor)
                    else:
                        abiertos.insert(i, sucesor)
            if(len(abiertos) > longitud):
                longitud = len(abiertos)
    if objetivo:
        print("Resultado del algoritmo A* con Piezas mal colocadas")
        print(f"COSTE SOLUCION:  {actual.costeCamino}")
        print(f"Generados:       {generados}")
        print(f"Visitados:       {visitados}")
        print(f"Máxima Longitud: {longitud}")
    else:
        print("No se ha encontrado solución en el algoritmo A* con Distancias de Manhattan")