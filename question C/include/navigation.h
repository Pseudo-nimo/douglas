#ifndef NAVIGATION_H
#define NAVIGATION_H

int **get_map(void);
int get_next_pos(int **map_data, int *actual, int *next_pos);
void print_map(void);

#endif /* NAVIGATION_H */
