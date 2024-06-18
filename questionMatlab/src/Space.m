classdef Space
    properties
        position
        value
    end
    
    methods
        function obj = Space(val, pos)
            obj.value = val;
            obj.position = pos;
        end
    end
end
