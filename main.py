from time import sleep 
from enum import Enum

# Mapa
INITIAL_POS = [0,0]
FINAL_POS = [6,6]
Gameloop = True

class Content(Enum):
    EMPTY = 255
    MOVE_RESTRICTION = 0
    RECHARGE_RESTRICTION = -1
    INITIAL_SPACE = 99
    FINAL_SPACE = 100
    GOLD = 191
    SILVER = 127
    BRONZE = 63



class Space():
    r:int
    Pos:list
    def __init__(self, p: list):
        self.Pos = p
        self.content = Content.EMPTY
        pass

class Camp():
    matrix:list 
    init: Space
    end: Space

    def __init__(self):
        
        self.matrix= [[Space([column,line]) for line in range(11)] for column in range(11)]
        
    
    def createSpace(self,spaceType:Space):
        self.matrix[spaceType.Pos[0]][spaceType.Pos[1]] = spaceType
        if spaceType.content == Content.FINAL_SPACE:
            self.end = spaceType

    def getSpacebyPosition(self,p):
        return self.matrix[p[0]][p[1]]

class initialSpace(Space):
    def __init__(self,pos):
        self.content=Content.INITIAL_SPACE
        self.Pos=pos

class finalSpace(Space):
    def __init__(self,p):
        self.content=Content.FINAL_SPACE
        self.Pos=p

class MoveRestriction(Space):
    def __init__(self,pos):
        self.content = Content.MOVE_RESTRICTION
        self.Pos=pos

class RechargeRestriction(Space):
    def __init__(self,pos):
        self.content = Content.RECHARGE_RESTRICTION
        self.Pos=pos

class Mineral(Space):
    def __init__(self,p):
        pass

class Gold(Mineral):
    def __init__(self, p):
        self.Pos=p
        self.content=Content.GOLD

class Silver(Mineral):
    def __init__(self, p):
        self.Pos=p
        self.content=Content.SILVER

class Player():

    def __init__(self, t):
        self.position = [0,0]
        self.world = t
        self.batery=[1,1,1,1]

    def recharge(self):
        while len(self.batery)<5:
            self.batery.append(1)
            sleep(1)

    def move(self):
        sleep(1)
        results:Space
        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo

        self.diagonal = self.world.matrix [self.position[0]+1] [self.position[1]+1]
        self.diagonal = self.world.getSpacebyPosition( [self.position[0]+1, self.position[1]+1])
        
        self.horizontal= self.world.matrix[self.position[0]+1][self.position[1]]

        self.vertical= self.world.matrix[self.position[0]][self.position[1]+1]
        
        #se a diagonal nao estiver bloqueada, devemos andar por ela
        if (self.diagonal.content != Content.MOVE_RESTRICTION): results= self.diagonal

        #caso contrario faremos uma analise do menor cateto
        else:
            _vDistance = self.world.end.Pos[1] - self.position[1]
            _hDistance = self.world.end.Pos[0] - self.position[0]

            if _hDistance < _vDistance:
                if (self.horizontal.content != Content.MOVE_RESTRICTION): 
                    results= self.horizontal
                else: raise Exception('erro na horizonta')
                            
            elif _hDistance > _vDistance:
                if (self.vertical.content != Content.MOVE_RESTRICTION): 
                    results = self.vertical
                else: raise Exception('erro na vertical')
                    
            else: 
                if (self.horizontal.content != Content.MOVE_RESTRICTION):
                    results= self.horizontal
        
        # Cancela o movimento diagonal quando alinhar
        if (FINAL_POS[0]-self.position[0])==0:  results = self.vertical
        elif(FINAL_POS[1]-self.position[1])==0: results=self.horizontal 

        # Recarga impossivel no proximo espaço
        shadowZone = results.content == Content.RECHARGE_RESTRICTION

        if len(self.batery)==1 or (shadowZone and len(self.batery)<3):self.recharge()

        self.position = results.Pos
        self.batery.pop()


if __name__ == '__main__':
    
    campo = Camp()
    robot = Player(campo)
    
    campo.createSpace(MoveRestriction([2,2]))
    campo.createSpace(MoveRestriction([3,2]))
    campo.createSpace(MoveRestriction([5,3]))
    campo.createSpace(RechargeRestriction([6,3]))
    campo.createSpace(initialSpace(INITIAL_POS))
    campo.createSpace(finalSpace(FINAL_POS))
    

    for line in range(9,-1, -1):
        for column in range(10):
            print(f'[{campo.matrix[column][line].content.value :^5}]', end = '')
        print()

    
    while Gameloop:
        robot.move()
        print(robot.position)
        if robot.position == FINAL_POS:
            print('chegou')
            Gameloop=False
