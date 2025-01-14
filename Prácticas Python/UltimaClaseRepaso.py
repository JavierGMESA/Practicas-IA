


def esValida(nodo, jugada, jugador):
    valida = False
    if jugador == -1:
        fila, col = nodo.blancas[jugada.ficha]
        match jugada.mov:
            case "ARRIBA":
                if (fila > 0 and nodo.tablero[fila-1][col] == 0) or fila == 0:
                    valida = True
            case "IZQUIERDA":
                if col > 0 and nodo.tablero[fila][col-1] == 0:
                    valida = True
            #sigue
    else:
        fila, col = nodo.negras[jugada.ficha]
        #repite

def terminal(nodo):
    u = 0
    if nodo.negras[0][1] == nodo.negras[1][1] and nodo.negras[0][1] == 3:
        u = +100
    elif nodo.blancas[0][0] == nodo.blancas[1][0] and nodo.blancas[0][0] == -1:
        u = -100
    return u

def heuristica(nodo):
    u = 0
    u += nodo.negras[0][1] + nodo.negras[1][1]
    u -= 2 - nodo.blancas[0][0] + 2 - nodo.blancas[1][0]
    return u