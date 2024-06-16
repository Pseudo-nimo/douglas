import robot_functions.navigation as nav
from enum import Enum

walkingtime=2
gameloop = True
myPath = ".//outputs//"

class Content(Enum):
    EMPTY = 255
    OBSTACLES = 0
    CHARGE_IMPOSSIBLE = 1
    FINAL_SPACE = 100
    GOLD = 191
    SILVER = 127
    BRONZE = 63
    CHARGING_CODE = 2

def createArchive(set, List):
    global nome_arquivo
    for _ in set:
        
        if _ == 191: nome_arquivo = myPath+"gold.txt"
        if _ == 127: nome_arquivo = myPath+"silver.txt"
        if _ == 63: nome_arquivo = myPath+"bronze.txt"
        if _ == 0: nome_arquivo = myPath+"obstacles.txt"
        if _ == 1: nome_arquivo = myPath+"charge_impossible.txt"
        if _ == 2: nome_arquivo = myPath+"charging.txt"
        with open(nome_arquivo, 'w') as arquivo:
            for i in List:
                if i[0]==_:
                    arquivo.write(str(i[1][0])+','+str(i[1][1])+'\n')
                    
class Space:
    def __init__(self,val: int,pos:list):
        self.position =pos
        self.value = val
        
        
if __name__ == "__main__":
    

    map_obj = nav.Map()
    map_data = map_obj.get_map()

    battery = [0]*3
    actual = [1, 1]
    next_pos = [-1, -1]
    
    path_obj = nav.Path()
    mineralList=[]
    restrictionList=[]
    chargingList=[]

 

    for i in range(8):

        next_pos = path_obj.get_next_pos(map_data, actual)

        if next_pos==[-1,-1]: break
        
        actual_path = Space(map_data[8-actual[1]][actual[0]], (actual[0], actual[1]))
        next_pos_data =    map_data[8-next_pos[1]][next_pos[0]]
        up_right_data =   Space(map_data[7-actual[1]][actual[0]+1], (actual[0]+1, actual[1]+1))
        up_data =         Space(map_data[7-actual[1]][actual[0]], (actual[0], actual[1]+1))
        right_data =      Space(map_data[8-actual[1]][actual[0]+1], (actual[0]+1, actual[1]+1))
        down_right_data = Space(map_data[9-actual[1]][actual[0]+1], (actual[0]+1, actual[1]-1))

        neighbors = [down_right_data,right_data,up_right_data, up_data ]    
        
        for _ in Content:

            #checar obstaculos(n can be 0 or 1)
            for n in neighbors:
                if n.value == _.value:
                    if [n.value, n.position] not in restrictionList:
                        restrictionList.append([n.value, n.position])
                        if (_.value == Content.OBSTACLES.value): print('obstacle_found: ', n.position[0],",",n.position[1],sep="")
 
            
            # checar minerios 
            if actual_path.value == _.value:
                if (_.value == Content.GOLD.value  or _.value == Content.SILVER.value or _.value == Content.BRONZE.value):
                    mineralList.append([actual_path.value, actual_path.position])

        if len(battery)<2 or (next_pos_data==Content.CHARGE_IMPOSSIBLE.value and len(battery)<3):
            chargingList.append([2, actual])
            while len(battery)<4:
                battery.append(1)
            walkingtime += 4

        battery.pop()
        walkingtime+=2 
        actual = next_pos
        
    
    print(len([a for a in mineralList if a[0] == Content.GOLD.value]))
    print(len([a for a in mineralList if a[0] == Content.SILVER.value]))
    print(len([a for a in mineralList if a[0] == Content.BRONZE.value]))
    print("sucess")
    print(walkingtime)

mineralSet = [191,127,63]
restrictionSet = [0,1]


createArchive(mineralSet,mineralList)
createArchive(restrictionSet,restrictionList)
createArchive([2],chargingList)
