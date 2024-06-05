class Map:
    def __init__(self):
        self.sz_x = 0
        self.sz_y = 0

    def read_map_from_file(self):
        with open("data/map.txt", "r") as file:
            lines = file.readlines()
            dimensions = lines[0].strip().split()
            self.sz_x = int(dimensions[0])
            self.sz_y = int(dimensions[1])
            self.map_data = [[0] * self.sz_x for _ in range(self.sz_y)]

            for i in range(1, self.sz_x + 1):
                row_data = list(map(int, lines[i].strip().split()))
                self.map_data[i - 1][:self.sz_y] = row_data


    def get_map(self):
        self.read_map_from_file()
        return self.map_data

    def print_map(self):
        self.read_map_from_file()
        print(f"Size X: {self.sz_x}")
        print(f"Size Y: {self.sz_y}")
        print("Map Data:")
        for i in range(self.sz_x):
            for j in range(self.sz_y):
                print(self.map_data[i][j], end=' ')
            print()

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Path:
    def __init__(self):
        self.num_coords = 0
        
    def read_coordinates(self):
        with open("data/path.txt", "r") as file:
            lines = file.readlines()
            self.num_coords = int(lines[0])
            self.path = [Position() for _ in range(self.num_coords)]

            for i in range(1, self.num_coords + 1):
                coordinates = lines[i].strip().split(',')
                self.path[i - 1].x = int(coordinates[0])
                self.path[i - 1].y = int(coordinates[1])

    def get_path_name(self):
        return 0
    def get_next_pos(self, map_data, actual):
        next_pos = [0, 0]

        self.read_coordinates()

        for i in range(self.num_coords - 1):
            if self.path[i].x == actual[0] and self.path[i].y == actual[1]:
                next_pos[0] = self.path[i + 1].x
                next_pos[1] = self.path[i + 1].y
                return next_pos

        print("Error! Unable to find next position!")
        next_pos[0] = -1
        next_pos[1] = -1
        return next_pos

if __name__ == "__main__":

    print("Navigation File From Robot Functions!")

