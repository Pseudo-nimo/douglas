classdef Map
    properties
        sz_x;
        sz_y;
        map_data;
    end
    
    methods
        function obj = read_map_from_file(obj)
            fileID = fopen('data/map.txt', 'r');
            lines = textscan(fileID, '%s', 'Delimiter', '\n');
            fclose(fileID);
            
            dimensions = str2double(strsplit(lines{1}{1}));
            obj.sz_x = dimensions(1);
            obj.sz_y = dimensions(2);
            obj.map_data = zeros(obj.sz_y, obj.sz_x);
            
            for i = 2:obj.sz_x + 1
                row_data = str2double(strsplit(lines{1}{i}));
                obj.map_data(i - 1, 1:obj.sz_y) = row_data;
            end
        end
        
        function map_data = get_map(obj)
            obj = obj.read_map_from_file();
            map_data = obj.map_data;
        end
        
        function print_map(obj)
            obj = obj.read_map_from_file();
            disp(['Size X: ', num2str(obj.sz_x)]);
            disp(['Size Y: ', num2str(obj.sz_y)]);
            disp('Map Data:');
            disp(obj.map_data);
        end
    end
end
