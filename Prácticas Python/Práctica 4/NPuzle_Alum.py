import numpy as np
from dataclasses import dataclass
import copy

operadores = {"8": "ARRIBA", "2": "ABAJO", "4": "IZQUIERDA", "6": "DERECHA"}


@dataclass
class tEstado:
    tablero: np.ndarray #IMPORTANTE: Matriz de Numpy a usar por facilidades
    fila: int
    col: int

    def __init__(self, tablero: np.ndarray):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        fila, col = np.where(self.tablero == 0) #IMPORTANTE: la función where devuelve ([0], [0]), no (0, 0)
        self.fila = fila[0]
        self.col = col[0]

    def __repr__(self) -> str: # Permite representar el objeto como cadena
        return f"{self.tablero}\n Fila: {self.fila}\n Col: {self.col}\n"


def estadoInicial() -> tEstado:
    puzle_inicial = np.array(
    [
        [0, 2, 3], 
        [1, 4, 5], 
        [8, 7, 6]
    ])
    return tEstado(puzle_inicial)


def estadoObjetivo() -> tEstado:
    puzle_final = np.array(
    [
        [1, 2, 3], 
        [0, 4, 5], 
        [8, 7, 6]
    ])
    return tEstado(puzle_final)


def coste(operador: str, estado: tEstado) -> int:
    return 1


def dispOperador(operador: str) -> None:
    print(f"Operador: {operadores[operador]}")


def iguales(actual: tEstado, objetivo: tEstado) -> bool:
    iguales = False
    iguales = (actual.tablero == objetivo.tablero).all()        #IMPORTANTE: COMPARAR MATRICES CON UNA SOLA INSTRUCCIÓN
    
    return iguales


def testObjetivo(actual: tEstado) -> bool:
    objetivo = estadoObjetivo()
    return iguales(actual, objetivo)


def esValido(operador: str, estado: tEstado) -> bool:
    valido = False                                              #IMPORTANTE: EMPEZAMOS CON valida A False
    match operadores[operador]:
        case "ARRIBA":
            valido = (estado.fila > 0)
        case "ABAJO":
            valido = (estado.fila < 2)
        case "IZQUIERDA":
            valido = (estado.col > 0)
        case "DERECHA":
            valido = (estado.col < 2)

    return valido



def aplicaOperador(operador: str, estado: tEstado) -> tEstado:
    nuevo = copy.deepcopy(estado) # Se hace la copia completa del estado anterior
    ficha = 0
    match operadores[operador]:
        case "ARRIBA":
            nuevo.tablero[nuevo.fila][nuevo.col] = nuevo.tablero[nuevo.fila - 1][nuevo.col]
            nuevo.tablero[nuevo.fila - 1][nuevo.col] = ficha
            nuevo.fila = nuevo.fila - 1
        case "ABAJO":
            nuevo.tablero[nuevo.fila][nuevo.col] = nuevo.tablero[nuevo.fila + 1][nuevo.col]
            nuevo.tablero[nuevo.fila + 1][nuevo.col] = ficha
            nuevo.fila = nuevo.fila + 1
        case "IZQUIERDA":
            nuevo.tablero[nuevo.fila][nuevo.col] = nuevo.tablero[nuevo.fila][nuevo.col - 1]
            nuevo.tablero[nuevo.fila][nuevo.col - 1] = ficha
            nuevo.col = nuevo.col - 1
        case "DERECHA":
            nuevo.tablero[nuevo.fila][nuevo.col] = nuevo.tablero[nuevo.fila][nuevo.col + 1]
            nuevo.tablero[nuevo.fila][nuevo.col + 1] = ficha
            nuevo.col = nuevo.col + 1
    
    return nuevo

