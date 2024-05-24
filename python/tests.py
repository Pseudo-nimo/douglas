from time import sleep 
from Spaces import *

TESTING = 0.01

# Mapa
INITIAL_POS =[0,0]
FINAL_POS = (7,7)
Gameloop = True

priority = 0

class Player():
    
    def __init__(self, board):
        
        self.world = board
        self.position = INITIAL_POS
        self.batery=[1,1,1,1]

        self._g,self._s,self._b=0,0,0

        self.rechargeList=[]
        self.obstacleList=[]
        self.timecount=0
        self.rootList=[]
        self.pathList=[]
        self.shadowList=[]
        self.mineralList=[]
        self.finalPathList=[]

    def recharge(self):
        self.rechargeList.append(self.position) 
        while len(self.batery)<5:
            self.batery.append(1)
            sleep(1 * TESTING)
            
            self.timecount+=1

    def register(self, results:Space):
        self.timecount+=2
        _p = self.position    
        if results.content ==  Content.GOLD:
            self.mineralList.append(['gold',results.Pos])
            self._g += 1
        if results.content ==  Content.SILVER:
            self.mineralList.append(['silver',results.Pos])
            self._s += 1
        if results.content ==  Content.BRONZE:
            self.mineralList.append(['bronze',results.Pos])
            self._b += 1
        
        if self.world.getSpace(*self.position).content == Content.RECHARGE_RESTRICTION:
            self.shadowList.append(self.position)

        if self.world.getSpace( _p[0]+1, _p[1]+1).content == Content.MOVE_RESTRICTION:
            self.obstacleList.append(self.position)

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
        
        if len(vizinhosDisponiveis)==2: self.rootList.append(self.position)

        _prioritySpace = vizinhosDisponiveis[priority]
            
        if (nextDiagonal.content != Content.MOVE_RESTRICTION): results= nextDiagonal
        
        #caso contrario faremos uma analise do menor cateto
        else:
            #self.obstacleList.append(nextDiagonal.Pos)
            _vDistance = self.world.end.Pos[1] - self.position[1]
            _hDistance = self.world.end.Pos[0] - self.position[0]

            if _hDistance < _vDistance: results= nextHorizontal   

            elif _hDistance > _vDistance: results = nextVertical

            if (_prioritySpace != Content.MOVE_RESTRICTION):
                results = _prioritySpace

            # ainda tenho que definir oq fazer na segunda tentativa


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

        # Recarga impossivel no proximo espaço
        shadowZone = results.content == Content.RECHARGE_RESTRICTION


        # Recarga
        if len(self.batery)==1 or (shadowZone and len(self.batery)<3): 
            
            self.recharge()

        self.register(results)
        self.position = results.Pos
        sleep(2 * TESTING)
        self.batery.pop()
        
def createCamp(campo):
    campo.createSpace(MoveRestriction(2,2))
    campo.createSpace(MoveRestriction(3,2))
    campo.createSpace(MoveRestriction(5,3))
    campo.createSpace(MoveRestriction(2,3))
    campo.createSpace(RechargeRestriction(6,3))
    campo.createSpace(RechargeRestriction(8,4))
    campo.createSpace(Gold(1,1))
    campo.createSpace(Silver(3,1))
    campo.createSpace(Silver(7,4))
    campo.createSpace(Bronze(4,2))
    campo.createSpace(Bronze(7,5))
    campo.createSpace(initialSpace(*INITIAL_POS))
    campo.createSpace(finalSpace(*FINAL_POS))
    
    campo.createSpace(MoveRestriction(6,3))
    campo.createSpace(MoveRestriction(7,3))
    ''' '''
    
    for line in range(9,-1, -1):
        for column in range(10):
            print(f'[{campo.matrix[column][line].content.value :^5}]', end = '')
        print()

if __name__ == '__main__':
    
    campo = Camp()
    robot = Player(campo)
    createCamp(campo)
    

    
    while Gameloop:
        
        try: 
            robot.pathList.append(robot.position)
            robot.move()
            robot.finalPathList.append(robot.position)
            
            
            
        except:
            print(robot.pathList)
            print(robot.finalPathList)
            print(robot.rootList)
            if priority == 1: priority=0
            else: priority=1
            robot.rootList.pop()
            for i in range(len(robot.finalPathList)-1,0,-1):
                if (i) > robot.finalPathList.index(robot.rootList[-1]):
                    robot.finalPathList.pop()
                    print('i:',robot.finalPathList)
            robot.position = robot.rootList[-1]
            
                    
        
        if robot.position == list(FINAL_POS):
            Gameloop = False


    for i in robot.obstacleList:
        print('obstacle_found '+str(i[0])+',',i[1])
    print(robot._g)
    print(robot._s)
    print(robot._b)
    print(robot.timecount)
    if robot.position == list(FINAL_POS):
        print('sucess')

#arquivos

nome_arquivo = 'path.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.pathList:
        arquivo.write(str(i[0])+','+str(i[1])+'\n')


nome_arquivo = 'fastest_path.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.finalPathList:
        arquivo.write(str(i[0])+','+str(i[1])+'\n')

nome_arquivo = 'charge_impossible.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.shadowList:
        arquivo.write(str(i[0])+','+str(i[1])+'\n')

nome_arquivo = 'gold.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.mineralList:
        if i[0]=='gold':
            arquivo.write(str(i[1][0])+','+str(i[1][1])+'\n')

nome_arquivo = 'silver.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.mineralList:
        if i[0]=='silver':
            arquivo.write(str(i[1][0])+','+str(i[1][1])+'\n')

nome_arquivo = 'bronze.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.mineralList:
        if i[0]=='bronze':
            arquivo.write(str(i[1][0])+','+str(i[1][1])+'\n')

nome_arquivo = 'charging.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.rechargeList:
        arquivo.write(str(i[0])+','+str(i[1])+'\n')

nome_arquivo = 'obstacles.txt'
with open(nome_arquivo, 'w') as arquivo:
    for i in robot.obstacleList:
        arquivo.write(str(i[0]+1)+','+str(i[1]+1)+'\n')

