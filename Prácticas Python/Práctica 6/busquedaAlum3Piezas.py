from __future__ import annotations
from Piezas3_Alum import *


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

def f(nodo: Nodo) -> int:
    return h(nodo.estado)

def expandir(nodo: Nodo) -> list:
    nodos: list
    nodos = []
    NUM_OPERADORES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            nuevo = Nodo(aplicaOperador(op, nodo.estado), op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
            nodos.append(nuevo)

    return nodos

def expandirNoRepetidos(nodo: Nodo, cerrados: list) -> list:
    nodos: list
    nodos = []
    NUM_OPERADORES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            estado = aplicaOperador(op, nodo.estado)
            i = 0
            coincide = False
            while(i < len(cerrados) and not coincide):
                coincide = (iguales(cerrados[i].estado, estado))
                i += 1
            if not coincide:
                nuevo = Nodo(estado, op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
                nodos.append(nuevo)

    return nodos

def expandirNoRepetidos2(nodo: Nodo, cerrados: set) -> list:
    nodos: list
    nodos = []
    NUM_OPERADORES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            estado = aplicaOperador(op, nodo.estado)
            if not (estado.crearHash() in cerrados): #IMPORTANTE: COMPROBAMOS SI ESTÁ EN LA TABLA HASH
                nuevo = Nodo(estado, op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
                nodos.append(nuevo)

    return nodos

def expandirNoRepetidosHeuristica(nodo: Nodo, cerrados: list) -> list:
    nodos: list
    nodos = []
    coincide: bool
    NUM_OPERADORES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for op in NUM_OPERADORES:
        if esValido(op, nodo.estado):
            estado = aplicaOperador(op, nodo.estado)
            nuevo = Nodo(estado, op, nodo.costeCamino + coste(op, nodo.estado), nodo.profundidad + 1, nodo)
            i = 0
            coincide = False
            while(i < len(cerrados) and not coincide):
                coincide = (iguales(cerrados[i].estado, estado) and (f(cerrados[i]) <= f(nuevo)))
                i += 1
            if not coincide:
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

def busquedaProfundidadLimitada(limite) -> bool:
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
            if actual.profundidad < limite:     #CONTROL DEL LÍMITE
                sucesores = expandir(actual)
                abiertos = sucesores + abiertos

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo


def busquedaProfundidadLimitadaIterativa() -> bool:
    
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    limite = 0
    while not objetivo:
        abiertos.append(raiz)

        while not(objetivo) and not(len(abiertos) == 0):
            actual = abiertos.pop(0)
            if(testObjetivo(actual.estado)):
                objetivo = True
            else:   
                if actual.profundidad < limite:
                    sucesores = expandir(actual)
                    abiertos = sucesores + abiertos
        limite += 1

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def busquedaAnchuraNoRepetidos1() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    cerrados = []
    sucesores = []
    
    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        #print(actual.estado.tablero)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            sucesores = expandirNoRepetidos(actual, cerrados)
            abiertos += sucesores

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def busquedaProfundidadNoRepetidos1() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    cerrados = []
    sucesores = []

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            sucesores = expandirNoRepetidosHeuristica(actual, cerrados)
            for sucesor in sucesores[::-1]:
                abiertos.insert(0, sucesor)

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def busquedaAnchuraNoRepetidos2() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    cerrados = set()            #IMPORTANTE: PARA OPTIMIZAR USAMOS UNA TABLA HASH (UN SET DONDE GUARDAMOS LOS IDENTIFICADORES DE LOS ESTADOS YA PROCESADOS)
    sucesores = []
    
    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        #print(actual.estado.tablero)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.add(actual.estado.crearHash())
            sucesores = expandirNoRepetidos2(actual, cerrados)
            abiertos += sucesores

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def busquedaProfundidadNoRepetidos2() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    cerrados = set()
    sucesores = []

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)
        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.add(actual.estado.crearHash())
            sucesores = expandirNoRepetidos2(actual, cerrados)
            for sucesor in sucesores[::-1]:
                abiertos.insert(0, sucesor)

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def BusquedaHeuristicaVoraz() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)

        #print(actual.estado)
        #print(f(actual))

        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            sucesores = expandir(actual)
            for sucesor in sucesores:
                i = 0
                while(i < len(abiertos) and f(sucesor) >= f(abiertos[i])):
                    i += 1
                if(i == len(abiertos)):
                    abiertos.append(sucesor)
                else:
                    abiertos.insert(i, sucesor)

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo

def BusquedaHeuristicaVorazNoRepetidos() -> bool:
    objetivo = False
    raiz = nodoInicial()
    abiertos = []
    sucesores = []
    cerrados = []

    abiertos.append(raiz)
    
    while not(objetivo) and not(len(abiertos) == 0):
        actual = abiertos.pop(0)

        #print(actual.estado)
        #print(f(actual))

        if(testObjetivo(actual.estado)):
            objetivo = True
        else:
            cerrados.append(actual)
            sucesores = expandirNoRepetidosHeuristica(actual, cerrados)
            for sucesor in sucesores:
                i = 0
                while(i < len(abiertos) and f(sucesor) >= f(abiertos[i])):
                    i += 1
                if(i == len(abiertos)):
                    abiertos.append(sucesor)
                else:
                    abiertos.insert(i, sucesor)

    if objetivo:
        dispSolucion(actual)
    elif not objetivo:
        print("No se ha encontrado solución")

    return objetivo