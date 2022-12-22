# https://www.acmicpc.net/problem/1996
n = int(input())
min_map = [input() for i in range(n)]
result_map = [['0']*n for _ in range(n)]
away = [-1,0,1]
for y in range(n):
    for x in range(n):
        if min_map[y][x] != '.':
            result_map[y][x] = '*'
        else:
            count = 0
            for i in away:
                for j in away:
                    if i == 0 and j == 0:
                        continue
                    elif y+i < 0 or y+i >= n:
                        continue
                    elif x+j < 0 or x+j >= n:
                        continue
                    elif min_map[y+i][x+j] != '.':
                        count += int(min_map[y+i][x+j])
            if len(str(count)) != 1:
                result_map[y][x] = 'M'
            else:
                result_map[y][x] = str(count)
for result in result_map:
    print(''.join(result))
