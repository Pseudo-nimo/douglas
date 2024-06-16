#include <cstdio>
#include <cstdlib>
#include "./include/printing.hpp"

#define EMPTY 255
#define OBSTACLES 0
#define CHARGE_IMPOSSIBLE 1
#define CHARGING_CODE 2
#define FINAL_SPACE 100
#define GOLD 191
#define SILVER 127
#define BRONZE 63


void write_on_archive(const char *set_name, Neighbor data_list[], int size) {

    char nome_arquivo[200]; // Tamanho suficiente para armazenar o caminho completo do arquivo
    FILE *arquivo;

    // Construir o caminho completo do arquivo
    sprintf(nome_arquivo, "..//output//%s.txt", set_name);

    // Abrir o arquivo para escrita
    arquivo = fopen(nome_arquivo, "w");

    // Verificar se o arquivo foi aberto corretamente
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo %s\n", nome_arquivo);
        exit(1); // Sair do programa com erro
    }

    // Escrever os dados no arquivo
    for (int i = 0; i < size; i++) {
        if (data_list[i].data != -1) { // Verifica se o dado é válido
            fprintf(arquivo, "%d,%d\n", data_list[i].position[0], data_list[i].position[1]);
        }
    }

    // Fechar o arquivo
    fclose(arquivo);
}

void remove_duplicates(Neighbor data_list[], int *size) {
    for (int i = 0; i < *size; i++) {
        for (int j = i + 1; j < *size; j++) {
            if (data_list[i].position[0] == data_list[j].position[0] &&
                data_list[i].position[1] == data_list[j].position[1]) {
                // Shift left all elements after the duplicate
                for (int k = j; k < *size - 1; k++) {
                    data_list[k] = data_list[k + 1];
                }
                (*size)--;
                j--; // Recheck at the same position after shifting
            }
        }
    }
}

void create_archive(Neighbor data_list[], int size, int type) {
    char name[200]; // Nome do arquivo baseado no tipo de mineral

    switch (type) {
        case GOLD:
            sprintf(name, "gold");
            break;
        case SILVER:
            sprintf(name, "silver");
            break;
        case BRONZE:
            sprintf(name, "bronze");
            break;
        
        case OBSTACLES:
            sprintf(name, "obstacles");
            break;
        case CHARGE_IMPOSSIBLE:
            sprintf(name, "charge_impossible");
            break;
        case CHARGING_CODE:
            sprintf(name, "charging");
            break;
        
        default:
            return; // Caso o tipo de restrição não seja reconhecido, não cria arquivo
    }

    Neighbor filtered_list[100]; // Assumindo um máximo de 100 entradas para cada tipo de mineral
    int filtered_count = 0;

    // Filtrar dados para o tipo específico de mineral
    for (int i = 0; i < size; i++) {
        if (data_list[i].data == type) {
            filtered_list[filtered_count++] = data_list[i];
        }
    }

    // Remover duplicatas
    remove_duplicates(filtered_list, &filtered_count);

    // Chamar create_archive para criar o arquivo específico para o tipo de mineral
    write_on_archive(name, filtered_list, filtered_count);
}
