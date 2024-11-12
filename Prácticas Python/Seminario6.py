#MISMO PROBLEMA DE NPUZLE PERO CON BÚSQUEDA HEURÍSTICA
from dataclasses import dataclass
import numpy as np
from copy import deepcopy

@dataclass
class tEstado:
    tablero: np.ndarray
    fA: int
    fB: int
    fC: int
    cA: int
    cB: int
    cC: int

    def __init__(self, tablero, fA, cA, fB, cB, fC, cC):
        self.tablero = tablero
        self.fA = fA
        self.fB = fB
        self.fC = fC
        self.cA = cA
        self.cB = cB
        self.cC = cC


operadores = {
    "1": "ARRIBA_A",
    "2": "ABAJO_A",
    "3": "IZQUIERDA_A",
    "4": "DERECHA_A",
    "5": "ARRIBA_B",
    "6": "ABAJO_B",
    "7": "IZQUIERDA_B",
    "8": "DERECHA_B",
    "9": "ARRIBA_C",
    "10": "ABAJO_C",
    "11": "IZQUIERDA_C",
    "12": "DERECHA_C"
}

def estadoInicial():
    tablero = np.array(
        [
            [-1, 0, 0, 3, 0, 0],
            [-1, 0, 0, 3, 0, 0]
            [0, 1, 0, 3, 0, 0]
            [1, 1, 1, -1, 2, 0]
            [0, 1, 0, 2, 2, 2]
            [0, 0, 0, 0, 0, 0]
        ]
    )
    estado = tEstado(tablero, 3, 1, 4, 4, 1, 3)
    return estado

def estadoObjetivo():
    tablero = np.array(
        [
            [-1, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0]
            [0, 0, 0, 0, 0, 0]
            [0, 1, 0, -1, 0, 3]
            [1, 1, 1, 2, 0, 3]
            [0, 1, 2, 2, 2, 3]
        ]
    )
    estado = tEstado(tablero, 4, 1, 5, 3, 4, 5)
    return estado

#IMPORTANTE
#FUNCIÓN HEURÍSTICA QUE DEVUELVE UN COSTE BASADO EN LAS DISTANCIAS DE MANHATAN ENTRE LA
#POSICIÓN ACTUAL DE LAS PIEZAS Y LA POSICIÓN
def h(estado: tEstado) -> int:
    objetivo = estadoObjetivo()
    return abs(estado.fA - objetivo.fA) + abs(estado.fB - objetivo.fC) + abs(estado.fC - objetivo.fC) + abs(estado.cA - objetivo.cA) + abs(estado.cB - objetivo.cB) + abs(estado.cC - objetivo.cC)

def esValido (op, estado):
    valido = False
    match operadores[op]:
        case "ARRIBA_A":
            valido = (estado.fA - 1 > 0 and estado.tablero[estado.fA - 1][estado.cA - 1] == 0 and estado.tablero[estado.fA - 1][estado.cA + 1] == 0 and estado.tablero[estado.fA - 2][estado.cA] == 0)
        case "ABAJO_A":
            valido = (estado.fA + 1 < 5 and estado.tablero[estado.fA + 1][estado.cA - 1] == 0 and estado.tablero[estado.fA + 1][estado.cA + 1] == 0 and estado.tablero[estado.fA + 2][estado.cA] == 0)
        case "IZQUIERDA_A":
            valido = ((estado.cA - 1 > 0 and estado.tablero[estado.fA - 1][estado.cA - 1] == 0 and estado.tablero[estado.fA + 1][estado.cA - 1] == 0 and estado.tablero[estado.fA][estado.cA - 2] == 0))
        case "DERECHA_A":
            valido = ((estado.cA + 1 < 5 and estado.tablero[estado.fA - 1][estado.cA + 1] == 0 and estado.tablero[estado.fA + 1][estado.cA + 1] == 0 and estado.tablero[estado.fA][estado.cA + 2] == 0))
        case "ARRIBA_B":
            valido = (estado.fB - 1 > 0 and estado.tablero[estado.fB - 1][estado.cB - 1] == 0 and  estado.tablero[estado.fB - 2][estado.cB] == 0)
        case "ABAJO_B":
            valido = (estado.fB + 1 < 5 and estado.tablero[estado.fB + 1][estado.cB - 1] == 0 and estado.tablero[estado.fB + 2][estado.cB] == 0)
        

def aplicaOperador(op, estado):
    nuevo = deepcopy(estado)
    match operadores[op]:
        case "ARRIBA_A":
            nuevo.tablero[nuevo.fA - 2][nuevo.cA] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA - 1] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA + 1] = 1
            nuevo.tablero[nuevo.fA + 1][nuevo.cA] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA - 1] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA + 1] = 0
            nuevo.fA -= 1
        case "ABAJO_A":
            pass
        #...

def testObjetivo(e):
    obj = estadoObjetivo()
    return (e.fA == obj.fA and e.fB == obj.fB and e.fC == obj.fC and e.cA == obj.cA and e.cB == obj.cB and e.cC == obj.cC)
