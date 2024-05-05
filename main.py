from time import sleep 

# Mapa
INITIAL_POS = [0,0]
FINAL_POS = [6,6]


Gameloop = True


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

    def __init__(self):
        
        self.tabuleiro= [[Space([column,line]) for line in range(11)] for column in range(11)]
        
    
    def createSpace(self,spaceType:Space):
        self.tabuleiro[spaceType.Pos[0]][spaceType.Pos[1]] = spaceType
        if spaceType.r == 100:
            self.end = spaceType

class initialSpace(Space):
    def __init__(self,pos):
        self.r=99
        self.Pos=pos

class finalSpace(Space):
    _t: int
    def __init__(self,p):
        self.r=100
        self.Pos=p

class MoveRestriction(Space):
    def __init__(self,pos):
        self.r = 1
        self.Pos=pos

class RechargeRestriction(Space):
    def __init__(self,pos):
        self.r = -1
        self.Pos=pos

class Player():
    horizontal: Space
    vertical: Space
    diagonal: Space
    Pos: list
    tab: Camp
    batery: int
    # 100% do código até agora foi escrito a mão

    def __init__(self, t):
        self.position = [0,0]
        self.tab = t
        self.batery = 4

    def recharge(self):
        while self.batery<5:
            print('recarregando: ', self.batery)
            self.batery+=1
            sleep(1)

    def move(self):

        sleep(1)
        results:Space
        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo

        self.diagonal=self.tab.tabuleiro[self.position[0]+1][self.position[1]+1]
        self.horizontal= self.tab.tabuleiro[self.position[0]+1][self.position[1]]
        self.vertical= self.tab.tabuleiro[self.position[0]][self.position[1]+1]
        
        '''print('D/V/H:', self.diagonaliagonal.Pos,'/',self.vertical.Pos,'/',self.horizontal.Pos)
        print('VD: ',vDistance)
        print('HD: ',hDistance)'''

        #se a diagonal nao estiver bloqueada, devemos andar por ela
        if (self.diagonal.r == 255): results= self.diagonal

        #caso contrario faremos uma analise do menor cateto
        else:
            vDistance = self.tab.end.Pos[1] - self.position[1]
            hDistance = self.tab.end.Pos[0] - self.position[0]

            if hDistance < vDistance:
                if (self.horizontal.r != 1):
                    results= self.horizontal
                else: raise Exception('erro na horizonta')
                            
            elif hDistance > vDistance:
                if (self.vertical.r != 1):
                    results= self.vertical
                else: raise Exception('erro na vertical')
                    
            else: 
                if (self.horizontal.r != 1):
                    results= self.horizontal
        
        # Cancela o movimento diagonal quando alinhar
        if (FINAL_POS[0]-self.position[0])==0:  results= self.vertical
        elif(FINAL_POS[1]-self.position[1])==0:results=self.horizontal 

        # Recarga impossivel no proximo espaço
        shadowZone = results.r == -1 

        if self.batery==1 or (shadowZone and self.batery<3):
            print('Recarga obrigatória')
            self.recharge()

        self.position = results.Pos
        self.batery-=1


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
            print(f'[{campo.tabuleiro[column][line].r:^5}]', end = '')
        print()

    
    while Gameloop:
        robot.move()
        print(robot.position)
        if robot.position == FINAL_POS:
            print('chegou')
            Gameloop=False
