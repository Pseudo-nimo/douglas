from time import sleep 

# Mapa
_initialPos = [0,0]
finalPos = [7,6]


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
        while self.batery<5:
            print('recarregando: ', self.batery)
            self.batery+=1
            sleep(1)

    def analysis(self):
        global Pos
        print('atual: ', self.Pos)
        self.d=self.tab.tabuleiro[self.Pos[0]+1][self.Pos[1]+1]
        self.h= self.tab.tabuleiro[self.Pos[0]+1][self.Pos[1]]
        self.v= self.tab.tabuleiro[self.Pos[0]][self.Pos[1]+1]
        
        print('D/V/H:',
              self.d.Pos,'/'
              ,self.v.Pos,'/'
              ,self.h.Pos)
        vDistance = self.tab.end.Pos[1] - self.Pos[1]
        hDistance = self.tab.end.Pos[0] - self.Pos[0]

        print('VD: ',vDistance)
        print('HD: ',hDistance)

        if (self.d.r == 255):
            #se a diagonal nao estiver bloqueada, devemos andar por ela
            return self.d
        else:
            #Caso contrario devemos analisar o menor cateto
            if hDistance < vDistance:
                print(self.h.Pos)
                if (self.h.r != 1):
                    return self.h
                else: raise Exception('erro na horizonta')
                            
            elif hDistance > vDistance:
                if (self.v.r != 1):
                    return self.v
                else: raise Exception('erro na vertical')
                    
            else: 
                if (self.h.r != 1):
                    return self.h
        
        return Space([0,0])

    def walk(self):
        sleep(1)
        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo
        results = self.analysis()
        
        # Recarga impossivel no proximo espaço
        shadowZone = self.tab.tabuleiro[results.Pos[0]][results.Pos[1]].r == -1 

        if self.batery==1 or shadowZone:
            self.recharge()

        # Cancela o movimento diagonal quando alinhar
        if (finalPos[0] - self.Pos[0]) == 0:  
            if self.tab.tabuleiro[self.Pos[0]][self.Pos[1]+1].r == -1:
                self.recharge()
            self.Pos[1] = self.Pos[1] + 1
        elif (finalPos[1] - self.Pos[1]) == 0: 
            if self.tab.tabuleiro[self.Pos[0] + 1][self.Pos[1]].r == -1: 
                self.recharge()
            self.Pos[0] = self.Pos[0] + 1        
        
        else:
            self.Pos = results.Pos
        self.batery-=1


if __name__ == '__main__':
    
    campo = Camp(_initialPos, finalPos)

    robot = Player(campo)
    campo.tabuleiro[2][2] = MoveRestriction([2,2])
    campo.tabuleiro[2][3] = MoveRestriction([2,3])
    campo.tabuleiro[9][8] = RechargeRestriction([9,8])
    Gameloop = True

    for i in range(9,-1, -1):
        for j in range(10):
            print(f'[{campo.tabuleiro[i][j].r:^5}]', end = '')
        print()

    
    while Gameloop:
        robot.walk()
        print(robot.Pos)
        if robot.Pos == finalPos:
            print('chegou')
            Gameloop=False
