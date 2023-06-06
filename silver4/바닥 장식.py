# https://www.acmicpc.net/problem/1388
def dfs(x, y):
    if floor[x][y] == '-':
        floor[x][y] = 1
        for _y in (1, -1):
            ty = y + _y
            if (0 < ty < m) and floor[x][ty] == '-':
                dfs(x, ty)
    elif floor[x][y] == '|':
        floor[x][y] = 1
        for _x in (1, -1):
            tx = x + _x
            if (0 < tx < n) and floor[tx][y] == '|':
                dfs(tx, y)


n, m = map(int, input().split())
floor = list()
for _ in range(n):
    floor.append(list(input()))

result = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] in ('-', '|'):
            dfs(i, j)
            result += 1
print(result)
