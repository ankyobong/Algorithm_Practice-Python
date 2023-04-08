# https://www.acmicpc.net/problem/2029
matches = list()
a = 0
b = 0
for _ in range(10):
    matches.append(input())
for i in [0, 3, 6, 9]:
    for j in [1, 4, 7]:
        if matches[i][j] == '.':
            a += 1
        if i == 9:
            pass
        elif matches[i+1][j-1] == '.':
            a += 1
if matches[1][-1] == '.':
    a += 1
if matches[4][-1] == '.':
    a += 1
if matches[7][-1] == '.':
    a += 1
for i in [0, 3, 6]:
    for j in [0, 3, 6]:
        if matches[i+1][j] != '.' and matches[i][j+1] != '.' and matches[i+3][j+1] != '.' and matches[i+1][j+3] != '.':
            b += 1
for i in [0, 3]:
    for j in [0, 3]:
        if matches[i+1][j] != '.' and matches[i][j+1] != '.' and matches[i+6][j+1] != '.' and matches[i+1][j+6] != '.'\
                and matches[i+4][j] != '.' and matches[i][j+4] != '.' and matches[i+6][j+4] != '.' and matches[i+4][j+6] != '.':
            b += 1
if '.'not in (matches[0][1], matches[0][4], matches[0][7], matches[1][0], matches[4][0], matches[7][0], matches[1][-1],
              matches[4][-1], matches[7][-1], matches[-1][1], matches[-1][4], matches[-1][7]):
    b += 1

print(a, b)