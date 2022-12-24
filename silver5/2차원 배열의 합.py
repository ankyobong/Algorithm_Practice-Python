# https://www.acmicpc.net/problem/2167
n, m = map(int, input().split())
a = []
list_s = [[0]*(m + 1)for _ in range(n+1)]
for _ in range(n):
    a.append([*map(int, input().split())])

for i in range(1, n+1):
    for j in range(1, m+1):
        list_s[i][j] = a[i-1][j-1] + list_s[i][j - 1] + list_s[i - 1][j] - list_s[i - 1][j - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(list_s[x][y] - list_s[x][j - 1] - list_s[i - 1][y] + list_s[i - 1][j - 1])

