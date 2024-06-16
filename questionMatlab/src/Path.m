classdef Path
    properties
        num_coords;
        path;
    end
    
    methods
        function obj = read_coordinates(obj)
            fileID = fopen('data/path.txt', 'r');
            lines = textscan(fileID, '%s', 'Delimiter', '\n');
            fclose(fileID);
            
            obj.num_coords = str2double(lines{1}{1});
            obj.path = Position.empty(obj.num_coords, 0);
             
            for i = 2:obj.num_coords + 1
                coordinates = str2double(strsplit(lines{1}{i}, ','));
                obj.path(i - 1) = Position(coordinates(1), coordinates(2));
            end
        end
        
        function next_pos = get_next_pos(obj, map_data, actual)
            obj = obj.read_coordinates();
            next_pos = [-1, -1];
            
            for i = 1:obj.num_coords - 1
                if obj.path(i).x == actual(1) && obj.path(i).y == actual(2)
                    next_pos(1) = obj.path(i + 1).x;
                    next_pos(2) = obj.path(i + 1).y;
                    return;
                end
            end
            
            disp('Error! Unable to find next position!');
        end
    end
end