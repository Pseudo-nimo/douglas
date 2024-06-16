#ifndef BATTERY_HPP
#define BATTERY_HPP

#define MAX_SIZE 4

class Battery {
     
public:
    int top;
    int values[MAX_SIZE];
    void init_battery();
    bool is_empty();
    bool is_full();
    void push();
    int pop();
    int percentage();
};


/*
struct Battery {
    int top;
    int values[MAX_SIZE];
};

// Funções para manipulação da bateria
void init_battery(Battery *battery);
bool is_empty(Battery *battery);
bool is_full(Battery *battery);
void push(Battery *battery);
int pop(Battery *battery);
int percentage(Battery *battery);*/

#endif // BATTERY_H
