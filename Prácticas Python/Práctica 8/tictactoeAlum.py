from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import numpy as np

visual = {1: "❌", -1: "⭕", 0.0: " "}


@dataclass
class Nodo:
    tablero: np.array
    vacias: int
    N: int

    def __init__(self, tablero):
        self.tablero = tablero
        self.N = self.tablero.shape[0]
        self.vacias = len(np.where(tablero == 0)[0])

    def __str__(self):
        string = f"{' ----+----+----'}\n|"
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if i == 2 and j == 2:
                string += f"\n ----+----+----\n"
            else:
                string += f"\n ----+----+----\n|"
        return f"{string}"


@dataclass
class Jugada:
    x: int
    y: int

    def __str__(self):
        return f"\nFila: ({self.x}, Col: {self.y})"


######
# Se crean todas las posibles jugadas para el for de rango (for jugada in jugadas)
jugadas = []
for i in range(0, 3):
    for j in range(0, 3):
        jugadas.append(Jugada(i, j))
######

def crearNodo(tablero):
    return Nodo(tablero)


def nodoInicial():
    tablero_inicial = np.zeros((3, 3))
    return Nodo(tablero_inicial)


def opuesto(jugador):
    return jugador * -1


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo = deepcopy(actual)
    nuevo.tablero[jugada.x][jugada.y] = jugador
    nuevo.vacias -= 1
    return nuevo

    raise NotImplementedError


def esValida(actual: Nodo, jugada: Jugada) -> bool:
    valida = True
    if jugada.x < 0 or jugada.x > 2 or jugada.y < 0 or jugada.y > 2:
        valida = False
    elif actual.tablero[jugada.x][jugada.y] != 0 :
        valida = False
    return valida

    #raise NotImplementedError


victorias = [
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def terminal(actual: Nodo) -> bool:
    fin = False

    #Primera Versión usando el tablero como matriz

    #tab = actual.tablero
    #i = 0
    #while i < 2 and not fin:
    #    if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2] and tab[i][0] != 0:
    #        fin = True
    #    elif tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i] and tab[0][i] != 0:
    #        fin = True
    #
    #    i+= 1
    #if not fin and tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] != 0:
    #    fin = True
    #elif tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[1][1] != 0:
    #    fin = True
    #elif actual.vacias == 0:
    #    fin = True

    #Segunda versión usando la función reshape() o flatten() para convertir el tablero en un vector
    tab = actual.tablero.reshape(9)                                         #IMPORTANTE: FUNCIÓN shape DE np.array PARA TRANSFORMAR DE MATRIZ A VECTOR.
    if actual.vacias == 0:                                                  #TAMBIÉN SE PUEDE USAR LA FUNCIÓN flatten PARA LO MISMO
        fin = True
    else:
        for v in victorias:
            if tab[v[0]] == tab[v[1]] and tab[v[1]] == tab[v[2]] and tab[v[0]] != 0:
                fin = True
    
    return fin

    #raise NotImplementedError


def utilidad(nodo: Nodo) -> int:
    puntuacion = 0

    #Primera Versión usando el tablero como matriz

    #tab = nodo.tablero
    #i = 0
    #if nodo.vacias != 0:
    #    while i < 2 and puntuacion == 0:
    #        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2] and tab[i][0] != 0:
    #            puntuacion = tab[i][0] * 100
    #        elif tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i] and tab[0][i] != 0:
    #            puntuacion = tab[0][i] * 100
    #
    #        i+= 1
    #    if puntuacion == 0 and tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] != 0:
    #        puntuacion = tab[1][1] * 100
    #    elif tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[1][1] != 0:
    #        puntuacion = tab[1][1] * 100

    #Segunda versión usando la función reshape() o flatten() para convertir el tablero en un vector
    tab = nodo.tablero.reshape(9)
    for v in victorias:
        if tab[v[0]] == tab[v[1]] and tab[v[1]] == tab[v[2]] and tab[v[0]] != 0:
            puntuacion = tab[v[0]] * 100
    
    return puntuacion

    #raise NotImplementedError


if __name__ == "__main__":
    M = np.array([
        [1,2],
        [3,4]
    ])
    print(M)
    M_vector = M.reshape(4)
    print(M_vector)
    M_vector = M.flatten()
    print(M_vector)
    M_de_nuevo = M_vector.reshape(2,2)
    print(M_de_nuevo)