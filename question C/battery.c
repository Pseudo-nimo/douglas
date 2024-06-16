#include "./include/battery.h"
#define MAX_SIZE 4

void init_battery(Battery *battery) {
    battery->top = -1;
}

int is_empty(Battery *battery) {
    return (battery->top == -1);
}

int is_full(Battery *battery) {
    return (battery->top == MAX_SIZE - 1);
}

void push(Battery *battery) {
    if (!is_full(battery)) {
        battery->top++;
        battery->values[battery->top] = battery->top;
    }
}

int pop(Battery *battery) {
    if (!is_empty(battery)) {
        int value = battery->values[battery->top];
        battery->top--;
        return value;
    }
    return -1; // Pilha vazia, retorna valor inválido
}


int percentage(Battery *battery) {
    // Calcular a porcentagem da bateria
    int current_level = (battery->top + 1) * 100 / MAX_SIZE;
    
    // Verificar se a bateria está abaixo de 50%
    return current_level;
}
