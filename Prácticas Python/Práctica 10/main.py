from busqueda import *
from time import time

def opuesto(jugador) -> int:
    if jugador == 1:
        return -1
    else:
        return 1
    

ganador = 0
jugador = int(input("Introduzca el 1er jugador: 1 IA, 2 Tú "))

if jugador != 1:
    jugador = -1

juego = NodoInicial()
visitados = [0]
print(juego)
while not ganador: # Puede añadir si lo desea alguna condición adicional
    if jugador == 1:
        inicio = time()

        juego = minimax(juego, visitados)
        #juego = poda_ab(juego, visitados)
        
        fin = time()
        print(f"Ha tardado un total de {fin-inicio} segundos")
    else:
        juego = jugadaAdversario(juego)
    print(juego)
    if terminal(juego):
        ganador = utilidad(juego)
    jugador = opuesto(jugador)

print(f"Se han visitado {visitados[0]} nodos")

match ganador:
    case 0:
        print("EMPATE")
    case 100:
        print("GANA MAX (IA)")
    case -100:
        print("GANA MIN (JUGADOR)")
