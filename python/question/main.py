import robot_functions.navigation as nav

if __name__ == "__main__":
    map_obj = nav.Map()
    map_data = map_obj.get_map()

    print("Map:")
    map_obj.print_map()

    actual = [1, 1]
    next_pos = [-1, -1]
    
    path_obj = nav.Path()
    paulino = nav.Map()

    paulino.print_map()
    next_pos = path_obj.get_next_pos(map_data, actual)
    path_name = path_obj.get_path_name(map_data, actual)

    if next_pos[0] != -1 and next_pos[1] != -1:
        print(f"Next Coordinate: ({next_pos[0]},{next_pos[1]})")