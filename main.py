import math
import time

# Mapa
_initialPos = [0,0]
finalPos = [6,7]
_movementModes = [
    'Vazio','diagonal','vertical','horizontal'
]


class Space():
    r:int
    Pos:list
    def __init__(self, p: list):
        self.Pos = p
        self.r = 255

        pass
    

class initialSpace(Space):
    def __init__(self):
        self.r=99

class finalSpace(Space):
    def __init__(self):
        self.r=100

class MoveRestriction(Space):
    def __init__(self):
        self.r = 1
        


class Player():
    h: Space
    v: Space
    d: Space

    
    # 100% do código até agora foi escrito a mão


    def __init__(self, t):
        self.Pos = _initialPos
        self.tab = t

    def observarArredores(self):
        global d,  v, h
        d=tabuleiro[self.Pos[0]+1][self.Pos[1]+1]
        return 0

    def analysis(self)->list:
        
        #checar diagonal
        nextDirection=[0,0]
        self.observarArredores()
        checking = self.checarCatetos(self.Pos)

        if (checking > 2) : 
            # o robo deve checar se já está alinhado com o objetivo
            if checking == 3:
                if (self.h != 0):
                    nextDirection = [1,0]
                    pass
            elif checking == 1:
                if (self.v != 0):
                    nextDirection = [0,1]
                    pass

        if (self.d==0): 
            # o robo deve escolher andar pelo menor cateto

            print('d=0')

            if checking == 0:
                if (self.h != 0):
                    nextDirection = [1,0]
                    pass
                        
            elif checking == 1:
                if (self.v != 0):
                    nextDirection = [0,1]
                    pass
            
            elif checking == 2: 
                if (self.h != 0):
                    nextDirection = [1,0]
                    pass


        else:
            #se a diagonal nao estiver bloqueada, devemos andar por ela
            nextDirection = [1,1]
        return nextDirection
        

    def walk(self):
        time.sleep(2)
        self.Pos[0] += self.analysis[0] # type: ignore
        self.Pos[1] += self.analysis[1] # type: ignore
        
        return -1

    def checarCatetos(self, pos: list)-> int:
    
        hDistance = finalPos[0] - self.Pos[0]
        vDistance = finalPos[1] - self.Pos[1]

        if not (hDistance == 0 or vDistance == 0): 

            if   hDistance > vDistance:
                return 0
            elif hDistance < vDistance:
                return 1
            else: 
                return 2
        else: 
            if   hDistance == 0:
                return 3
            if   vDistance == 0:
                return 4
        return -1
            


            

if __name__ == '__main__':
    
    

    tabuleiro = [[Space([i,j]) for i in range(10)] for j in range(10)]

    tabuleiro[_initialPos[0]][_initialPos[1]] = initialSpace()
    tabuleiro[finalPos[0]][finalPos[1]] = finalSpace()
    robot = Player(tabuleiro)
    Gameloop = True

    for i in range(9,-1, -1):
        for j in range(10):
            #print(f'{tabuleiro[i][j].Pos}'+f' role: {tabuleiro[i][j].r}', end ='')
            print(f'[{tabuleiro[i][j].r:^5}]', end = '')

        print()

    '''
    while Gameloop:
        
        pass
'''