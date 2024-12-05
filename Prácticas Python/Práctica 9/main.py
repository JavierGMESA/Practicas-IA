from heuristica import *
from tictactoeAlum import *

ganador = 0
jugador = int(input("Introduzca el 1er jugador: 1 AI, 2 Tú "))

if jugador != 1:
    jugador = -1

juego = nodoInicial()
limiteMinimax = 3
while juego.vacias > 0 and not ganador:
    if jugador == 1:
        #juego = minimaxHeuristico(juego, limiteMinimax)
        juego = poda_ab(juego)
    else:
        juego = jugadaAdversario(juego)
    print(juego)
    if terminal(juego):
        ganador = utilidad(juego)
    jugador = opuesto(jugador)

# Duda: en el minimax heurístico la IA en algunos turnos donde tiene la victoria asegurada prefiere impedir que el jugador 
# contrario pueda ganar en su siguiente turno aunque el juego pueda acabarse en el turno actual con la IA siendo el ganador

match ganador:
    case 0:
        print("EMPATE")
    case 100:
        print("GANA MAX (IA)")
    case -100:
        print("GANA MIN (JUGADOR)")