#ifndef PRINTING_H
#define PRINTING_H

#include <vector>
#include <string>
#include <iostream>

#define EMPTY 255
#define OBSTACLES 0
#define CHARGE_IMPOSSIBLE 1
#define CHARGING_CODE 2
#define FINAL_SPACE 100
#define GOLD 191
#define SILVER 127
#define BRONZE 63

class Space {
public:
    Space(int data,int posit[2]);
    int data; 
    int position[2];

};



void write_on_archive(std::string name,std::vector<Space> data_list, int size);
void remove_duplicates(std::vector<Space> data_list, int size);
void create_archive(std::vector<Space> data_list, int size) ;

#endif // PRINTING_HPP
