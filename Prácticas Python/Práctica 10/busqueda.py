from Conecta4_Alum import *

limite = 6
limite_ab = 6

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
        col = int(input("Col: "))
        jugada = Jugada(col)
        valida = esValida(nodo, jugada)
        if not valida:
            print("\n Intenta otra posicion del tablero \n")
    nodo = aplicaJugada(nodo, jugada, -1)
    return nodo


def valorMin(nodo: Nodo, visitados: list) -> int:
    jugador = -1
    visitados[0] += 1
    if terminal(nodo):
        valor_min = utilidad(nodo)
    else:
        valor_min = 100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_min = min(valor_min, valorMax(aplicaJugada(nodo, j, jugador), visitados))
    return valor_min


def valorMax(nodo: Nodo, visitados: list) -> int:
    jugador = 1
    visitados[0] += 1
    if terminal(nodo):
        valor_max = utilidad(nodo)
    else:
        valor_max = -100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_max = max(valor_max, valorMin(aplicaJugada(nodo, j, jugador), visitados))
    return valor_max

def minimax(nodo: Nodo, visitados: list) -> Nodo:
    jugador = 1
    mejor_jugada = jugadas[0]
    max = -10000
    for j in jugadas:
        if esValida(nodo, j):
            intento = aplicaJugada(nodo, j, jugador)
            max_actual = valorMinHeuristico(intento, 1, visitados)
            if max_actual > max:
                max = max_actual
                mejor_jugada = j
    nodo = aplicaJugada(nodo, mejor_jugada, jugador)
    return nodo
    #raise NotImplementedError


def valorMinHeuristico(nodo: Nodo, profundidad: int, visitados: list) -> int:
    jugador = -1
    visitados[0] += 1
    if terminal(nodo):
        valor_min = utilidad(nodo)
    elif profundidad == limite:
        valor_min = heuristica(nodo)

        #print(valor_min)
        #print(nodo)
    else:
        valor_min = 100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_min = min(valor_min, valorMaxHeuristico(aplicaJugada(nodo, j, jugador), profundidad + 1, visitados))
    return valor_min

    #raise NotImplementedError


def valorMaxHeuristico(nodo: Nodo, profundidad: int, visitados: list) -> int:
    jugador = 1
    visitados[0] += 1
    if terminal(nodo):
        valor_max = utilidad(nodo)
    elif profundidad == limite:
        valor_max = heuristica(nodo)

        #print(valor_max)
        #print(nodo)
    else:
        valor_max = -100000
        for j in jugadas:
            if esValida(nodo, j):

                #print(aplicaJugada(nodo, j, jugador))

                valor_max = max(valor_max, valorMinHeuristico(aplicaJugada(nodo, j, jugador), profundidad + 1, visitados))
    return valor_max

def poda_ab(nodo: Nodo, visitados: list) -> Nodo:
    jugador = 1
    alfa = -100000
    beta = 100000
    prof = 0

    mejor_jugada = jugadas[0]
    for jugada in jugadas:
        if esValida(nodo, jugada):
            intento = aplicaJugada(nodo, jugada, jugador)

            #print(intento)

            v = valorMin_ab(intento, prof + 1, alfa, beta, visitados)
            if v > alfa:
                alfa = v
                mejor_jugada = jugada
    
    nodo = aplicaJugada(nodo, mejor_jugada, jugador)
    return nodo

def valorMin_ab(nodo: Nodo, prof: int, alfa: int, beta: int, visitados: list) -> int:
    visitados[0] += 1
    #print(f"Entra en valorMin_ab con profundidad {prof} y limite {limite_ab}")
    #print(nodo)

    if terminal(nodo):
        vmin = utilidad(nodo)
        #print("Se ha llegado a un nodo terminal")

    elif prof == limite_ab:
        vmin = heuristica(nodo)

        #print(nodo)
        #print(f"Se ha llegado al límite con valor de heurística {vmin}")

    else:
        i = 0
        while i < len(jugadas) and alfa < beta:
            jugada = jugadas[i]
            if esValida(nodo, jugada):
                intento = aplicaJugada(nodo, jugada, -1)
                beta = min(beta, valorMax_ab(intento, prof+1, alfa, beta, visitados))
                
            i += 1
        vmin = beta

        #if i < len(jugadas):
        #    print("Se ha podado")
    
    return vmin

def valorMax_ab(nodo: Nodo, prof: int, alfa: int, beta: int, visitados: list) -> int:
    visitados[0] += 1
    #print(f"Entra en valorMax_ab con profundidad {prof} y limite {limite_ab}")
    #print(nodo)

    if terminal(nodo):
        vmax = utilidad(nodo)
        #print("Se ha llegado a un nodo terminal")

    elif prof == limite_ab:
        vmax = heuristica(nodo)

        #print(f"Se ha llegado al límite con valor de heurística {vmax}")
        #print(nodo)

    else:
        i = 0
        while i < len(jugadas) and alfa < beta:
            jugada = jugadas[i]
            if esValida(nodo, jugada):
                intento = aplicaJugada(nodo, jugada, 1)
                alfa = max(alfa, valorMin_ab(intento, prof+1, alfa, beta, visitados))
            
            i += 1
        vmax = alfa

        #if(i < len(jugadas)):
        #    print("Se ha podado")
    
    return vmax