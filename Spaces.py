from enum import Enum

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
    def __init__(self, x,y):
        self.Pos = [x,y]
        self.content = Content.EMPTY
        pass

class Camp():
    matrix:list 
    init: Space
    end: Space

    def __init__(self):
        self.matrix= [[Space(*(column,line)) for line in range(11)] for column in range(11)]
        
    def createSpace(self,spaceType:Space):
        self.matrix[spaceType.Pos[0]][spaceType.Pos[1]] = spaceType
        if spaceType.content == Content.FINAL_SPACE:
            self.end = spaceType
        
            

    def getSpace(self,x,y)->Space:
        return self.matrix[x][y]

class initialSpace(Space):
    def __init__(self,x,y):
        self.Pos=[x,y]
        self.content=Content.INITIAL_SPACE
        

class finalSpace(Space):
    def __init__(self, x,y):
        self.content=Content.FINAL_SPACE
        self.Pos= [x,y]

class MoveRestriction(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content = Content.MOVE_RESTRICTION
        

class RechargeRestriction(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content = Content.RECHARGE_RESTRICTION


class Gold(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.GOLD
        

class Silver(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.SILVER

class Bronze(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.BRONZE