// battery.h

#ifndef BATTERY_H
#define BATTERY_H

#define MAX_SIZE 4


typedef struct {
    int top;
    int values[MAX_SIZE];
} Battery;

void init_battery(Battery *battery);
int is_empty(Battery *battery);
int is_full(Battery *battery);
void push(Battery *battery);
int pop(Battery *battery);
int percentage(Battery *Battery);

#endif
