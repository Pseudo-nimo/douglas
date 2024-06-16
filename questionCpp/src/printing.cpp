#include <iostream>
#include <fstream>
#include "./include/printing.hpp"

#define EMPTY 255
#define OBSTACLES 0
#define CHARGE_IMPOSSIBLE 1
#define CHARGING_CODE 2
#define FINAL_SPACE 100
#define GOLD 191
#define SILVER 127
#define BRONZE 63

Space::Space(int data, int posit[2]) {
    this->data = data;
    this->position[0] = posit[0];
    this->position[1] = posit[1];
}

void write_on_archive(std::string name, std::vector<Space> data_list) {

    std::string nome_arquivo; // Tamanho suficiente para armazenar o caminho completo do arquivo
    // Construir o caminho completo do arquivo
    nome_arquivo = "..//output//"+name+".txt";

    // Abrir o arquivo para escrita
    std::ofstream arquivo(nome_arquivo);

    // Verificar se o arquivo foi aberto corretamente
    if (!arquivo.is_open()) {
        std::cout<< "Erro ao abrir o arquivo \n"<< nome_arquivo<<std::endl;
        exit(1); // Sair do programa com erro
    }

    // Escrever os dados no arquivo
    for (int i = 0; i < data_list.size(); i++) {
        if (data_list[i].data != -1) { // Verifica se o dado é válido
            
            arquivo << data_list[i].position[0]<<","<< data_list[i].position[1] << '\n';
        }
    }

    // Fechar o arquivo
    
    arquivo.close();
}

void create_archive(std::vector<Space> data_list, int type) {
    std::string name; // Nome do arquivo baseado no tipo de mineral
    
    switch (type) {
        case GOLD:
            name= "gold";
            break;
        case SILVER:
            name= "silver";
            break;
        case BRONZE:
            name= "bronze";
            break;
        case OBSTACLES:
            name= "obstacles";
            break;
        case CHARGE_IMPOSSIBLE:
            name= "charge_impossible";
            break;
        case CHARGING_CODE:
            name= "charging";
            break;
        
        default:
            return; // Caso o tipo de restrição não seja reconhecido, não cria arquivo
    }
    std::vector<Space>  filtered_list; // Assumindo um máximo de 100 entradas para cada tipo de mineral

    // Filtrar dados para o tipo específico de mineral
    for (int i = 0; i < data_list.size(); i++) {
        if (data_list[i].data == type) {
            filtered_list.push_back(data_list[i]);
        }
    }

    // Remover duplicatas
    //remove_duplicates(data_list, 10);

    // Chamar create_archive para criar o arquivo específico para o tipo de mineral
    write_on_archive(name, filtered_list );
}
