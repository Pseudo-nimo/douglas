from enum import Enum
from operator import indexOf

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
    Pos:list
    def __init__(self, x,y):
        self.Pos = [x,y]
        self.content = Content.EMPTY
        self.name = 'free_2_go'

class Camp():
    matrix:list 
    init: Space
    end: Space

    def __init__(self):
        self.matrix= [[Space(*(column,line)) for line in range(11)] for column in range(11)]
        self.init = self.getSpace(0,0)

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
        self.name='free_2_go'

class MoveRestriction(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content = Content.MOVE_RESTRICTION
        self.name="obstacle"   

class RechargeRestriction(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content = Content.RECHARGE_RESTRICTION
        self.name="charging_impossible"

class Gold(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.GOLD
        self.name="gold"

class Silver(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.SILVER
        self.name="silver"


class Bronze(Space):
    def __init__(self, x,y):
        self.Pos=[x,y]
        self.content=Content.BRONZE
        self.name="bronze"

