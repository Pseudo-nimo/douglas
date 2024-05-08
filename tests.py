from time import sleep 
from Spaces import *

TESTING = 0

# Mapa
INITIAL_POS = (0,0)
FINAL_POS = (7,7)
Gameloop = True


class Player():
    def __init__(self, board):
        
        self.world = board
        self.position = INITIAL_POS
        self.batery=[1,1,1,1]
        self.branch_points = [] 
        self.vizinhosDisponiveis=[]

    def recharge(self):
        while len(self.batery)<5:
            self.batery.append(1)
            sleep(1* TESTING)

    def move(self):
        sleep(2 * TESTING)
        _p = self.position
        self.vizinhosDisponiveis=[]
        
        results:Space
        # a variavel results deve guardar as informações do espaço escolhido para ser o próximo

        
        self.diagonal = self.world.getSpace( _p[0]+1, _p[1]+1)
        self.horizontal = self.world.getSpace( _p[0]+1, _p[1])
        self.vertical= self.world.getSpace( _p[0], _p[1]+1)
        
        vizinho = [self.diagonal, self.horizontal, self.vertical]
        
        for v in vizinho:
            if v.content != Content.MOVE_RESTRICTION:
                self.vizinhosDisponiveis.append(v)
        campo.defineRoot(
            self.vizinhosDisponiveis[1],
            self.vizinhosDisponiveis[0],
            *self.position
                    )

            

        #caso o espaço diagonal esteja livre, ele será escolhido

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
        elif(FINAL_POS[1]-self.position[1])==0: results = self.horizontal 

        # Recarga impossivel no proximo espaço
        shadowZone = results.content == Content.RECHARGE_RESTRICTION

        if len(self.batery)==1 or (shadowZone and len(self.batery)<3):self.recharge()

        self.position = results.Pos
        self.batery.pop()


if __name__ == '__main__':
    
    campo = Camp()
    robot = Player(campo)
    
    campo.createSpace(MoveRestriction(2,2))
    campo.createSpace(MoveRestriction(3,2))
    campo.createSpace(MoveRestriction(5,3))
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
        robot.move()
        if(campo.getSpace(*robot.position).content == Content.GOLD):
            print('OUROOOOOOOOOOOOOOOOOOO')
        if(campo.getSpace(*robot.position).content == Content.SILVER):
            print('PRATAAAAAAAAAAAAAAAAAA')
        if(campo.getSpace(*robot.position).content == Content.BRONZE):
            print('BRONZEEEEEEEEEEEEEEEE')
            
            
            
        print(robot.position)
        if robot.position == list(FINAL_POS):
            print('chegou')
            for c in campo.rootList:
                print (c.key)
            Gameloop = False
