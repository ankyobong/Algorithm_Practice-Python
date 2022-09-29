from collections import deque


def on_bfs(x, y, check, light):
    queue = deque()
    queue.append([x, y])

    check[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx and nx < m and 0<=ny and ny < n:
                if light[nx][ny] == 0 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    queue.append([nx, ny])


def off_bfs(x, y, check, light):
    queue = deque()
    queue.append([x, y])

    check[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx and nx < m and 0<=ny and ny < n:
                if light[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    queue.append([nx, ny])


global m, n
m, n = map(int, input().split())

light = []

for i in range(m):
    light.append(list(map(int,input().split())))

global dx, dy
dx = [0,0,1,-1]
dy = [1,-1,0,0]

on_check = [[0 for x in range(n)] for y in range(m)]
on_count = 0

for i in range(m):
    for j in range(n):
        if light[i][j] == 0 and on_check[i][j] == 0:
            on_bfs(i,j,on_check,light)
            on_count += 1

off_check = [[0 for x in range(n)] for y in range(m)]
off_count = 0

for i in range(m):
    for j in range(n):
        if light[i][j] == 1 and off_check[i][j] == 0:
            off_bfs(i,j,off_check,light)
            off_count += 1

print(on_count, off_count)