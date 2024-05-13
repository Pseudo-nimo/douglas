
from time import sleep 
from Spaces import *

TESTING = 0.1

# Mapa
INITIAL_POS = (0,0)
FINAL_POS = (7,7)
Gameloop = True

priority = 0


class Player():

    def __init__(self, board):
        
        self.world = board
        self.position = INITIAL_POS
        self.batery=[1,1,1,1]

        self.endPrompt=[]
        self.mineralLogs=[]
        self.goldLogs:list
        self.silverLogs:list
        self.bronzeLogs=[]
        self.timecount=0

    def recharge(self):
        while len(self.batery)<5:
            self.batery.append(1)
            sleep(1 * TESTING)
            self.timecount+=1

    def move(self):
        
        _p = self.position
        vizinhosDisponiveis=[]
        results:Space

        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo
        nextDiagonal = self.world.getSpace( _p[0]+1, _p[1]+1)
        nextHorizontal = self.world.getSpace( _p[0]+1, _p[1])
        nextVertical= self.world.getSpace( _p[0], _p[1]+1)
        
        vizinho = [nextDiagonal, nextHorizontal, nextVertical]
        
        vizinhosDisponiveis = [a for a in vizinho if a.content != Content.MOVE_RESTRICTION ]
        
        if len(vizinhosDisponiveis)==2: rootList.append(self.position)

        prio = vizinhosDisponiveis[priority]
            
        if (nextDiagonal.content != Content.MOVE_RESTRICTION): results= nextDiagonal
        #caso contrario faremos uma analise do menor cateto

        else:
            _vDistance = self.world.end.Pos[1] - self.position[1]
            _hDistance = self.world.end.Pos[0] - self.position[0]

            if _hDistance < _vDistance: results= nextHorizontal     
            elif _hDistance > _vDistance: results = nextVertical
            if (prio != Content.MOVE_RESTRICTION):
                results = prio
        
        # Cancela o movimento nextDiagonal quando alinhar
        if (FINAL_POS[0]-self.position[0])==0: results = nextVertical
            
        elif(FINAL_POS[1]-self.position[1])==0: results = nextVertical
        
        #Tratamento de erro
        if results == nextVertical:
            if (nextVertical.content != Content.MOVE_RESTRICTION): 
                results = nextVertical
            else: raise Exception('erro na vertical')

        elif results == nextHorizontal:
            if (nextHorizontal.content != Content.MOVE_RESTRICTION): 
                results = nextHorizontal
            else: raise Exception('erro na horizontal')

                
        if (    
                results.content == (Content.GOLD) or 
                results.content == Content.SILVER or 
                results.content == Content.BRONZE 
            ): 
            self.mineralLogs.append([results.name, self.position])


        # Recarga impossivel no proximo espaço
        shadowZone = results.content == Content.RECHARGE_RESTRICTION

        if len(self.batery)==1 or (shadowZone and len(self.batery)<3):self.recharge()

        self.position = results.Pos
        sleep(2 * TESTING)
        self.batery.pop()
        self.timecount += 2


if __name__ == '__main__':
    
    campo = Camp()
    robot = Player(campo)
    
    campo.createSpace(MoveRestriction(2,2))
    campo.createSpace(MoveRestriction(3,2))
    campo.createSpace(MoveRestriction(5,3))
    campo.createSpace(MoveRestriction(6,3))
    campo.createSpace(MoveRestriction(7,3))
    campo.createSpace(MoveRestriction(2,3))
    campo.createSpace(RechargeRestriction(6,3))
    campo.createSpace(Gold(1,1))
    campo.createSpace(Silver(3,1))
    campo.createSpace(Silver(7,4))
    campo.createSpace(Bronze(4,2))
    campo.createSpace(Bronze(7,5))
    campo.createSpace(initialSpace(*INITIAL_POS))
    campo.createSpace(finalSpace(*FINAL_POS))
    
    for line in range(9,-1, -1):
        for column in range(10):
            print(f'[{campo.matrix[column][line].content.value :^5}]', end = '')
        print()

    
    while Gameloop:
        try: 
            robot.move()
            
        except:
            if priority == 1: priority=0
            else: priority=1
            rootList.pop()
            robot.position = rootList[-1]
        
        if robot.position == list(FINAL_POS):
            print('chegou')
            Gameloop = False
    print(robot.mineralLogs)
            #[print(rootList[i], end='/') for i in range(len(rootList))]


nome_arquivo = 'meuarquivo.txt'
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo de escrita em arquivo em Python.\n')
print(f'O arquivo {nome_arquivo} foi criado com sucesso.')
