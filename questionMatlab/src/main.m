map_obj = Map();
map_data = map_obj.get_map();

disp('Map:');
map_obj.print_map();

actual = [1, 1];
next_pos = [-1, -1];

path_obj = Path();
next_pos = path_obj.get_next_pos(map_data, actual);

if next_pos(1) ~= -1 && next_pos(2) ~= -1
    disp(['Next Coordinate: (', num2str(next_pos(1)), ',', num2str(next_pos(2)), ')']);
end
