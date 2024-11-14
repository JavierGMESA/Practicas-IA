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

    def __repr__(self) -> str: # Permite representar el objeto como cadena
        return f"{self.tablero}\n"
    
    def crearHash(self) -> str: #IMPORTANTE: FUNCIÓN QUE DEVUELVE UN HASH (IDENTIFICADOR) DEL TABLERO
        return f"{self.tablero.tobytes()}{self.fA}{self.cA}{self.fB}{self.cB}{self.fC}{self.cC}"


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
            [-1, 0, 0, 3, 0, 0],
            [0, 1, 0, 3, 0, 0],
            [1, 1, 1, -1, 2, 0],
            [0, 1, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0]
        ]
    )
    estado = tEstado(tablero, 3, 1, 4, 4, 1, 3)
    return estado

def estadoObjetivo():
    tablero = np.array(
        [
            [-1, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, -1, 0, 3],
            [1, 1, 1, 2, 0, 3],
            [0, 1, 2, 2, 2, 3]
        ]
    )
    estado = tEstado(tablero, 4, 1, 5, 3, 4, 5)
    return estado

#IMPORTANTE
#FUNCIÓN HEURÍSTICA QUE DEVUELVE UN COSTE BASADO EN LAS DISTANCIAS DE MANHATAN ENTRE LA
#POSICIÓN ACTUAL DE LAS PIEZAS Y LA POSICIÓN OBJETIVO
def h(estado: tEstado) -> int:
    objetivo = estadoObjetivo()
    return abs(estado.fA - objetivo.fA) + abs(estado.fB - objetivo.fB) + abs(estado.fC - objetivo.fC) + abs(estado.cA - objetivo.cA) + abs(estado.cB - objetivo.cB) + abs(estado.cC - objetivo.cC)

#IMPORTANTE
#FUNCIÓN DE EVALUACIÓN QUE DEVUELVE UN COSTE BASADO EN LAS DISTANCIAS DE MANHATAN ENTRE LA
#POSICIÓN ACTUAL DE LAS PIEZAS Y LA POSICIÓN OBJETIVO MÁS EL COSTE DE LLEGAR DE LA RAIZ AL 
#NODO ACTUAL (ALGORITMO A*)
#def f(Actual) -> int:
#    return Actual.coste + h(Actual.estado)

def esValido (op, estado: tEstado):
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
            valido = (estado.fB - 1 > 0 and estado.tablero[estado.fB - 1][estado.cB - 1] == 0 and  estado.tablero[estado.fB - 2][estado.cB] == 0 and estado.tablero[estado.fB - 1][estado.cB + 1] == 0)
        case "ABAJO_B":
            valido = (estado.fB < 5 and estado.tablero[estado.fB + 1][estado.cB - 1] == 0 and estado.tablero[estado.fB + 1][estado.cB] == 0 and estado.tablero[estado.fB + 1][estado.cB + 1] == 0)
        case "IZQUIERDA_B":
            valido = (estado.cB - 1 > 0 and estado.tablero[estado.fB][estado.cB - 2] == 0 and estado.tablero[estado.fB - 1][estado.cB - 1] == 0)
        case "DERECHA_B":
            valido = (estado.cB + 1 < 5 and estado.tablero[estado.fB][estado.cB + 2] == 0 and estado.tablero[estado.fB - 1][estado.cB + 1] == 0)
        case "ARRIBA_C":
            valido = (estado.fC - 1 > 0 and estado.tablero[estado.fC - 2][estado.cC] == 0)
        case "ABAJO_C":
            valido = (estado.fC + 1 < 5 and estado.tablero[estado.fC + 2][estado.cC] == 0)
        case "IZQUIERDA_C":
            valido = (estado.cC > 0 and estado.tablero[estado.fC - 1][estado.cC - 1] == 0 and estado.tablero[estado.fC][estado.cC - 1] == 0 and estado.tablero[estado.fC + 1][estado.cC - 1] == 0)
        case "DERECHA_C":
            valido = (estado.cC < 5 and estado.tablero[estado.fC - 1][estado.cC + 1] == 0 and estado.tablero[estado.fC][estado.cC + 1] == 0 and estado.tablero[estado.fC + 1][estado.cC + 1] == 0)
        
    return valido

def aplicaOperador(op, estado: tEstado):
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
            nuevo.tablero[nuevo.fA + 2][nuevo.cA] = 1
            nuevo.tablero[nuevo.fA + 1][nuevo.cA - 1] = 1
            nuevo.tablero[nuevo.fA + 1][nuevo.cA + 1] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA - 1] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA + 1] = 0
            nuevo.fA += 1
        case "IZQUIERDA_A":
            nuevo.tablero[nuevo.fA][nuevo.cA - 2] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA - 1] = 1
            nuevo.tablero[nuevo.fA + 1][nuevo.cA - 1] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA + 1] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA + 2] = 0
            nuevo.tablero[nuevo.fA + 1][nuevo.cA + 1] = 0
            nuevo.cA -= 1
        case "DERECHA_A":
            nuevo.tablero[nuevo.fA][nuevo.cA + 2] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA + 1] = 1
            nuevo.tablero[nuevo.fA + 1][nuevo.cA + 1] = 1
            nuevo.tablero[nuevo.fA - 1][nuevo.cA - 1] = 0
            nuevo.tablero[nuevo.fA][nuevo.cA - 2] = 0
            nuevo.tablero[nuevo.fA + 1][nuevo.cA - 1] = 0
            nuevo.cA += 1
        case "ARRIBA_B":
            nuevo.tablero[nuevo.fB - 2][nuevo.cB] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB - 1] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB + 1] = 2
            nuevo.tablero[nuevo.fB][nuevo.cB] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB - 1] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB + 1] = 0
            nuevo.fB -= 1
        case "ABAJO_B":
            nuevo.tablero[nuevo.fB + 1][nuevo.cB] = 2
            nuevo.tablero[nuevo.fB + 1][nuevo.cB - 1] = 2
            nuevo.tablero[nuevo.fB + 1][nuevo.cB + 1] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB - 1] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB + 1] = 0
            nuevo.fB += 1
        case "IZQUIERDA_B":
            nuevo.tablero[nuevo.fB][nuevo.cB - 2] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB - 1] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB + 1] = 0
            nuevo.cB -= 1
        case "DERECHA_B":
            nuevo.tablero[nuevo.fB][nuevo.cB + 2] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB + 1] = 2
            nuevo.tablero[nuevo.fB - 1][nuevo.cB] = 0
            nuevo.tablero[nuevo.fB][nuevo.cB - 1] = 0
            nuevo.cB += 1
        case "ARRIBA_C":
            nuevo.tablero[nuevo.fC - 2][nuevo.cC] = 3
            nuevo.tablero[nuevo.fC + 1][nuevo.cC] = 0
            nuevo.fC -= 1
        case "ABAJO_C":
            nuevo.tablero[nuevo.fC + 2][nuevo.cC] = 3
            nuevo.tablero[nuevo.fC - 1][nuevo.cC] = 0
            nuevo.fC += 1
        case "IZQUIERDA_C":
            nuevo.tablero[nuevo.fC - 1][nuevo.cC -1] = 3
            nuevo.tablero[nuevo.fC][nuevo.cC - 1] = 3
            nuevo.tablero[nuevo.fC + 1][nuevo.cC - 1] = 3
            nuevo.tablero[nuevo.fC - 1][nuevo.cC] = 0
            nuevo.tablero[nuevo.fC][nuevo.cC] = 0
            nuevo.tablero[nuevo.fC + 1][nuevo.cC] = 0
            nuevo.cC -= 1
        case "DERECHA_C":
            nuevo.tablero[nuevo.fC - 1][nuevo.cC +1] = 3
            nuevo.tablero[nuevo.fC][nuevo.cC + 1] = 3
            nuevo.tablero[nuevo.fC + 1][nuevo.cC + 1] = 3
            nuevo.tablero[nuevo.fC - 1][nuevo.cC] = 0
            nuevo.tablero[nuevo.fC][nuevo.cC] = 0
            nuevo.tablero[nuevo.fC + 1][nuevo.cC] = 0
            nuevo.cC += 1
    
    return nuevo

def coste(operador: str, estado: tEstado) -> int:
    return 1

def iguales(actual: tEstado, objetivo: tEstado) -> bool:
    iguales = False
    iguales = (actual.fA == objetivo.fA and actual.fB == objetivo.fB and actual.fC == objetivo.fC and actual.cA == objetivo.cA and actual.cB == objetivo.cB and actual.cC == objetivo.cC)
    return iguales

def testObjetivo(e: tEstado):
    obj = estadoObjetivo()
    return iguales(e, obj)