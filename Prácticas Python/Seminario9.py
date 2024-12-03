# CINQUILLO SOLO CON OROS Y BASTOS, Y SOLO 2 JUGADORES

# Tenemos las cartas de MAX, las cartas de MIN, y la MESA.
# La primera carta que hay que poner es el 5.
# El juego comienza con el jugador que tenga el 5 de oros. 
# Gana el primero que se quede sin cartas. 
# Es posible pasar, pero si tiene carta que pueda poner, debe ponerla.

# aplicaJugada: colocar carta en la mesa
# esValida: posee la carta y la puede poner. Si es un 5 la pone sin restricciones.
# Que se pueda colocar significa que haya una diferencia de 1 con respecto al 
# extremo superior o al inferior.

# Propuesta de clase: 
# Representar todo con una matriz de 2 filas y 11 columnas donde cada celda
# corresponde a una carta y nos dice si esa carta la tiene MAX, la tiene MIN, o está
# en la mesa

# IMPORTANTE
# Como heurística se podría escoger el número de cartas, pero eso es flojo.
# Una mejor heurística sería valorar las cartas (no es tan valioso el 5 que la sota)



import numpy as np
from copy import deepcopy
from dataclasses import dataclass

# Mi propuesta
@dataclass
class Nodo:
    mesa: np.ndarray
    cartasMax: list
    cartasMin: list

    def __init__(self, Max: list, Min: list):
        self.cartasMax = Max
        self.cartasMin = Min
        self.mesa = np.array([[-1, -1], [-1, -1]])

@dataclass
class Jugada:
    palo: int
    valor: int

    def __init__(self, palo: int, valor: int):
        self.palo = palo
        self.valor = valor

def esValida(actual: Nodo, jugada: Jugada, jugador: int) -> bool:
    valida = True
    if jugador == 1:
        if (jugada.valor, jugada.palo) not in actual.cartasMax:
            valida = False
        elif (jugada.valor - actual.mesa[jugada.palo][1] != 1) or (actual.mesa[jugada.palo][0] - jugada.valor != 1):
            valida = False
    else:
        if (jugada.valor, jugada.palo) not in actual.cartasMin:
            valida = False
        elif (jugada.valor - actual.mesa[jugada.palo][1] != 1) or (actual.mesa[jugada.palo][0] - jugada.valor != 1):
            valida = False
    
    return valida

def aplicaJugada(actual: Nodo, jugada: Jugada, jugador: int) -> Nodo:
    nuevo = deepcopy(actual)
    if jugador == 1:
        actual.cartasMax.remove((jugada.valor, jugada.palo))        #IMPORTANTE
    else:
        actual.cartasMin.remove((jugada.valor, jugada.palo))
    # sigue

    return nuevo
