#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <cstring>

#include "./navigation.c"
#include "./battery.cpp"
#include "./printing.cpp"

// Definição dos valores correspondentes aos conteúdos do mapa
#define EMPTY 255
#define OBSTACLES 0
#define CHARGE_IMPOSSIBLE 1
#define CHARGING_CODE 2
#define FINAL_SPACE 100
#define GOLD 191
#define SILVER 127
#define BRONZE 63

void print_obstacle_found(int x, int y) {
    std::cout << "obstacle_found " << x << "," << y << std::endl;
}

bool is_in_list( Neighbor list[], int size, int pos[]) {
    for (int i = 0; i < size; i++) {
        if (list[i].position[0] == pos[0] && list[i].position[1] == pos[1]) {
            return true;
        }
    }
    return false;
}


int main() {
    Battery battery;
    battery.init_battery();
    for (int i = 0; i < 3; i++) battery.push();

    int walking_time = 2;

    int **map_data = get_map();

    int actual[2] = {1, 1};
    int next_pos[2] = {-1, -1};

    // Inicialização das listas de minerais e restrições
    Neighbor mineralList[50];
    Neighbor restrictionList[50];
    Neighbor rechargeList[50];

    int mineralCount = 0;
    int restrictionCount = 0;
    int rechargeCount = 0;

    // Contadores de minerais
    int gold_count = 0;
    int silver_count = 0;
    int bronze_count = 0;
    
    for (int i = 0; i < 8; i++) {
        
       get_next_pos(map_data, actual, next_pos);

        if (next_pos[0] == -1 && next_pos[1] == -1) break;

        Neighbor actual_path = {map_data[8 - actual[1]][actual[0]],{actual[0], actual[1]}};
        int next_pos_data = map_data[8 - next_pos[1]][next_pos[0]];
        Neighbor up_right_data = {map_data[7 - actual[1]][actual[0] + 1], {actual[0] + 1, actual[1] + 1}};
        Neighbor up_data = {map_data[7 - actual[1]][actual[0]], {actual[0], actual[1] + 1}};
        Neighbor right_data = {map_data[8 - actual[1]][actual[0] + 1], {actual[0] + 1, actual[1] + 1}};
        Neighbor down_right_data = {map_data[9 - actual[1]][actual[0] + 1], {actual[0] + 1, actual[1] - 1}};

        Neighbor neighbors[] = {down_right_data, right_data, up_right_data, up_data};

        // Checar obstáculos (0)
        for (int i = 0; i < 4; i++) {
            
            if ((neighbors[i].data == OBSTACLES || neighbors[i].data == CHARGE_IMPOSSIBLE) &&
                !is_in_list(restrictionList, restrictionCount, neighbors[i].position)) {
                restrictionList[restrictionCount] = neighbors[i];
                restrictionCount++;
                
                if (neighbors[i].data == OBSTACLES) {
                    print_obstacle_found(neighbors[i].position[0], neighbors[i].position[1]);
                }
            }
        }


        
        // Checar minérios (191, 127, 63)
        if ((actual_path.data == GOLD || actual_path.data == SILVER || actual_path.data == BRONZE) &&
            !is_in_list(mineralList, mineralCount,actual)) {
            mineralCount++;
            mineralList[mineralCount] = (actual_path);
            if (actual_path.data == GOLD) {
                gold_count++;
            } else if (actual_path.data == SILVER) {
                silver_count++;
            } else if (actual_path.data == BRONZE) {
                bronze_count++;
            }
        }

        // Verificar a bateria e recarregar se necessário
        if ((next_pos_data == CHARGE_IMPOSSIBLE && battery.percentage() <= 50) || battery.percentage() <= 25) {
            for (int i = 0; i < 4; i++) battery.push();
            rechargeCount++; 
            rechargeList[rechargeCount] = ((Neighbor){CHARGING_CODE, {actual[0], actual[1]}});
            walking_time += 4;
        }

        // Remover item da bateria e aumentar tempo de caminhada
        if (!battery.is_empty()) {
            battery.pop();
            walking_time += 2;
        }

        actual[0] = next_pos[0];
        actual[1] = next_pos[1];
    }

    std::cout << gold_count << std::endl;
    std::cout << silver_count << std::endl;
    std::cout << bronze_count << std::endl;
    std::cout << walking_time << std::endl;

    create_archive(mineralList,10,GOLD);
    create_archive(mineralList, 10,SILVER);
    create_archive(mineralList,10, BRONZE);
    create_archive(restrictionList,10, OBSTACLES);
    create_archive(restrictionList,10,CHARGE_IMPOSSIBLE);
    create_archive(rechargeList,rechargeCount, CHARGING_CODE);

    return 0;
}
