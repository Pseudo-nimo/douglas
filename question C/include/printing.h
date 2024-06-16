typedef struct {
    int data;
    int position[2];
} Neighbor;

void write_on_archive(const char *set_name, Neighbor data_list[], int size) ;

void remove_duplicates(Neighbor data_list[], int *size) ;

void create_archive(Neighbor data_list[], int size, int mineral_type) ;

