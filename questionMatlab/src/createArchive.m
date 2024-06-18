function createArchive(set, List, myPath)
    if ~exist(myPath, 'dir')
        mkdir(myPath);
    end
    nome_arquivo = '';
    for k = 1:length(set)
        s = set(k);
        if isequal(s, Content.GOLD)
            nome_arquivo = fullfile(myPath, 'gold.txt');
        elseif isequal(s, Content.SILVER)
            nome_arquivo = fullfile(myPath, 'silver.txt');
        elseif isequal(s, Content.BRONZE)
            nome_arquivo = fullfile(myPath, 'bronze.txt');
        elseif isequal(s, Content.OBSTACLES)
            nome_arquivo = fullfile(myPath, 'obstacles.txt');
        elseif isequal(s, Content.CHARGE_IMPOSSIBLE)
            nome_arquivo = fullfile(myPath, 'charge_impossible.txt');
        elseif isequal(s, Content.CHARGING_CODE)
            nome_arquivo = fullfile(myPath, 'charging.txt');
        end
        
        fid = fopen(nome_arquivo, 'w');
        if fid == -1
            error('Failed to open file: %s', nome_arquivo);
        end
        for i = 1:length(List)
            if isequal(List{i}{1}, s)
                fprintf(fid, '%d,%d\n', List{i}{2}(1), List{i}{2}(2));
            end
        end
        fclose(fid);
    end
end
