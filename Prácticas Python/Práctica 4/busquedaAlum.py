from __future__ import annotations
from NPuzle_Alum import *


@dataclass
class Nodo:
    estado: tEstado
    operador: str
    costeCamino: int
    profundidad: int
    padre: Nodo


def nodoInicial() -> Nodo:
    return Nodo(estadoInicial(), None, 0, 0, None)


def dispCamino(nodo: Nodo) -> None:         #función para mostrar la rama que ha seguido un nodo hoja
    lista = []
    aux = nodo
    while aux.padre != None:
        lista.append((aux.estado.tablero, aux.operador))
        aux = aux.padre
    for i in lista[::-1]: # Se utiliza ::-1 para recorrer la lista en sentido inverso, desde la raíz hasta el nodo objetivo.
        print("Operador: ", operadores[i[1]], "\n", i[0])
        print()


def dispSolucion(nodo: Nodo) -> None:
    dispCamino(nodo)
    print("Profundidad: ", nodo.profundidad)
    print("Coste: ", nodo.costeCamino)


def expandir(nodo: Nodo) -> list:
    nodos: list
    nodos = []
    NUM_OPERADORES = ["8", "2", "4", "6"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            nuevo = Nodo(aplicaOperador(op, nodo.estado), op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
            nodos.append(nuevo)

    return nodos


def busquedaAnchura() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    
    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            sucesores = expandir(actual)
            abiertos += sucesores

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaProfundidad() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            sucesores = expandir(actual)
            for sucesor in sucesores[::-1]:
                abiertos.insert(0, sucesor)

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

