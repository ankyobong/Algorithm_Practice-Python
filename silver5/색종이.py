# https://www.acmicpc.net/problem/2563
dohwazi = [[0]*101 for i in range(101)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            dohwazi[i][j] = 1

result = 0
for row in dohwazi:
    result += row.count(1)
print(result)
