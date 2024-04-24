import math

# Mapa
tabuleiro = list()

_initialPos = (0,0)

finalPos = (6,7)

_movementModes = [
    'Vazio','diagonal','vertical','horizontal'
]

class Player():
    h =1
    v =1
    d = 1
    def __init__(self):
        self.Pos = _initialPos
    def analisis(self):
        #checar diagonal
        if (self.d==0): 
            # o robo deve escolher andar pelo menor cateto
            pass
        else:
            nextDirection = (1,1)
        return nextDirection

    def walk(self):
        self.Pos[0] += self.analisis[0]
        self.Pos[1] += self.analisis[1]
        
        pass
        
            

if __name__ == '__main__':
    robot = Player()