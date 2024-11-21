#PROBLEMA DE LOS CANIBALES Y MISIONEROS

#Guardamos para cada orilla el número de misioneros y caníbales que hay
#Para la barca indicamos mediante una variable en que orilla está

#OPERADORES: mover la barca con 1 misionero, con 2 misiones, con 1 canibal, con 2 canibales, y con 1 misionero y 1 canibal 
#(tanto para la derecha como para la izquierda, aunque se puede hacer general mirando donde está la barca)

from dataclasses import dataclass
import numpy as np
import copy

@dataclass
class tEstado:
    Mi: int
    Md: int
    Ci: int
    Cd: int
    B: int      #Si es 1 está a la izquierda y si es 2 está a la derecha
    def tEstado(self, mi, md, ci, cd, b):
        self.Mi = mi
        self.Md = md
        self.Ci = ci
        self.Cd = cd
        self.B = b

OPERADORES = {
    "1": "M1",
    "2": "M2",
    "3": "C1",
    "4": "C2",
    "5": "M1C1"
    }

def estadoObjetivo() -> tEstado:
    return tEstado(3, 3, 0, 0, 1)

def iguales(e1: tEstado, e2: tEstado) -> bool:
    return (e1.Mi == e2.Mi and e1.Md == e2.Md and e1.Ci == e2.Ci and e1.Cd == e2.Cd and e1.B == e2.B)


def testObjetivo(estado: tEstado) -> bool:
    objetivo = estadoObjetivo()
    return iguales(estado, objetivo)


def esValido(op, estado: tEstado) -> bool:
    valido = True
    match OPERADORES[op]:
        case "M1":
            if(estado.B == 1):
                if(estado.Mi < 1):
                    valido = False
                else:
                    valido = estado.Mi - 1 >= estado.Ci
            else:
                if(estado.Md < 1):
                    valido = False
                else:
                    valido = estado.Md - 1 >= estado.Cd
                    

    return valido

