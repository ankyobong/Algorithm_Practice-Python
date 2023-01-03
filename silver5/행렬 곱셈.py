# https://www.acmicpc.net/problem/2740
n, m = map(int, input().split())
a = [[map(int, input().split())]for _ in range(n)]
m, k = map(int, input().split())
b = [[map(int, input().split())]for _ in range(m)]

c = [[0 for _ in range(k)] for _ in range(n)]

for n in range(n):
    for k in range(k):
        for m in range(m):
            c[n][k] += a[n][m] * b[m][k]

for i in c:
    for j in i:
        print(j, end = ' ')
    print()