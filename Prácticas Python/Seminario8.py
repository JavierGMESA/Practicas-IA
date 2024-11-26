from dataclasses import dataclass
import numpy as np
from copy import deepcopy

@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    p_MAX: int
    p_MIN: int

    def __init__(self, tam):
        self.tablero = np.array(np.zeros(tam, dtype=int)) #IMPORTANTE: CREAR VECTOR INICIALIZADO A 0
        self.vacias = tam
        self.p_MAX = self.p_MIN = 0

@dataclass
class Jugada:
    ficha: int

    def __init__(self, ficha):
        self.ficha = ficha

def esValida(nodo: Nodo, jugada: Jugada) -> bool:
    valido = True
    if jugada.ficha < 1 or jugada.ficha > len(nodo.tablero):
        valido = False
    elif nodo.tablero[jugada.ficha - 1] != 0:
        valido = False
    return valido

def aplicaJugada(nodo: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo = deepcopy(nodo)
    nuevo.tablero[jugada.ficha - 1] = jugador
    if jugador == 1:
        nuevo.p_MAX += jugada.ficha
    else:
        nuevo.p_MIN += jugada.ficha
    nuevo.vacias -= 1
    return nuevo

def testTerminal(nodo: Nodo) -> bool:
    return nodo.vacias == 0 or nodo.p_MAX == 15 or nodo.p_MIN == 15

def utilidad(nodo: Nodo) -> int:
    puntuacion = 0
    if nodo.p_MAX == 15:
        puntuacion = 100
    elif nodo.p_MIN == 15:
        puntuacion = (-100)
    else:
        puntuacion = 0
    return puntuacion

nodo = Nodo(7)
print(nodo)