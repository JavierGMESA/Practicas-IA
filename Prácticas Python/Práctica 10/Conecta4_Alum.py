import numpy as np 
from dataclasses import dataclass 
from copy import deepcopy 


@dataclass
class Nodo:
    tablero: np.array
    # Puede añadir más atributos si lo considera oportuno 

    def __init__(self, tablero):
        self.tablero = tablero

    def __str__(self):
        visual = {-1: "🟡", 1: "🔴", 0.0: " "}
        string = ""
        for i in range(self.tablero.shape[0]):
            for j in range(self.tablero.shape[1]):
                if i==0 and j==0:
                    string+="|"
                if self.tablero[i, j] == 0:
                    string += "    |"
                else:
                    string += f" {visual[self.tablero[i, j]]} |"
            if  i < self.tablero.shape[0]-1:
                string += f"\n ----+----+----+----+----+----+----\n|"
            else:
                
                string += f"\n ----+----+----+----+----+----+----\n"
        return f"{string}"

@dataclass
class Jugada:
    # Implementar de acuerdo con lo que necesite o bien, puede eliminarlo y realizar 
    # los cambios en el resto del código que hace referencia a Jugada.
    colum: int

    def __init__(self, col: int):
        self.colum = col

def NodoInicial():
    tablero = np.zeros((6,7))
    return Nodo(tablero)

def NodoInicial_Poda():
    tablero = np.array([
        [1, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 1],
        [1, 1, -1, 0, -1, -1, 1],
        [-1, 1, -1, -1, 1, 1, -1],
        [-1, -1, 1, 1, -1, 1, 1],
        [1, -1, -1, -1, 1, 1, -1]
    ])
    return Nodo(tablero)


def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo = deepcopy(actual)
    i = 0
    while (i + 1 < 7 and nuevo.tablero[i + 1][jugada.colum] != 0):
        i = i + 1
    nuevo.tablero[i][jugada.colum] = jugador
    return nuevo


def esValida(actual: Nodo, jugada: Jugada) -> bool:
    valida = True
    if jugada.colum < 0 or jugada.colum > 6 or actual.tablero[0][jugada.colum] != 0:
        valida = False
    return valida


def terminal(actual: Nodo) -> bool:
    fin = False
    tab = actual.tablero
    i = 0
    while i < 6 and not fin:
        j = 0
        while j < 7 and not fin:
            if tab[i][j] != 0:
                if i < 3:
                    if tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] and tab[i+2][j] == tab[i+3][j]:
                        fin = True

                if not fin:
                    if j < 4:
                        if tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] and tab[i][j+2] == tab[i][j+3]:
                            fin = True
                    
                    if not fin:
                        if i < 3 and j < 4:
                            if tab[i][j] == tab[i+1][j+1] and tab[i+1][j+1] == tab[i+2][j+2] and tab[i+2][j+2] == tab[i+3][j+3]:
                                fin = True
                        if not fin:
                            if i < 3 and j >= 3:
                                if tab[i][j] == tab[i+1][j-1] and tab[i+1][j-1] == tab[i+2][j-2] and tab[i+2][j-2] == tab[i+3][j-3]:
                                    fin = True
                                
                            if not fin:
                                if i >= 3 and j >= 3:
                                    if tab[i][j] == tab[i-1][j-1] and tab[i-1][j-1] == tab[i-2][j-2] and tab[i-2][j-2] == tab[i-3][j-3]:
                                        fin = True
                                if not fin:
                                    if i >= 3 and j < 4:
                                        if tab[i][j] == tab[i-1][j+1] and tab[i-1][j+1] == tab[i-2][j+2] and tab[i-2][j+2] == tab[i-3][j+3]:
                                            fin = True
            j = j + 1
        i = i + 1
    return fin


def utilidad(nodo: Nodo) -> int:
    punt = 0
    tab = nodo.tablero
    i = 0
    while i < 6 and punt == 0:
        j = 0
        while j < 7 and punt == 0:
            if tab[i][j] != 0:
                if i < 4:
                    if tab[i][j] == tab[i+1][j] and tab[i+1][j] == tab[i+2][j] and tab[i+2][j] == tab[i+3][j]:
                        punt = tab[i][j] * 100

                if not punt != 0:
                    if j < 4:
                        if tab[i][j] == tab[i][j+1] and tab[i][j+1] == tab[i][j+2] and tab[i][j+2] == tab[i][j+3]:
                            punt = tab[i][j] * 100
                    
                    if not punt != 0:
                        if i < 4 and j < 4:
                            if tab[i][j] == tab[i+1][j+1] and tab[i+1][j+1] == tab[i+2][j+2] and tab[i+2][j+2] == tab[i+3][j+3]:
                                punt = tab[i][j] * 100
                        if punt != 0:
                            if i < 4 and j >= 3:
                                if tab[i][j] == tab[i+1][j-1] and tab[i+1][j-1] == tab[i+2][j-2] and tab[i+2][j-2] == tab[i+3][j-3]:
                                    punt = tab[i][j] * 100
                                
                            if punt != 0:
                                if i >= 3 and j >= 3:
                                    if tab[i][j] == tab[i-1][j-1] and tab[i-1][j-1] == tab[i-2][j-2] and tab[i-2][j-2] == tab[i-3][j-3]:
                                        punt = tab[i][j] * 100
                                if punt != 0:
                                    if i >= 3 and j < 4:
                                        if tab[i][j] == tab[i-1][j+1] and tab[i-1][j+1] == tab[i-2][j+2] and tab[i-2][j+2] == tab[i-3][j+3]:
                                            punt = tab[i][j] * 100
            j = j + 1
        i = i + 1
    return punt

def heuristica(nodo: Nodo) -> int:
    raise NotImplementedError


tablero = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 1],
    [1, 1, -1, 0, -1, -1, 1],
    [-1, -1, -1, -1, 1, 1, -1],
    [-1, -1, 1, 1, -1, 1, 1],
    [1, -1, -1, -1, 1, 1, -1]
])

act = Nodo(tablero)
if terminal(act):
    print(f"Nodo terminal con utilidad {utilidad(act)}")
