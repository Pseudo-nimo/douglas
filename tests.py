tab = [['0' for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        tab[i][j]=f'{i},{j}'

for j in range(9,-1,-1):
        for i in range(10):
            print(f'[{tab[i][j]:^5}]', end = '')
        print()