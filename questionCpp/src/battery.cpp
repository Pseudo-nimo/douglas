#include "./include/battery.hpp"
#define MAX_SIZE 4

void Battery::init_battery() {
    (*this).top = -1;
}

bool Battery::is_empty() {
    return ((*this).top == -1);
}

bool Battery::is_full() {
    return ((*this).top == MAX_SIZE - 1);
}

void Battery::push() {
    if (!(*this).is_full()) {
        (*this).top++;
        (*this).values[(*this).top] = (*this).top;
    }
}

int Battery::pop() {
    if (!is_empty()) {
        int value = (*this).values[(*this).top];
        (*this).top--;
        return value;
    }
    return -1; // Pilha vazia, retorna valor inválido
}

int Battery::percentage() {
    // Calcular a porcentagem da bateria
    int current_level = ((*this).top + 1) * 100 / MAX_SIZE;
    
    // Verificar se a bateria está abaixo de 50%
    return current_level;
}
