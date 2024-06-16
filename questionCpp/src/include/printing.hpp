#ifndef PRINTING_H
#define PRINTING_H

#include <vector>
#include <string>

#define EMPTY 255
#define OBSTACLES 0
#define CHARGE_IMPOSSIBLE 1
#define CHARGING_CODE 2
#define FINAL_SPACE 100
#define GOLD 191
#define SILVER 127
#define BRONZE 63


class Neighbor {
public:
    int data;
    int position[2];
};

void write_on_archive(const char *set_name, Neighbor data_list[], int size);
void remove_duplicates(Neighbor data_list[], int *size);
void create_archive(Neighbor data_list[], int size, int type) ;

#endif // PRINTING_HPP
