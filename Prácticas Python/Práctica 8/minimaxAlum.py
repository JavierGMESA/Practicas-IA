from tictactoeAlum import *


def PSEUDOminimax(nodo):
    mejorJugada = -1
    puntos = -2
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, 1)
            util = utilidad(intento)                #LLAMA TODO EL RATO A UTILIDAD Y LA POCA INTELIGENCIA QUE
            if util > puntos:                       #PUEDE APLICAR ES: SI CON LA SIGUIENTE JUGADA GANO, APLICO
                puntos = util                       #DICHA JUGADA DE INMEDIATO
                mejorJugada = jugada
    nodo = aplicaJugada(nodo, mejorJugada, 1)
    return nodo


def jugadaAdversario(nodo):
    valida = False
    jugada = None
    while not valida:
        fila = int(input("Fila: "))
        col = int(input("Col: "))
        jugada = Jugada(fila, col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def minimax(nodo) -> Nodo:
    jugador = 1
    mejor_jugada = jugadas[0]
    max = -10000
    for j in jugadas:
        if esValida(nodo, j):
            intento = aplicaJugada(nodo, j, jugador)
            max_actual = valorMin(intento)
            if max_actual > max:
                max = max_actual
                mejor_jugada = j
    nodo = aplicaJugada(nodo, mejor_jugada, jugador)
    return nodo
    #raise NotImplementedError


def valorMin(nodo) -> int:
    jugador = -1
    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        valor_min = 100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_min = min(valor_min, valorMax(aplicaJugada(nodo, j, jugador)))
    return valor_min

    #raise NotImplementedError


def valorMax(nodo) -> int:
    jugador = 1
    if terminal(nodo):
        valor_max = utilidad(nodo)
    else:
        valor_max = -100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_max = max(valor_max, valorMin(aplicaJugada(nodo, j, jugador)))
    return valor_max
    #raise NotImplementedError
