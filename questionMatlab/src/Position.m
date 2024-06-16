classdef Position
    properties
        x = 0;
        y = 0;
    end
    
    methods
        function obj = Position(x, y)
            if nargin > 0
                obj.x = x;
            end
            if nargin > 1
                obj.y = y;
            end
        end
    end
end