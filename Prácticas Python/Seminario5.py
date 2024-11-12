#PROBLEMA DE LOS LADRONES Y LA CINTA AUTOMÁTICA

from dataclasses import dataclass
import copy

@dataclass  
class tEstado:

    def __init__(self, cinta):
        self.cinta = cinta
        self.L = 0
        self.B = 0

    def __repr__(self):
        return f"{self.cinta} \nL = {self.L}\nC = {self.B}"
    
    def esValido(move, estado):
        valido = False
        valido = (len(estado.cinta) != 0)
        return valido
    
    def aplicaOperador(move, estado):
        nuevo = copy.deepcopy(estado)
        match move:
            case "IZQUIERDA":
                nuevo.L += nuevo.cinta.pop(0)
            case "DERECHA":
                nuevo.L += nuevo.cinta.pop()
            
        if(len(nuevo.cinta) > 0):
            nuevo.B += estado.cinta.pop()
        
        return nuevo

    def test_objetivo(estado):
        return (len(estado.cinta) == 0 and estado.L >= estado.B)
    
abiertos: list
cerrados: list
NUM_OPERADORES: list
abiertos = []
cerrados = []
NUM_OPERADORES = ["IZQUIERDA", "DERECHA"]

def expandir(actual):
    Sucesores: list
    Sucesores = []
    for op in NUM_OPERADORES:
        if(tEstado.esValido(op, actual)):
            nuevo = tEstado.aplicaOperador(op, actual)
            Sucesores.append(nuevo)
    return Sucesores 


Inicial = tEstado([4, 3, 2, 5, 7, 1, 8, 6])
abiertos.append(Inicial)
while(len(abiertos) != 0 and not (tEstado.test_objetivo(abiertos[0]))):
    Actual = abiertos.pop(0)
    Sucesores = expandir(Actual)
    abiertos += Sucesores

if(len(abiertos) == 0):
    print("Ninguna solución")
else:
    print(abiertos[0])



        



