from time import sleep 

# Mapa
_initialPos = [0,0]
finalPos = [9,1]
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

class Camp():
    tabuleiro:list 
    init: Space
    end: Space

    def __init__(self, i:list, e):
        
        self.tabuleiro= [[Space([i,j]) for i in range(11)] for j in range(11)]
        self.init= Space(i)
        self.end=Space(e)
        
        self.tabuleiro[self.end.Pos[0]][self.end.Pos[1]] = finalSpace()
        self.tabuleiro[self.init.Pos[0]][self.init.Pos[1]] = initialSpace()
        self.tabuleiro[self.init.Pos[0]][self.init.Pos[1]]
        

class initialSpace(Space):
    def __init__(self):
        self.r=99

class finalSpace(Space):
    def __init__(self):
        self.r=100

class MoveRestriction(Space):
    def __init__(self,p):
        self.r = 1
        self.Pos=p

class RechargeRestriction(Space):
    def __init__(self,p):
        self.r = -1
        self.Pos=p


class Player():
    h: Space
    v: Space
    d: Space
    Pos: list
    tab: Camp
    batery: int
    # 100% do código até agora foi escrito a mão

    def __init__(self, t):
        self.Pos = _initialPos
        self.tab = t
        self.batery = 4

    def recharge(self):
        for i in range (4):
            print('recarregando: ', self.batery)
            self.batery+=1
            sleep(1)


    def observarArredores(self):
        global d, v, h, Pos, tab
        self.d=self.tab.tabuleiro[self.Pos[0]+1][self.Pos[1]+1]
        self.h= self.tab.tabuleiro[self.Pos[0]+1][self.Pos[1]]
        self.v= self.tab.tabuleiro[self.Pos[0]][self.Pos[1]+1]
        return 0

    def analysis(self):
        global d, v, h

        #checar diagonal
        
        self.observarArredores()

        vDistance = self.tab.end.Pos[1] - self.Pos[1]
        hDistance = self.tab.end.Pos[0] - self.Pos[0]

        if not (self.d.r == 255): 
            if hDistance > vDistance:
                if (self.h.r != 0):
                    return self.h
                            
            elif hDistance < vDistance:
                if (self.v.r != 0):
                    return self.v
                    
            else: 
                if (self.h.r != 0):
                    return self.h
                   
        else:
            #se a diagonal nao estiver bloqueada, devemos andar por ela
            return self.d
        return Space([0,0])

    def walk(self):
        global d, h, v
        
        sleep(0.5)

        results:Space
        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo
        results = self.analysis()
        
        # Recarga impossivel no proximo espaço
        shadowZone = self.tab.tabuleiro[results.Pos[0]][results.Pos[1]].r == -1 # and self.batery<3
        if self.batery==1 or shadowZone:
            self.recharge()
            return 0
        
        if (finalPos[0] - self.Pos[0]) == 0:
            self.Pos[1] = self.Pos[1] + 1
        elif (finalPos[1] - self.Pos[1]) == 0:
            self.Pos[0] = self.Pos[0] + 1
        else:
            self.Pos = results.Pos
        self.batery-=1
        print(robot.Pos)
        return 0


if __name__ == '__main__':
    
    campo = Camp(_initialPos, finalPos)

    robot = Player(campo)
    campo.tabuleiro[1][1] = MoveRestriction([1,1])
    campo.tabuleiro[1][2] = MoveRestriction([1,2])
    campo.tabuleiro[6][1] = RechargeRestriction([6,1])
    Gameloop = True

    for i in range(9,-1, -1):
        for j in range(10):
            print(f'[{campo.tabuleiro[j][i].r:^5}]', end = '')
        print()

    
    while Gameloop:
        robot.walk()
        
        if robot.Pos == finalPos:
            print('chegou')
            Gameloop=False
