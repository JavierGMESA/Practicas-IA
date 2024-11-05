#PROBLEMA DEL TABLERO CON 3 FICHAS
from dataclasses import dataclass
import numpy as np
from copy import deepcopy

@dataclass
class tEstado:
    tablero: np.ndarray #Igualmente en el tablero guardaremos un 1 donde esté A, un 2 donde esté B y un 3 donde esté C
    fA: int
    fB: int
    fC: int
    cA: int
    cB: int
    cC: int

#No hay proceso derrivado: no hago constructor
    

operadores = {
    "1": "ARRIBA_A",
    "2": "ABAJO_A",
    "3": "IZQUIERDA_A",
    "4": "DERECHA_A",
    #...
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
    estado = tEstado()
    estado.tablero = tablero
    estado.fA, estado.cA = 3, 1
    estado.fB, estado.cB = 4, 4
    estado.fC, estado.cC = 1, 3
    return estado

def estadoObjetivo():
    pass

def esValido (op, estado):
    valido = False
    match operadores[op]:
        case "ARRIBA_A":
            valido = (estado.fA - 1 > 0 and estado.tablero[estado.fA - 1][estado.cA - 1] == 0 and estado.tablero[estado.fA - 1][estado.cA + 1] == 0 and estado.tablero[estado.fA - 2][estado.cA] == 0)
        case "ABAJO_A":
            pass
        #...

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