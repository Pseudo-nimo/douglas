#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "./navigation.c"
#include "./battery.c"
#include "./printing.c"

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
    printf("obstacle_found %d,%d\n", x, y);
}

int is_in_list(Neighbor list[], int size, int pos[]) {
    for (int i = 0; i < size; i++) {
        if (list[i].position[0] == pos[0] && list[i].position[1] == pos[1]) {
            return 1;
        }
    }
    return 0;
}

int main() {
    Battery battery;
    init_battery(&battery);
    for (int i = 0;i < 3; i++)push(&battery);
    
    int walking_time = 2;

    int **map_data = get_map();

    
    int actual[2] = {1, 1};
    int next_pos[2] = {-1, -1};

    // Inicialização das listas de minerais e restrições
    Neighbor mineralList[10]; // Assumindo um máximo de 100 entradas
    Neighbor restrictionList[10]; // Assumindo um máximo de 100 entradas
    Neighbor rechargeList[10];

    int mineralCount = 0;
    int restrictionCount = 0;
    int rechargeCount = 0;

    // Contadores de minerais
    int gold_count = 0;
    int silver_count = 0;
    int bronze_count = 0;

    for (int i = 0; i<8; i++) {

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
            !is_in_list(mineralList, mineralCount, actual)) {
            // Adicionar à lista de minerais
            mineralList[mineralCount] = (Neighbor){actual_path.data, {actual[0], actual[1]}};
            mineralCount++;
            if (actual_path.data == GOLD) {
                gold_count++;
            } else if (actual_path.data == SILVER) {
                silver_count++;
            } else if (actual_path.data == BRONZE) {
                bronze_count++;
            }
        }


        // Verificar a bateria e recarregar se necessário
        if ((next_pos_data == CHARGE_IMPOSSIBLE && percentage(&battery) <= 50 )|| percentage(&battery) <=25) {
            for (int i = 0;i < 4; i++) push(&battery);
            rechargeList[rechargeCount] = (Neighbor){CHARGING_CODE,{actual[0], actual[1]} };
            rechargeCount++;
            walking_time += 4;
  
        }

        // Remover item da bateria e aumentar tempo de caminhada
        if (!is_empty(&battery)) {
            pop(&battery); // Desempilhar 1 unidade
            walking_time += 2;
        }
       

        actual[0] = next_pos[0];
        actual[1] = next_pos[1];
    }

    // Verificar se alcançou o ponto final
    //int reached_final = ({8 - actual[1], actual[0]} == {7,6});

    // Exibir resultados finais
    printf("%d\n", gold_count);
    printf("%d\n", silver_count);
    printf("%d\n", bronze_count);
    printf("%d\n", walking_time);

    //printf("%s\n", reached_final ? "success" : "failure");

    // Arquivar os dados para cada tipo de mineral
    create_archive( mineralList, mineralCount, GOLD);
    create_archive( mineralList, mineralCount, SILVER);
    create_archive( mineralList, mineralCount, BRONZE);
    create_archive(restrictionList, restrictionCount, OBSTACLES);
    create_archive(restrictionList, restrictionCount, CHARGE_IMPOSSIBLE);
    create_archive(rechargeList, rechargeCount, CHARGING_CODE);

    return 0;
}
