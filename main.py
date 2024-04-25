import os
import math
import time

# Mapa
_initialPos = [0,0]
finalPos = [9,6]
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
    Pos: list
    # 100% do código até agora foi escrito a mão

    def __init__(self, t):
        self.Pos = _initialPos
        self.d=tabuleiro[self.Pos[0]+1][self.Pos[1]+1]
        self.h=tabuleiro[self.Pos[0]+1][self.Pos[1]]
        self.v=tabuleiro[self.Pos[0]][self.Pos[1]+1]
        
        self.tab = t



    def observarArredores(self):
        global d, v, h, Pos
        self.d=tabuleiro[self.Pos[0]+1][self.Pos[1]+1]
        self.h=tabuleiro[self.Pos[0]+1][self.Pos[1]]
        self.v=tabuleiro[self.Pos[0]][self.Pos[1]+1]
        return 0

    def analysis(self) -> list:
        global d, v, h
        #checar diagonal
        nextDirection = [-1,-1]
        self.observarArredores()
        checking = self.checarCatetos(self.Pos)
        '''
        if (checking > 2) : 
            # o robo deve checar se já está alinhado com o objetivo
            if checking == 3:
                if (self.h.r != 0):
                    nextDirection = [1,0]
                    pass
            elif checking == 4:
                if (self.v.r != 0):
                    nextDirection = [0,1]
                    pass
            if checking == 12:
                nextDirection = [0,0]
        '''

        if not (self.d.r == 255): 
            # o robo deve escolher andar pelo menor cateto

            print('nao pode diagonalizar', checking)

            if checking == 0:
                if (self.h.r != 0):
                    return [1,0]
                    
                        
            elif checking == 1:
                if (self.v.r != 0):
                    return [0,1]
                    
            
            elif checking == 2: 
                if (self.h.r != 0):
                    nextDirection = [1,0]
                    pass
            else: nextDirection=[0,0]
        else:
            #se a diagonal nao estiver bloqueada, devemos andar por ela
            nextDirection = [1,1]

        return nextDirection
        

    def walk(self):
        time.sleep(0.5)
        results = self.analysis()
        if self.Pos == finalPos:
            return 12
        elif (finalPos[0] - self.Pos[0]) == 0:
            self.Pos[1] = self.Pos[1] + 1
        elif (finalPos[1] - self.Pos[1]) == 0:
            self.Pos[0] = self.Pos[0] + 1
        else:
            self.Pos[0] = self.Pos[0] + results[0]
            self.Pos[1] = self.Pos[1] + results[1]
            
            
        return -1

    def checarCatetos(self, pos: list)-> int:
    
        hDistance = finalPos[0] - self.Pos[0]
        vDistance = finalPos[1] - self.Pos[1]


        if   hDistance > vDistance:
            return 0
        elif hDistance < vDistance:
            return 1
        else: 
            return 2
        return -1


if __name__ == '__main__':
    
    

    tabuleiro = [[Space([i,j]) for i in range(11)] for j in range(11)]

    tabuleiro[_initialPos[0]][_initialPos[1]] = initialSpace()
    tabuleiro[finalPos[0]][finalPos[1]] = finalSpace()
    robot = Player(tabuleiro)
    tabuleiro[1][1] = MoveRestriction()
    Gameloop = True

    for i in range(9,-1, -1):
        for j in range(10):
            #print(f'{tabuleiro[i][j].Pos}'+f' role: {tabuleiro[i][j].r}', end ='')
            print(f'[{tabuleiro[j][i].r:^5}]', end = '')

        print()

    
    while Gameloop:
        print(robot.Pos)
        if robot.walk() == 12:
            print('chegou')
            Gameloop=False
