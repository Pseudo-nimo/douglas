import math



# Mapa
tabuleiro = list()

_initialPos = [0,0]

finalPos = [6,7]

_movementModes = [
    'Vazio','diagonal','vertical','horizontal'
]



class Space():
    r:int
    def __init__(self, p: list):
        self.Pos = p
        self.r: int
        pass
    def defineRole(self, r):
        self.role = r


class restriction(Space):
    def __init__(self, r):
        self.defineRole(r)
        
        


class Player():
    h: Space
    v: Space
    d: Space

    # 100% do código até agora foi escrito a mão


    def __init__(self):
        self.Pos = _initialPos

    def observarArredores(self):
        return 0

    def analysis(self)->list:

        #checar diagonal
        nextDirection=[0,0]
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
                        # cvggg
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
        self.Pos[0] += self.analysis[0] # type: ignore
        self.Pos[1] += self.analysis[1] # type: ignore
        
        return 0

    def checarCatetos(self, pos: list)-> int:
    
        hDistance = finalPos[0] - pos[0]
        vDistance = finalPos[1] - pos[1]

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
    robot = Player()
    Gameloop = True
    print('hello')
    while Gameloop:
        
        pass
