
from time import sleep 
from Spaces import *

TESTING = 0.1

# Mapa
INITIAL_POS = (0,0)
FINAL_POS = (7,7)
Gameloop = True
rootList=[]
priority = 'right'




class Player():
    def __init__(self, board):
        
        self.world = board
        self.position = INITIAL_POS
        self.batery=[1,1,1,1]

    def recharge(self):
        while len(self.batery)<5:
            self.batery.append(1)
            sleep(1 * TESTING)

    def move(self):
        sleep(2 * TESTING)
        _p = self.position
        vizinhosDisponiveis=[]
        results:Space

        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo
        self.diagonal = self.world.getSpace( _p[0]+1, _p[1]+1)
        self.horizontal = self.world.getSpace( _p[0]+1, _p[1])
        self.vertical= self.world.getSpace( _p[0], _p[1]+1)
        
        vizinho = [self.diagonal, self.horizontal, self.vertical]
        
        vizinhosDisponiveis = [a for a in vizinho if a.content != Content.MOVE_RESTRICTION ]
        
        if len(vizinhosDisponiveis)==2:
            #print(f'Salvando o ponto {self.position} como bifurcação')
            print(vizinhosDisponiveis)
            rootList.append(self.position)

        if priority == 'right':
            prio = vizinhosDisponiveis[0]
        else:
            prio = vizinhosDisponiveis[1]
            
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
               
            
            if (prio != Content.MOVE_RESTRICTION):
                results= prio
        
        # Cancela o movimento diagonal quando alinhar
        if (FINAL_POS[0]-self.position[0])==0:  
            if (self.vertical.content != Content.MOVE_RESTRICTION): 
                    results = self.vertical
            else: raise Exception('erro na vertical')
        elif(FINAL_POS[1]-self.position[1])==0: 
            if (self.vertical.content != Content.MOVE_RESTRICTION): 
                results = self.vertical
            else: raise Exception('erro na vertical')
                
                
        if(campo.getSpace(*robot.position).content == Content.GOLD):
                print('OUROOOOOOOOOOOOOOOOOOO')
        if(campo.getSpace(*robot.position).content == Content.SILVER):
                print('PRATAAAAAAAAAAAAAAAAAA')
        if(campo.getSpace(*robot.position).content == Content.BRONZE):
                print('BRONZEEEEEEEEEEEEEEEE')

        # Recarga impossivel no proximo espaço
        shadowZone = results.content == Content.RECHARGE_RESTRICTION

        if len(self.batery)==1 or (shadowZone and len(self.batery)<3):self.recharge()

        self.position = results.Pos
        self.batery.pop()

root: Space

if __name__ == '__main__':
    
    campo = Camp()
    robot = Player(campo)
    
    campo.createSpace(MoveRestriction(2,2))
    campo.createSpace(MoveRestriction(3,2))
    campo.createSpace(MoveRestriction(5,3))
    campo.createSpace(MoveRestriction(6,3))
    campo.createSpace(MoveRestriction(7,3))
    campo.createSpace(MoveRestriction(2,3))
    #campo.createSpace(RechargeRestriction(6,3))
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
            if priority == 'left': priority='right'
            else: priority='left'
            rootList.pop()
            robot.position = rootList[-1]
        
        if(campo.getSpace(*robot.position).content == Content.GOLD):
                print('OUROOOOOOOOOOOOOOOOOOO')
        if(campo.getSpace(*robot.position).content == Content.SILVER):
                print('PRATAAAAAAAAAAAAAAAAAA')
        if(campo.getSpace(*robot.position).content == Content.BRONZE):
                print('BRONZEEEEEEEEEEEEEEEE')
        print(robot.position)
        
        if robot.position == list(FINAL_POS):
            print('chegou')
            Gameloop = False
            [print(rootList[i], end='/') for i in range(len(rootList))]


nome_arquivo = 'meuarquivo.txt'
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo de escrita em arquivo em Python.\n')
print(f'O arquivo {nome_arquivo} foi criado com sucesso.')
