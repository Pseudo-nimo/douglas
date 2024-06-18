% Main function
myPath = 'C://Users//20231engciv0049//Downloads//outputs//';
walkingtime = 2;
gameloop = true;

% Assuming nav is a MATLAB package or toolbox, and Map and Path are its classes
map_obj = Map();
map_data = map_obj.get_map();

battery = zeros(1, 3);
actual = [1, 1];
next_pos = [-1, -1];

path_obj = Path();
mineralList = {};
restrictionList = {};
chargingList = {};

for i = 1:8
    next_pos = path_obj.get_next_pos(map_data, actual);
    if isequal(next_pos, [-1, -1])
        break;
    end
    
    actual_path = Space(map_data(8-actual(2)+1, actual(1)), actual);
    next_pos_data = map_data(8-next_pos(2)+1, next_pos(1));
    up_right_data = Space(map_data(7-actual(2)+1, actual(1)+1), [actual(1)+1, actual(2)+1]);
    up_data = Space(map_data(7-actual(2)+1, actual(1)), [actual(1), actual(2)+1]);
    right_data = Space(map_data(8-actual(2)+1, actual(1)+1), [actual(1)+1, actual(2)+1]);
    down_right_data = Space(map_data(9-actual(2)+1, actual(1)+1), [actual(1)+1, actual(2)-1]);

    neighbors = {down_right_data, right_data, up_right_data, up_data};
    
    contentValues = [Content.EMPTY, Content.OBSTACLES, Content.CHARGE_IMPOSSIBLE, ...
        Content.FINAL_SPACE, Content.GOLD, Content.SILVER, Content.BRONZE, Content.CHARGING_CODE];
    
    
    for c = contentValues
        % Check obstacles
        for n = neighbors
            if n{1}.value == c
                if ~any(cellfun(@(x) isequal(x, {c, n{1}.position}), restrictionList))
                    restrictionList{end+1} = {c, n{1}.position};
                    if c == Content.OBSTACLES
                        fprintf('obstacle_found: %d,%d\n', n{1}.position(1), n{1}.position(2));
                    end
                end
            end
        end
        
        % Check minerals
        if actual_path.value == c
            if c == Content.GOLD || c == Content.SILVER || c == Content.BRONZE
                mineralList{end+1} = {c, actual_path.position};
            end
        end
    end
    
    if length(battery) < 2 || (next_pos_data == Content.CHARGE_IMPOSSIBLE && length(battery) < 3)
        chargingList{end+1} = {Content.CHARGING_CODE, actual};
        while length(battery) < 4
            battery(end+1) = 1;
        end
        walkingtime = walkingtime + 4;
    end
    
    battery(end) = [];
    walkingtime = walkingtime + 2;
    actual = next_pos;
end


disp(sum(cellfun(@(x) x{1} == Content.GOLD, mineralList)));
disp(sum(cellfun(@(x) x{1} == Content.SILVER, mineralList)));
disp(sum(cellfun(@(x) x{1} == Content.BRONZE, mineralList)));
disp('success');
disp(walkingtime);

mineralSet = [Content.GOLD, Content.SILVER, Content.BRONZE];
restrictionSet = [Content.OBSTACLES, Content.CHARGE_IMPOSSIBLE];

createArchive(mineralSet, mineralList, myPath);
createArchive(restrictionSet, restrictionList, myPath);
createArchive({Content.CHARGING_CODE}, chargingList, myPath);
