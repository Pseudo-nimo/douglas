import math

# Mapa
tabuleiro = list()

_initialPos = [0,0]

finalPos = [6,7]

_movementModes = [
    'Vazio','diagonal','vertical','horizontal'
]





class Player():
    h =1
    v =1
    d = 1
    def __init__(self):
        self.Pos = _initialPos

    def analisis(self)->list:

        #checar diagonal
        if (self.d==0): 
            # o robo deve escolher andar pelo menor cateto

            print('d=0')

            if self.checarCatetos(self.Pos) == 0:
                if (self.h != 0):
                    nextDirection = [1,0]
                    pass

            elif self.checarCatetos(self.Pos) == 1:
                if (self.h != 0):
                    nextDirection = [0,1]
                    pass
            
            else: 
                if (self.h != 0):
                    nextDirection = [1,0]
                    pass


        else:
            #se a diagonal nao estiver bloqueada, devemos andar por ela
            nextDirection = [1,1]
        return nextDirection

    def walk(self):
        self.Pos[0] += self.analisis[0] # type: ignore
        self.Pos[1] += self.analisis[1] # type: ignore
        
        pass

    def checarCatetos(self, pos: list):
    
        hDistance = finalPos[0] - pos[0]
        vDistance = finalPos[1] - pos[1]

        if hDistance>vDistance:
            return 0
        elif hDistance<vDistance:
            return 1
        else: return 2
        
            

if __name__ == '__main__':
    robot = Player()